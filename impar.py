import os 

os.system("cls")

par = 0

impar = 0

for i in range(1,6,1):
    
    numero = int(input(f"Digite valor {i} = "))
    
    if  numero % 2 == 0:
        
        par  +=1
        
    else:
        
        impar += 1
        
print(f"A quantidade numeros pares é {par} = ")
print(f"A quantidade numeros impar é {impar} = ")
        
 

        
        