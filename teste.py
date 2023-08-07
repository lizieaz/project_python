# Mostrando informações
print("Olá, Mundo")

# Recebendo informações
input("Qual o seu nome?")

# Armazenando informações como variáveis
projeto = "Desenvolvimento Python"
print(projeto)
## toda informação no input é texto (string)
projeto = input("Digite o nome do projeto: ")
horas_previstas = int(input("Digite a quantidade de horas previstas: "))
valor_hora = int(input("Digite o valor da hora trabalhada: "))
prazo = int(input("Digite o prazo em meses: "))

type(valor_hora)

# Calculando o valor total do projeto
valor_projeto = int(horas_previstas) * int(valor_hora)