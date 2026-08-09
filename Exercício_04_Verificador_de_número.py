# ============================================
# Exercício 05 - Verificador de Número
# Autor: Josué
# Linguagem: Python
# Descrição: Programa que verifica se um número
# é positivo, negativo ou igual a zero.
# ============================================

print("=" * 45)
print("       VERIFICADOR DE NÚMERO")
print("=" * 45)

numero = float(input("Digite um número: "))

print("\nRESULTADO")
print("-" * 45)

if numero > 0:
    print("O número é POSITIVO.")
elif numero < 0:
    print("O número é NEGATIVO.")
else:
    print("O número é IGUAL A ZERO.")

print("=" * 45)
print("       FIM DO PROGRAMA")
print("=" * 45)