#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shelve
from arquivo_unificado import arquivo_unificado
from thread import thread
from os import environ

codigo_cidade = '90670'
candidatos = arquivo_unificado(
    'https://resultados.tse.jus.br',
    'oficial',
    'ele2024',
    '619',
    'mt',
    codigo_cidade,
    '11'
)

# Check se já foi postado
data_hora = candidatos[0]['dg'] + ' ' + candidatos[0]['hg']
with shelve.open('/tmp/eleicoes', 'c') as cache:
    if cache.get(codigo_cidade) == data_hora:
        #print( 'igual')
        exit()

    else:
        cache[codigo_cidade] = data_hora
        #print( 'diferente')

cta = 'Atualização da #eleicao municipal para prefeito em #Cuiaba - #MT \n\n'
posts = [ cta + candidatos[0]['pst'].replace(',', '.') + '% das seções totalizadas às ' + candidatos[0]['hg']  + ' de ' + candidatos[0]['dg'] + '\n\nSiga o fio!' ]
for candidato in candidatos:
    msg = cta + candidato['cand']['nmu'] + ', ' + candidato['sg'] + ' - ' + candidato['cand']['n'] + ' \n';

    if candidato['cand']['st']:
        msg += candidato['cand']['st'] + ' com '

    msg += candidato['cand']['vap'] + ' (' + candidato['cand']['pvap'].replace(',', '.') + '%) dos votos \n\n' + \
        candidatos[0]['pst'].replace(',', '.') + '% das seções totalizadas às ' + candidatos[0]['hg']  + ' de ' + candidatos[0]['dg']
    posts.append( msg )

thread(
    environ['BASE_URL'],
    environ['LOGIN'],
    environ['PASSWORD'],
    posts
)
