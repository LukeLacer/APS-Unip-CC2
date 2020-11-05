import json #modulo que gerencia o json
import dados, moldura, imprime

#pega o json e joga no dicionario dados_reciclaveis
with open('data/dados_reciclaveis.json', encoding="utf8") as f:
    dados_reciclaveis = json.load(f)

imprime.titulo()
imprime.entrada()
imprime.menu()