'''4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
'''
from decimal import Decimal

faturamento_sp = Decimal('67836.43')
faturamento_rj = Decimal('36678.66')
faturamento_mg = Decimal('29229.88')
faturamento_es = Decimal('27165.48')
faturamento_outros = Decimal('19849.53')

Valor_total_mensal = faturamento_sp + faturamento_rj + faturamento_mg + faturamento_es + faturamento_outros

Sp_percentural = (faturamento_sp / Valor_total_mensal) *100
Rj_percentural =  (faturamento_rj / Valor_total_mensal) *100
Mg_percentural = (faturamento_mg / Valor_total_mensal) *100
Es_percentural = (faturamento_es / Valor_total_mensal) *100
Outros_percentural = (faturamento_outros / Valor_total_mensal) *100

print(f"Percentual de São Paulo: {Sp_percentural:.2f}%")
print(f"Percentual do Rio de Janeiro: {Rj_percentural:.2f}%")
print(f"Percentual de Minas Gerais: {Mg_percentural:.2f}%")
print(f"Percentual do Espírito Santo: {Es_percentural:.2f}%")
print(f"Percentual dos outros: {Outros_percentural:.2f}%")