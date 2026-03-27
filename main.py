import csv

dataset = 'PokemonStats.csv'
contador = 0

with open(dataset, 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for registro in leitor:
        contador += 1
        if contador < 6:
            print(registro)
    print(f'O Dataset {dataset} possui {contador-1} arquivos')
    print(f'Nomes das colunas: {leitor.fieldnames}')