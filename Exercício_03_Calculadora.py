# ============================================
# Exercício 03 - Calculadora
# Autor: Josué
# Linguagem: Python
# ============================================

def mostrar_menu():
    print("\n" + "=" * 40)
    print("        CALCULADORA PYTHON")
    print("=" * 40)
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")
    print("=" * 40)


def calcular(opcao, num1, num2):

    if opcao == 1:
        return num1 + num2

    elif opcao == 2:
        return num1 - num2

    elif opcao == 3:
        return num1 * num2

    elif opcao == 4:
        if num2 == 0:
            return "Erro: não é possível dividir por zero."

        return num1 / num2


while True:

    mostrar_menu()

    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 0:
            print("\nPrograma encerrado.")
            break

        if opcao not in [1, 2, 3, 4]:
            print("\nOpção inválida. Tente novamente.")
            continue

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        resultado = calcular(opcao, num1, num2)

        print("\nResultado:", resultado)

    except ValueError:
        print("\nErro: digite apenas números.")


print("=" * 40)
print("       FIM DO EXERCÍCIO 03")
print("=" * 40)