function preencherSeletorCidades(cidades) {
    const selectElement = document.getElementById("cidade-select");

    cidades.forEach(cidade => {
        const option = document.createElement("option");
        option.value = cidade.id;
        option.textContent = cidade.nome;
        selectElement.appendChild(option);
    });
}

fetch("https://servicodados.ibge.gov.br/api/v1/localidades/municipios")
    .then(response => response.json())
    .then(cidades => {
        preencherSeletorCidades(cidades);
    })
    .catch(error => {
        console.error("Erro ao obter cidades:", error);
    });
