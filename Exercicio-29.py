# 29.	Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados.

#Inicio
def main():
    opcao: int = 0
    valor: float = 0

    opcao = int(input("Seleciona sua opção de investimento, 1-Poupança / 2-Renda Fixa: "))
    valor = float(input("Digite o valor do investimento: "))

    CalculoInvestimento(opcao, valor)

def CalculoInvestimento(opcao, valor):
    res: float = 0

    if (opcao == 1):
        res = valor*(1.03**30)
        print("Valor final depois de 30 dias:", res)
    elif (opcao == 2):
        res = valor*(1.05**30)
        print("Valor final depois de 30 dias:", res)
    else:
        print("Opção inválida")
#Fim

if (__name__ == "__main__"):
    main();