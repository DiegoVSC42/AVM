from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from pydantic import Field, BaseModel
from langchain.globals import set_debug

set_debug(True)

numero_dias = 7
numero_criancas = 3
atividade = "praia"


class Destino(BaseModel):
    cidade: str = Field("A cidade recomendada para visitar")
    motivo: str = Field("motivo pelo qual é interessante visitar essa cidade")


class Restaurantes(BaseModel):
    cidade: str = Field("A cidade recomendada para visitar")
    restaurantes: str = Field("restaurantes recomendados na cidade")


parseador_destino = JsonOutputParser(pydantic_object=Destino)
parseador_restaurantes = JsonOutputParser(pydantic_object=Restaurantes)

prompt_cidade = PromptTemplate(
    template="""
    Sugira uma cidade dado o meu interesse por {interesse}.
    {formato_de_saida}
    """,
    input_variables=["interesse"],
    partial_variables={"formato_de_saida": parseador_destino.get_format_instructions()},
)
prompt_restaurantes = PromptTemplate(
    template="""
    Sugira restaurantes populares entre locais em {cidade}.
    {formato_de_saida}
    """,
    partial_variables={
        "formato_de_saida": parseador_restaurantes.get_format_instructions()
    },
)

prompt_cultural = PromptTemplate(
    template="Sugira atividades e locais culturais em {cidade}"
)
modelo = ChatOllama(
    model="mistral",
    temperature=0.5,
)

cadeia_1 = prompt_cidade | modelo | parseador_destino
cadeia_2 = prompt_restaurantes | modelo | parseador_restaurantes
cadeia_3 = prompt_cultural | modelo | StrOutputParser()

cadeia = cadeia_1 | cadeia_2 | cadeia_3
resposta = cadeia.invoke({"interesse": "praias"})

print(
    f"""
##########################################################################
Prompt Cidade: 
{prompt_cidade.template}
##########################################################################
"""
)
print(
    f"""
##########################################################################
Prompt Restaurantes: 
{prompt_restaurantes.template}
##########################################################################
"""
)
print(
    f"""
##########################################################################
Prompt Cultural: 
{prompt_cultural.template}
##########################################################################
"""
)

print(resposta)
print(
    """
\n##########################################################################\n
    """,
)
