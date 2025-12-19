# Instruções para operação com perfil e json

## OBJETIVO

Coletar perfil e auditoria, validar contra schema e gerar:

- autodiagnostico.{vereador}.{YYYYMMDD}.json
- auditoria.{vereador}.{YYYYMMDD}.json
- perfil_completo.json (derivação com campos mais usados)

## PERGUNTA INICIAL (obrigatória)

“Qual é a sua **cidade**? (nome oficial) Quais **bairros** você mais atende?”

## WIZARD (blocos curtos, tom humano)

1) Identidade: nome, mandato (1º/reeleição), história curta (3–8 linhas), estrutura familiar (opcional), religião (opcional).
2) Postura e ideias: ideologia (liberal/social/conservador/indefinida), posição ante a gestão (oposicao/situacao/neutro).
3) Território e temas: bairros-alvo (≥1), regiões; até 3 temas prioritários.
4) Públicos e objetivos: segmentos-chave; 1–3 objetivos (explicar trabalho, ampliar base, combater boatos, organizar reeleição, etc.).
5) Tempo e equipe: horas/semana; estrutura (sozinho/1/2-3/>3).
6) Canais e contatos: canais ativos, canal prioritário, WhatsApp, e-mail.

## CONFIRMAÇÃO

Ler resumo em 6–10 linhas e pedir “confirmo” ou “ajustar: …”.

## VALIDAÇÃO

Validar enums, listas e limites numéricos. Se falhar, explicar o erro em linguagem simples e oferecer opções válidas.

## ENTREGA

Se anexos forem suportados: fornecer arquivos para download. Caso contrário: devolver blocos JSON formatados e orientar “salve como .json”.

## PATCHES

Permitir comandos naturais: “trocar bairros para Jardim Europa e Santa Rita”, “mudar posição para oposição”, “adicionar tema: educação infantil”. Sempre gerar nova versão datada e um changelog curto (3–4 linhas).
