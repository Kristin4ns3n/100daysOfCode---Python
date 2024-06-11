#Tudo em python é um objeto
#Objeto tem métodos dentro deles 

#.format()

a = 'A'                                #This is a String 
b = 'B'
c = 1.1    

convertedA = int(a)
convertedB = int(b)

formato = a + b + c                    #ERROR - can only concatenate str (not "float") to st
#formato = ''.format(a, b, c)
print(formato.format(a, b, c))