function gerarTabuada(){

    const numeroInput = document.getElementById(`numeroinput`)

    let numero = parseInt(numeroInput.value)

    const resultadoDiv = document.getElementById(`ResultadoTabuada`)

    resultadoDiv.innerHTML = ""

    resultadoDiv.innerHTML += `<h2>Tabuada do numero ${numero}:</h2>`

    for (let i = 1; i <= 10; i++) {

        let resultado = numero * i

        resultadoDiv.innerHTML += `<p> ${numero} x ${i} = ${resultado} </p>`
    }

}

const btGerar = document.getElementById("btGerar")
btGerar.addEventListener("click", gerarTabuada)