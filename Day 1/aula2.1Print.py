def Print():                #Print() == is a function
    Nome = input("Digite o nome do cliente: ")
    DataVencimento = input("Digite o dia de vencimento: ")
    ValorFatura = input("Digite o valor da fatura: ") 

    print()
    print(f"Nome: {Nome} \tData de vencimento: {DataVencimento} \tFatura: R${ValorFatura}")

Print()

#This is really beautiful

#\n = Quebra de linha - br
#Esse caractere é digitado escapando-se a letra "n" com uma barra invertida - a famosa sequência "\n" 
#quando o parser do Python encontra essa sequência dentro de uma string ela é automaticamente convertida 
#para o caractere de quebra de linha usado em sistemas Unix, que é universal (o "print" depois converte 
#para a sequência correta em cada sistema operacional):

#Formatação de string 