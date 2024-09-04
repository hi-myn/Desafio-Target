'''3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;'''

import json
with open('dados.json', 'r') as data:
    faturamento = json.load(data)

#vetor para guardar valores do faturamento
valores = []
menor_faturamento = float('inf')
maior_faturamento = float('-inf')
soma_faturamento = 0
dias_com_faturamento = 0

for item in faturamento:
    valor=item['valor']
    if valor > 0:
        valores.append(valor)
        if valor < menor_faturamento:
            menor_faturamento = valor
        if valor > maior_faturamento:
            maior_faturamento = valor
        soma_faturamento += valor
        dias_com_faturamento += 1


# Calculando a média mensal
media_mensal = 0
if dias_com_faturamento > 0:
    media_mensal = soma_faturamento / dias_com_faturamento
else:
    media_mensal = 0


# Contando quantos dias tiveram faturamento superior à média
dias_acima_da_media = 0
for valor in valores:
    if valor > media_mensal:
        dias_acima_da_media += 1

# Exibindo os resultados
print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento superior à média mensal: {dias_acima_da_media}")

