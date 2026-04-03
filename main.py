# importações
import csv
import funcoes as f

# variaveis
dataset = 'PokemonStats.csv'
maior_hp = soma_hp = maior_attack = soma_attack = contador = contador_hp_validos = contador_atk_validos = 0
menor_hp = 250
menor_attack = 134
lista_filtro1 = []
lista_filtro2 = []
lista_filtro3 = []

with open(dataset, 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo) # lê cada linha do database como um dicionário onde as chaves são os nomes das colunas
    for registro in leitor:
        # dados relevantes
        hp = registro['HP'].strip() 
        attack = registro['Attack'].strip() 
        sp_attack = registro['SpAtk'].strip()            
        velocidade = registro['Speed'].strip()
        tipo1 = registro['Type1'].strip()
        tipo2 = registro['Type2'].strip()

        if hp != '': # analise dos dados da coluna hp
            hp = int(hp)
            if hp >= 0:
                contador_hp_validos += 1 # casos validos
                soma_hp += hp
                if hp > maior_hp: 
                    maior_hp = hp
                if hp < menor_hp:
                    menor_hp = hp

        if attack != '': # analise dos dados da coluna attack
            attack = int(attack)
            if attack >= 0:
                contador_atk_validos += 1 # casos validos
                soma_attack += attack
                if attack > maior_attack:
                    maior_attack = attack
                if attack < menor_attack:
                    menor_attack = attack

        if hp > 60: # reúne componentes do filtro 1 (tipo Normal e hp > 60)
            if tipo1 == 'Normal' or tipo2 == 'Normal':
                lista_filtro1.append(registro['Name'])

        if attack < 80: # reune componentes do filtro 2 (tipo agua, speed > 80 e attack < 80)
            if velocidade != '':
                velocidade = int(velocidade)
                if velocidade > 80:
                    if tipo1 == 'Water' or tipo2 == 'Water':
                        lista_filtro2.append(registro['Name']) 

        if sp_attack != '': # reune componentes do filtro 3 (speed >= 100 e spatk >=s 100)
            sp_attack = int(sp_attack)
            if sp_attack >= 100:
                if velocidade != '':
                    velocidade = int(velocidade)
                    if velocidade >= 100:
                        lista_filtro3.append(registro['Name'])

        contador += 1 # quantidade de registros
        if contador < 6:
            print(registro) # mostra os 5 primeiros registros

# exposição dos dados
print(f'O Dataset {dataset} possui {contador} registros') # quantidade de registros
print(f'Nomes das colunas: {leitor.fieldnames}') # nome das colunas
print(f'Dados sobre HP: Valor Máximo: {maior_hp}. Valor mínimo: {menor_hp}. Média Aritmética: {f.media(soma_hp, contador_hp_validos):.2f}. Valores válidos: {contador_hp_validos}. Valores inválidos: {contador - contador_hp_validos}') # dados sobre coluna HP
print(f'Dados sobre Attack: Valor Máximo: {maior_attack}. Valor mínimo: {menor_attack}. Média Aritmética: {f.media(soma_attack, contador_atk_validos):.2f}. Valores válidos: {contador_atk_validos}. Valores inválidos: {contador - contador_atk_validos}') # dados sobre coluna Attack
print(f'Filtro 1: Pokemons do Tipo Normal com HP acima de 60. Registros: {f.imprime_lista(lista_filtro1, 10)}. Total de ocorrências: {len(lista_filtro1)}') # Filtro 1
print(f'Filtro 2: Pokemons do Tipo Água com Speed acima de 80 e Attack abaixo de 80. Registros: {f.imprime_lista(lista_filtro2, 10)}. Total de ocorrências: {len(lista_filtro2)}') # Filtro 2
print(f'Filtro 3: Pokemons Sweepers (alta velocidade e ataque especial para finalizar adversários). Registros: {f.imprime_lista(lista_filtro3, 10)}. Total de ocorrências: {len(lista_filtro3)}') # Filtro 3

# geração do relatório TXT
with open('relatorio.txt', 'w', encoding='utf-8') as arquivo:
    