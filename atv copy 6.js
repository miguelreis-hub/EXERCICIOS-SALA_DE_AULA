let pares = 0
let impares = 0


vetor_numeros = [4,12,23,31,47,58]


for (let i = 0;  i<vetor_numeros.length; i++){

    if(vetor_numeros[i] % 2 == 0)
        pares +=1
    else
        impares+=1
    
}


console.log(`A quantidade de numeros de pares é  = ${pares}`)
console.log("")
console.log(`A quantidade de numeros impares é = ${impares}`)