from typing import Dict
from tools.rag_tool import FerramentaRAG, carregar_ou_construir_indice
from config import DOCS, LLM_MODEL
import os


class AgenteMultiRAG:
    """
    Orquestra várias tools (uma por documento).
    Comandos:
      :tools                 -> lista
      :use NOME              -> define tool ativa
      @NOME pergunta         -> usa direto a tool NOME
      texto livre            -> usa a tool ativa
    """

    def __init__(self):
        self.tools: Dict[str, FerramentaRAG] = {}
        self.active_tool: str | None = None

    def carregar_tools(self) -> None:
        for item in DOCS:
            name = item["name"]
            path = item["path"]
            persist = bool(item.get("persist", True))

            if not os.path.exists(path):
                print(f"[AVISO] Arquivo não encontrado para a tool '{name}': {path}")
                continue

            print(f">> Preparando índice para '{name}' (arquivo: {path}) ...")
            vectordb = carregar_ou_construir_indice(name, path, persist=persist)
            self.tools[name] = FerramentaRAG(vectordb, model_name=LLM_MODEL)

        if not self.tools:
            raise ValueError(
                "Nenhuma tool válida foi carregada. Verifique os caminhos em DOCS."
            )

        # define a primeira como ativa
        self.active_tool = next(iter(self.tools.keys()))

    def listar_tools(self) -> str:
        linhas = []
        for name in self.tools.keys():
            mark = " *" if name == self.active_tool else ""
            linhas.append(f"- {name}{mark}")
        return "Tools disponíveis:\n" + "\n".join(linhas) + "\n\n( * = ativa )"

    def set_active(self, name: str) -> str:
        if name not in self.tools:
            return (
                f"Tool '{name}' não encontrada. Use ':tools' para ver as disponíveis."
            )
        self.active_tool = name
        return f"Tool ativa agora é: {name}"

    def responder(self, entrada: str) -> str:
        entrada = entrada.strip()

        # listar
        if entrada.lower() in {":tools", ":ls"}:
            return self.listar_tools()

        # trocar ativa
        if entrada.lower().startswith(":use "):
            nome = entrada.split(" ", 1)[1].strip()
            return self.set_active(nome)

        # prefixo @
        if entrada.startswith("@"):
            try:
                nome, pergunta = entrada[1:].split(" ", 1)
            except ValueError:
                return "Formato inválido. Use '@nome_da_tool sua pergunta'."
            nome = nome.strip()
            pergunta = pergunta.strip()
            tool = self.tools.get(nome)
            if not tool:
                return f"Tool '{nome}' não encontrada. Use ':tools' para ver as disponíveis."
            if not pergunta:
                return "Escreva sua pergunta após o nome da tool, por favor."
            return tool(pergunta)

        # sem prefixo: usa ativa
        if not self.active_tool:
            return "Nenhuma tool ativa. Use ':tools' para listar e ':use NOME' para ativar."
        return self.tools[self.active_tool](entrada)
