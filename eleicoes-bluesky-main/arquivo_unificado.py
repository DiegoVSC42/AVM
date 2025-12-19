import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import locale
import warnings # ambiente local

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
warnings.simplefilter('ignore', InsecureRequestWarning) # ambiente local


def arquivo_unificado(host, ambiente, ciclo, eleicao, uf, municipio, cargo):
    '''
    EA20 – Arquivo de resultado unificado
    See https://www.tse.jus.br/eleicoes/informacoes-tecnicas-sobre-a-divulgacao-de-resultados
    '''

    url = host + '/' + ambiente + '/' + ciclo + '/' + eleicao + '/dados/' + uf + '/' + uf +  municipio.zfill(5) + '-c' + cargo.zfill(4) + '-e' + eleicao.zfill(6) + '-u.json'

    try:
        response = requests.get(url, verify=False) # ambiente local
        response.raise_for_status()
        data = response.json()

        result = []
        for carg in data['carg']:
            for agr in carg['agr']:
                for par in agr['par']:
                    for cand in par['cand']:
                        cand['vap'] = locale.format_string('%d', int(cand['vap']), grouping=True)
                        candidato = {
                            'dg': data.get('dg'), # Data da geração do arquivo
                            'hg':  data.get('hg'), # Hora da geração do arquivo
                            'pst': data['s'].get('pst'), # Percentual de Seções Totalizadas
                            'sg': par['sg'], # Sigla do partido
                            'cand': cand
                        }
                        result.append(candidato)

        return sorted(result, key=lambda x: int(x['cand']['seq']))

    except requests.exceptions.RequestException as e:
        print(e)
