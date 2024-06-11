# Conversão de Tipos 
# Coerção

# Type convertion, typecasting, coercion é o ato de converter um tipo em outro 
# Tipos imutáveiss e primitivos: [str, int, float, bool]
# str, int, float e bool == tipos imutáveis. Não sofrem alteração durante o desenvolvimento 

# Como no Python não é uma linguagem estática, ou seja, não precisa declarar o tipo ao se declarar a variável
# Linguagens de tipagem dinâmica e fraca: PHP e JavaScript 

# Polimorfismo

A = '1'
print(f'Data: {int(A)}', type(A))                           #print(int(A), type(A))

B = 1.1
print(f'Data: {int(B)}', type(B)) 

A = 1
print(f'Data: {float(A)}', type(A)) 

print(f'Data: {bool("")}')                                 # Empty String. Typecasting of a String to Boolean --> Bool = False
print(f'Data: {bool(" ")}')                                # String --> Bool = True
print()
print(A + B)


