#Entrada: Mensagem de boas-vindas, identificação do tripulante e valores para os cálculos de conversão. .✦ ݁˖

print("Olá! Seja bem-vindo(a) ao SAAT (Sistema De Apoio para Astronautas)! /ᐠ ◝ ⩊ ◜ マ₊˚⊹♡₊ ⊹ ")
nome_do_usuario = input("Por favor, digite seu nome completo: ")
print("Por gentileza, forneça no formulário abaixo as informações requeridas: ")
distancia = input("𖹭.ᐟInsira a distância da sua viagem em km: ")
velocidade = input("𖹭.ᐟInsira a velocidade da sua nave: ")
destino = input("𖹭.ᐟinsira o destino final: ")

#Processamento: Conversão dos valores inseridos em horas/dia para a saída de dados. .✦ ݁˖

distancia = float(distancia)
velocidade = float(velocidade)
tempo_em_horas = distancia/velocidade
horas_do_dia = 24
tempo_em_dias = tempo_em_horas/horas_do_dia

#Saída: Resultados dos cálculos de conversão e mensagem de despedida. .✦ ݁˖

print("Estimado(a) Astronauta " +nome_do_usuario+", o sistema SAAT calculou o tempo previsto de sua viagem para "
"" +destino+".")
print("Considerando uma distância de", distancia,"km, com velocidade de", velocidade,"km/h, a estimativa em horas "
"é de "f"{tempo_em_horas:.2f}, o que equivale a {tempo_em_dias:.2f} dias!!! ദ്ദി/ᐠ - ⩊ -マ.ᐟ")
print("Tenha uma ótima viagem e aproveite a vista. ฅ₍^˵◝ ⩊ ◜˵マⳊ")
