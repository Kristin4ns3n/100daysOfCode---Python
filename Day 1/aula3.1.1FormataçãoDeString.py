def CaracterísticaFísicas():
    nome = "Luiz Otávio"
    altura = 1.80
    peso = 95
    imc = peso/altura ** 2

    print()
    print(nome, 'tem', altura, 'de altura', 'pesa', peso, 'quilos e seu imc é', imc)
    print(f'{nome} tem {altura:.2f} de altura, pesa {peso} de quilos e o seu imc é {imc:.2f}')
    

CaracterísticaFísicas()

#Formatação personalizada de strings

#A classe embutida de string fornece a capacidade de fazer substituições de variáveis complexas e
#formatação de valor por meio do método format(). A classe Formatter no módulo 
#string permite que você crie e personalize seus próprios comportamentos de formatação de strings usando 
#a mesma implementação que o método embutido format().

#class string.Formatter
#print(f'{text }')          #f string 

#Formatação                 #.format()

#Tudo em python é um objeto
#Objeto tem métodos dentro deles 