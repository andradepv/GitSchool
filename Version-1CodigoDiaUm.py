def caixa_eletronico():
    # Solicitar o valor do saque ao usuário
    valor_saque = int(input("Digite o valor do saque (entre 10 e 600 reais): "))

    # Verificar se o valor está dentro do intervalo permitido
    if valor_saque < 10 or valor_saque > 600:
        print("Valor inválido! O valor do saque deve estar entre 10 e 600 reais.")
        return

    # Inicializar a quantidade de notas de cada valor
    notas_100 = notas_50 = notas_10 = notas_5 = notas_1 = 0

    # Calcular a quantidade de notas de cada valor
    if valor_saque >= 100:
        notas_100 = valor_saque // 100
        valor_saque %= 100
    if valor_saque >= 50:
        notas_50 = valor_saque // 50
        valor_saque %= 50
    if valor_saque >= 10:
        notas_10 = valor_saque // 10
        valor_saque %= 10
    if valor_saque >= 5:
        notas_5 = valor_saque // 5
        valor_saque %= 5
    if valor_saque >= 1:
        notas_1 = valor_saque // 1
        valor_saque %= 1

    # Exibir a quantidade de notas de cada valor
    print(f"Notas de 100: {notas_100}")
    print(f"Notas de 50: {notas_50}")
    print(f"Notas de 10: {notas_10}")
    print(f"Notas de 5: {notas_5}")
    print(f"Notas de 1: {notas_1}")

# Chamar a função principal
caixa_eletronico()
