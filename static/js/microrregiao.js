function preencherSeletorMicrorregioes(microrregioes) {
    const selectElement = document.getElementById("microrregiao-select");

    microrregioes.forEach(microrregiao => {
        const option = document.createElement("option");
        option.value = microrregiao.id;
        option.textContent = microrregiao.nome;
        selectElement.appendChild(option);
    });
}

fetch("https://servicodados.ibge.gov.br/api/v1/localidades/microrregioes")
    .then(response => response.json())
    .then(microrregioes => {
        preencherSeletorMicrorregioes(microrregioes);
    })
    .catch(error => {
        console.error("Erro ao obter microrregiao:", error);
    });
