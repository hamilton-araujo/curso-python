import decimal

numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.7)
numero_3 = numero_1 + numero_2

numero_4 = decimal.Decimal("0.1")
numero_5 = decimal.Decimal("0.7")
numero_6 = numero_4 + numero_5

print(numero_3)
print(f"{numero_3:.2f}")
print(round(numero_3, 2))
# A função Decimal.from_float() converte um float para um Decimal
print(numero_6)