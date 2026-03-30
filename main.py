# importações
import csv
import funcoes as f

# variaveis
dataset = 'PokemonStats.csv'
maior_hp = soma_hp = maior_attack = soma_attack = contador = contador_hp_validos = contador_atk_validos = 0
menor_hp = 250
menor_attack = 134
lista_filtro1 = lista_filtro2 = []

with open(dataset, 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for registro in leitor:
        for chave in registro:
            if chave == "HP":
                registro[chave] = int(registro[chave])
                if registro[chave] > maior_hp:
                    maior_hp = registro[chave]
                if registro[chave] < menor_hp:
                    menor_hp = registro[chave]
                soma_hp += registro[chave]
                if registro[chave] != " " and registro[chave] > 0:
                    contador_hp_validos += 1

                if registro[chave] > 60:
                    if registro['Type1'] == 'Normal' or registro['Type2'] == 'Normal':
                        lista_filtro1.append(registro['Name'])

            if chave == "Attack":
                registro[chave] = int(registro[chave])
                if registro[chave] > maior_attack:
                    maior_attack = registro[chave]
                if registro[chave] < menor_attack:
                    menor_attack = registro[chave]
                soma_attack += registro[chave]
                if registro[chave] != " " and registro[chave] > 0:
                    contador_atk_validos += 1

        contador += 1
        if contador < 6:
            print(registro) # mostra os 5 primeiros registros

    print(f'O Dataset {dataset} possui {contador-1} arquivos') # quantidade de registros
    print(f'Nomes das colunas: {leitor.fieldnames}') # nome das colunas
    print(f'Dados sobre HP: Valor Máximo: {maior_hp}. Valor mínimo: {menor_hp}. Média Aritmética: {f.media(soma_hp, contador):.2f}. Valores válidos: {contador_hp_validos - 1}. Valores inválidos: {contador - contador_hp_validos}') # dados sobre coluna HP
    print(f'Dados sobre Attack: Valor Máximo: {maior_attack}. Valor mínimo: {menor_attack}. Média Aritmética: {f.media(soma_attack, contador):.2f}. Valores válidos: {contador_atk_validos - 1}. Valores inválidos: {contador - contador_atk_validos}') # dados sobre coluna Attack
    print(f'Filtro 1: Pokemons do Tipo Normal com HP acima de 60. Registros: {f.imprime_lista(lista_filtro1, 10)}. Total de ocorrências: {len(lista_filtro1)}') # Filtro 1
