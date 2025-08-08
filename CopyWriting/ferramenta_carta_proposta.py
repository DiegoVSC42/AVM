from docx import Document
from langchain.tools import BaseTool
from typing import ClassVar, Optional


def busca_paragrafos_relevantes(path, query) -> str:
    doc = Document(path)
    resultados = []
    palavras = [
        pal.strip().lower() for pal in query.replace("?", "").split() if len(pal) > 2
    ]

    for paragrafo in doc.paragraphs:
        texto = paragrafo.text.strip()
        texto_lc = texto.lower()
        if texto and any(palavra in texto_lc for palavra in palavras):
            resultados.append(texto)

    if resultados:
        return "\n\n".join(resultados)
    else:
        return "Não encontrei essa informação na carta proposta."


class DadosCartaProposta(BaseTool):
    name: ClassVar[str] = "CartaPropostaCursoVereador"
    description: ClassVar[
        str
    ] = """
    Ferramenta que procura respostas no conteúdo do arquivo docx da carta proposta do curso 'Eu vereador Mandato'.
    Busca por palavras relevantes da sua pergunta, retornando todos os parágrafos do arquivo que mencionam qualquer uma delas.
    """
    path: Optional[str] = None

    def _run(self, query: str) -> str:
        if not self.path:
            return "Arquivo não especificado."
        resultado = busca_paragrafos_relevantes(self.path, query)
        return resultado
