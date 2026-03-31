import os 
os.system("cls")


vetor = []


for i in range(1,6,1):
    
    numero = int(input("Digite um numero = "))
    
    if numero < 0:
        
        vetor.append(0)
        
    else:
        
        vetor.append(numero)


print(f"Os valores presentes no vetor são = {vetor}")