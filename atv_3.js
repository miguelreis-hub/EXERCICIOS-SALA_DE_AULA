notas = [10,10,10]


const soma = notas.reduce((soma,atual) => soma + atual, 0)


const media_final = soma / notas.length

console.log(media_final)