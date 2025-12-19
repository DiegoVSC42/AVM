import warnings

warnings.filterwarnings("ignore")
from langchain.tools import BaseTool
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_community.llms import Ollama
from pydantic import BaseModel, Field
from typing import List, Optional, ClassVar
import pandas as pd
import json


def busca_dados_de_estudante(estudante: str) -> dict:
    dados = pd.read_csv("documentos/estudantes.csv")
    dados["USUARIO"] = dados["USUARIO"].str.lower().str.strip()
    estudante = estudante.lower().strip()
    dados_com_esse_estudante = dados[dados["USUARIO"] == estudante]
    if dados_com_esse_estudante.empty:
        return {}
    return dados_com_esse_estudante.iloc[0].to_dict()


class DadosDeEstudante(BaseTool):
    name: ClassVar[str] = "DadosDeEstudante"
    description: ClassVar[str] = (
        "Use esta ferramenta quando o usuário fizer perguntas relacionadas a um estudante específico, como 'Ana'. "
        "Ela extrai dados como histórico escolar, interesses e preferências do estudante com base no nome. "
        "Passe como argumento o nome do estudante (ex: 'ana', 'joão', 'maria'). "
        "Use essa ferramenta antes de tentar criar um perfil acadêmico ou fazer recomendações personalizadas."
    )

    class ExtratorDeEstudante(BaseModel):
        estudante: str = Field(
            description="Nome do estudante informado, sempre em letras minúsculas. "
        )

    def _run(self, input: str) -> str:
        llm = Ollama(model="mistral")
        parser = JsonOutputParser(pydantic_object=self.ExtratorDeEstudante)

        template = PromptTemplate(
            template="""Você deve analisar a entrada a seguir e extrair o nom de usuario informado.
            Entrada:
            -------------------
            {input}
            -------------------

Formato de saída:
{formato_saida}
""",
            input_variables=["input"],
            partial_variables={"formato_saida": parser.get_format_instructions()},
        )

        cadeia = template | llm | parser
        resposta = cadeia.invoke({"input": input})
        estudante = resposta["estudante"]

        if isinstance(estudante, list):
            estudante = estudante[0]

        estudante = str(estudante).strip().lower()
        dados = busca_dados_de_estudante(estudante)
        # print("\nAchei")
        # print(dados)
        return json.dumps(dados)


class Nota(BaseModel):
    area_de_conhecimento: str = Field(description="Área de conhecimento da disciplina")
    nota: float = Field(description="Nota obtida na area")


class PerfilAcademicoDeEstudante(BaseModel):
    nome: str = Field(description="Nome do estudante")
    ano_de_conclusao: int = Field(description="Ano de conclusão do ensino médio")
    notas: List[Nota] = Field(
        description="Lista de notas das disciplinas e áreas de conhecimento"
    )
    resumo: str = Field(
        description="Resumo das principais características do estudante de forma a torná-lo único e atraente para universidades"
    )


class PerfilAcademico(BaseTool):
    name: ClassVar[str] = "PerfilAcademico"
    description: ClassVar[str] = (
        "Cria um perfil acadêmico de um estudante. "
        "Esta ferramenta requer como entrada todos os dados do estudante. "
        "Eu sou incapaz de buscar os dados do estudante. "
        "Você tem que buscar os dados do estudante antes de me invocar."
    )

    def _run(self, input: str) -> str:
        llm = Ollama(model="mistral")
        parser = JsonOutputParser(pydantic_object=PerfilAcademicoDeEstudante)

        template = PromptTemplate(
            template="""
- Formate o estudante para seu perfil acadêmico. 
- Com os dados, identifique as opções de universidades sugeridas e cursos compatíveis com o interesse do aluno.
- Destaque o perfil do aluno dando ênfase principalmente naquilo que faz sentido para instituições de interesse do aluno.

Persona: você é uma consultora de carreira e precisa indicar com detalhes, riqueza, mas de forma direta ao ponto, para o estudante, as opções e consequências possíveis.

Informações atuais:

{dados_do_estudante}
{formato_de_saida}
""",
            input_variables=["dados_do_estudante"],
            partial_variables={"formato_de_saida": parser.get_format_instructions()},
        )

        cadeia = template | llm | parser
        resposta = cadeia.invoke({"dados_do_estudante": input})
        return resposta

    def _arun(self, input: str):
        raise NotImplementedError("Esta ferramenta não suporta execução assíncrona.")
