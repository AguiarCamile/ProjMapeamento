document.addEventListener('DOMContentLoaded', function() {
    const estadoSelect = document.getElementById('estado');
    const microrregiaoSelect = document.getElementById('microrregiao');
    const cidadeSelect = document.getElementById('cidade');


    fetch('https://servicodados.ibge.gov.br/api/v1/localidades/estados?orderBy=nome')
        .then(response => response.json())
        .then(data => {
            data.forEach(item => {
                const option = document.createElement('option');
                option.value = item.nome;
                option.textContent = item.nome;
                estadoSelect.appendChild(option);
            });

            estadoSelect.value = "{{ db.Estado }}";
        })
        .catch(error => console.error('Erro ao buscar dados do estado:', error));


    fetch('https://servicodados.ibge.gov.br/api/v1/localidades/microrregioes?orderBy=nome')
        .then(response => response.json())
        .then(data => {
            data.forEach(item => {
                const option = document.createElement('option');
                option.value = item.nome;
                option.textContent = item.nome;
                microrregiaoSelect.appendChild(option);
            });

            microrregiaoSelect.value = "{{ db.Microrregiao }}";
        })
        .catch(error => console.error('Erro ao buscar dados da microrregiao:', error));


    fetch('https://servicodados.ibge.gov.br/api/v1/localidades/municipios?orderBy=nome')
        .then(response => response.json())
        .then(data => {
            data.forEach(item => {
                const option = document.createElement('option');
                option.value = item.nome;
                option.textContent = item.nome;
                cidadeSelect.appendChild(option);
            });

            cidadeSelect.value = "{{ db.Cidade }}";
        })
        .catch(error => console.error('Erro ao buscar dados da cidade:', error));
});


