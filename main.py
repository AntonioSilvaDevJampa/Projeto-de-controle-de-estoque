## Programa de controle de estoque##
# Primeiro importar a biblioteca datetime para fazer uso de datas

from datetime import date, time,  datetime, timedelta


# usar o input para digitar o nome do funcionario

nome_do_funcionario = input(' Digite o seu nome ')

print(f' Obrigado pela identificação , {nome_do_funcionario}')

# usar o datetime para formatar a data 

import pytz

brasilia_timezone = pytz.timezone("America/Sao_Paulo")

datetime_brasilia = datetime.now(brasilia_timezone)

# formata a data e hora no padrão desejado

formatted_datetime = datetime_brasilia.strftime("%d-%m-%Y %H:%M:%S")

print("Data e hora no fuso horário do Brasil:", formatted_datetime)

#now = datetime.now()

# formatar a hora no formato brasileiro (dd/mm/yyy hh:mm:ss)

#br_time = now.strftime("%d/%m/%Y %H:%M:%S")

## Usar o imput para registrar a data ##

data_entrada = input(f' digite a data de hoje ')

data_hora = datetime.strptime(data_entrada, '%d/%m/%Y')

print(f' A data de hoje é , {data_entrada}')

## Registrar qual produto entrou no estoque nessa data ##

produto = input( ' digite qual o produto que entrou no estoque hoje ')

print(f' O produto que entrou no estoque hoje foi , {produto}' )

## usar o input para determinar a quantidade do produto ##

quantidade = input(' digite a quantidade ')

print(f' a quantidade do produto é de {quantidade}')

data_val = input( 'Digite a data de validade do produto ')

print(f' A data de validade do produto é , {data_val}')


















               
