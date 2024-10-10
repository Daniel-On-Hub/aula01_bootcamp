CONSTANTE_BONUS = 1000

# 1) Solicite ao usuário que digite o nome.
nome_usuario = input("Digite seu Nome: ")

# 2) Solicite ao usuário que digite o valor do seu salário
# Converter a entrada para um número de ponto flutuante
salario_usuario = float(input("Digite seu Salario: "))

# 3) Solicite ao usuario que digite o valor do bonus recebido
# converter a entrada para um numero de ponto flutuante
bonus_salario = float(input("Digite seu bonus: "))


# 4) Calcule o valor do bônus
valor_bonus = CONSTANTE_BONUS + salario_usuario * bonus_salario

# 5) Imprime a mensagem personalizada incluindo o nome de usuario e o valor
print(f"O usuario {nome_usuario} possui o bonus de {valor_bonus}")