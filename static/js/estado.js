function preencherSeletorEstados(estados) {
    const selectElement = document.getElementById("estado-select");

    estados.forEach(estado => {
        const option = document.createElement("option");
        option.value = estado.sigla;
        option.textContent = estado.nome;
        selectElement.appendChild(option);
    });
}

fetch("https://servicodados.ibge.gov.br/api/v1/localidades/estados")
    .then(response => response.json())
    .then(estados => {
        preencherSeletorEstados(estados);
    })
    .catch(error => {
        console.error("Erro ao obter estados:", error);
    });

const microrregiaoSelect = document.getElementById("microrregiao-select");
const cidadeSelect = document.getElementById("cidade-select");


