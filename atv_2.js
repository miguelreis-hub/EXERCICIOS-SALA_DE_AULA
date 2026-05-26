vetor_numeros = [1,2,3,4,5,6]

console.log(vetor_numeros)

console.log("Multiplicando cada elemento do vetor por 2:")

const dobrados = vetor_numeros.map(n => n * 2) //map mapear cada element do vetor (n => n*2) isso diz que para cada n multiplique por 2 e o resultado coloque em uma nova variavel
console.log(dobrados)


vetor_numeros.push(1)

const impares = vetor_numeros.filter(n => n % 2 == 1) // filtrar o vetor a cada n presente no vetor, filtre numeros que dividindo por 2 tem resto igual a 1 = sendo impar
console.log(impares)

const pares = vetor_numeros.filter(n => n % 2 == 0) // filtrar o vetor a cada n presente no vetor resto da divisao por dois igual á 0 é par 
console.log(pares)

const negativos = vetor_numeros.filter(n => n < 0) // filtrar o vetor a cada n presente no vetor, filtre numeros menores que 0 e coloque num novo vetor

console.log(negativos)


const soma = vetor_numeros.reduce((soma,atual) => soma + atual,0) // reduce reduz o vetor a um unico valor, nesse caso a soma de todos os elementos do vetor, o 0 é o valor inicial da soma


console.log(soma)