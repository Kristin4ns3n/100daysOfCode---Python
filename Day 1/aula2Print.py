print('First')
print(12, 34, sep=" ", end='\n')  #separador     #end == final de print, útlimo argumento 
print(56, 78, sep=' ')            #argumento sep (padrão) com aspas simples 
print()                           #Espaço de linha 

print('Second')                   #Espaço de linha 
print(12, 34, sep=' ') 
print(56, 78, end='\n\n') 
#print('\n')                      #Suddenly I have two breaks instead of one

print('Third')                    #Espaço de linha 
print(12, 34, sep='-')
print(56, 78, sep='-.-')

#É uma função. 
#Recebe um argumento entre os parênteses ()

#Por padrão a função print no python faz uma quebra de linha
#Diferente da linguagem C onde temos que explicitálo \n \t
#Quebra de linha: Carryedge Return Line Feed (CRLF) == quebra de linha específica do Windows  \r \n 
#                 LF == Line Feed \n
#                 \r\n == CRLF == Windowns
#                 \n == LF == Unix

#Argumentos são pasados em funções ou métodos entre parênteses 
#Argumentos não nomeados #Study

#Exibe alguma informação na tela. 
#Exibe um output