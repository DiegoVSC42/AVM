import re
import pandas as pd

def extrair_decisoes(texto_markdown):
    decisoes = []
    
    # Encontrar todas as decisões
    padroes_decisao = re.finditer(r'### Decisão ([\d.]+): (.+?)\n\n\*\*Contexto:\*\* (.+?)\n\n\*\*Pergunta:\*\* (.+?)\n\n---', texto_markdown, re.DOTALL)
    
    for match_decisao in padroes_decisao:
        decisao_id = match_decisao.group(1)
        titulo = match_decisao.group(2).strip()
        contexto = match_decisao.group(3).strip()
        pergunta = match_decisao.group(4).strip()
        
        # Extrair fase do ID (exemplo: 1.1 -> fase 1)
        fase = int(decisao_id.split('.')[0])
        
        # Encontrar o início desta decisão
        inicio_decisao = match_decisao.end()
        
        # Encontrar próxima decisão ou fim do texto
        proxima_decisao = re.search(r'### Decisão', texto_markdown[inicio_decisao:])
        if proxima_decisao:
            fim_decisao = inicio_decisao + proxima_decisao.start()
        else:
            fim_decisao = len(texto_markdown)
        
        bloco_decisao = texto_markdown[inicio_decisao:fim_decisao]
        
        # Extrair todas as opções (A, B, C, D)
        opcoes = re.finditer(r'\*\*Opção ([A-D])\) (.+?)(?:🎯|✅|⚠️|❌)?\s*\((.+?)\)\*\*\n\n(.*?)\n\n\*\*Feedback:\*\* (.+?)\n\n\*\*Dica do Vitorino:\*\* \*"(.+?)"\*', bloco_decisao, re.DOTALL)
        
        ordem = 0
        for match_opcao in opcoes:
            letra = match_opcao.group(1)
            texto_opcao = match_opcao.group(2).strip()
            tipo_opcao = match_opcao.group(3).strip().lower()
            tabela = match_opcao.group(4)
            feedback = match_opcao.group(5).strip()
            dica = match_opcao.group(6).strip()
            
            # Extrair dados da tabela
            custos = extrair_custos(tabela)
            impactos = extrair_impactos(tabela)
            
            decisao = {
                'decisaoId': decisao_id,
                'fase': fase,
                'titulo': titulo,
                'contexto': contexto,
                'situacao': '',
                'pergunta': pergunta,
                'ativo': True,
                'ordem': ordem,
                'opcaoLetra': letra,
                'opcaoTexto': texto_opcao,
                'opcaoTipo': tipo_opcao,
                'custoDinheiro': custos['dinheiro'],
                'custoTempo': custos['tempo'],
                'custoEnergia': custos['energia'],
                'impactoVotos': impactos['votos'],
                'impactoContatos': impactos['contatos'],
                'impactoReputacao': impactos['reputacao'],
                'feedbackEducacional': feedback,
                'dicaVitorino': dica
            }
            
            decisoes.append(decisao)
            ordem += 1
    
    return decisoes

def extrair_custos(tabela):
    custos = {'dinheiro': 0, 'tempo': 0, 'energia': 0}
    
    # Procurar linha de custos
    match_custos = re.search(r'\*\*Custos\*\*\s*\|\s*(.+?)\s*\|', tabela)
    if match_custos:
        linha_custos = match_custos.group(1)
        
        # Extrair dinheiro (R$ XXX)
        match_dinheiro = re.search(r'R\$\s*([\d.]+)', linha_custos)
        if match_dinheiro:
            custos['dinheiro'] = float(match_dinheiro.group(1).replace('.', ''))
        
        # Extrair tempo
        match_tempo = re.search(r'(-?\d+)\s*tempo', linha_custos)
        if match_tempo:
            custos['tempo'] = int(match_tempo.group(1))
        
        # Extrair energia
        match_energia = re.search(r'(-?\d+)\s*energia', linha_custos)
        if match_energia:
            custos['energia'] = int(match_energia.group(1))
        
        # Verificar se é "Nenhum"
        if 'Nenhum' in linha_custos or 'nenhum' in linha_custos:
            custos = {'dinheiro': 0, 'tempo': 0, 'energia': 0}
    
    return custos

def extrair_impactos(tabela):
    impactos = {'votos': 0, 'contatos': 0, 'reputacao': 0}
    
    # Extrair votos
    match_votos = re.search(r'\*\*Votos\*\*\s*\|\s*([+-]?[\d.]+)%', tabela)
    if match_votos:
        impactos['votos'] = float(match_votos.group(1))
    
    # Extrair contatos
    match_contatos = re.search(r'\*\*Contatos\*\*\s*\|\s*([+-]?\d+)', tabela)
    if match_contatos:
        impactos['contatos'] = int(match_contatos.group(1))
    
    # Extrair reputação
    match_reputacao = re.search(r'\*\*Reputação\*\*\s*\|\s*([+-]?[\d.]+)', tabela)
    if match_reputacao:
        impactos['reputacao'] = float(match_reputacao.group(1))
    
    return impactos

# Ler o arquivo markdown
with open('decisoes.md', 'r', encoding='utf-8') as f:
    texto_markdown = f.read()

# Extrair todas as decisões
decisoes = extrair_decisoes(texto_markdown)

# Criar DataFrame
df = pd.DataFrame(decisoes)

# Salvar em Excel
df.to_excel('decisoes_extraidas.xlsx', index=False, engine='openpyxl')

# Ou salvar em CSV
df.to_csv('decisoes_extraidas.csv', index=False, encoding='utf-8-sig')

print(f"Extração concluída! {len(decisoes)} opções extraídas de {len(decisoes)//4} decisões.")
print(f"Arquivos gerados: decisoes_extraidas.xlsx e decisoes_extraidas.csv")