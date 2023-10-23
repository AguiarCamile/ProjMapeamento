document.addEventListener('DOMContentLoaded', function() {
    const estadoSelect = document.getElementById('estado');
    const microrregiaoSelect = document.getElementById('microrregiao');
    const cidadeSelect = document.getElementById('cidade');

    // Função para inicializar o Select2 em um campo de seleção
    function initSelect2(selectElement) {
        $(selectElement).select2({
            width: '100%', // Defina a largura conforme necessário
            placeholder: 'Selecione uma opção',
            allowClear: true, // Opcional: permite que o usuário desmarque a seleção
        });
    }

    // Inicialize o Select2 para cada campo de seleção
    initSelect2(estadoSelect);
    initSelect2(microrregiaoSelect);
    initSelect2(cidadeSelect);

    // Busque os dados dos estados da API e adicione-os ao campo de Estado
    fetch('https://servicodados.ibge.gov.br/api/v1/localidades/estados?orderBy=nome')
        .then(response => response.json())
        .then(data => {
            data.forEach(item => {
                const option = new Option(item.nome, item.nome, false, false);
                estadoSelect.appendChild(option);
            });

            estadoSelect.value = "{{ db.Estado }}";

            // Atualize o Select2 após adicionar as opções
            $(estadoSelect).trigger('change');
        })
        .catch(error => console.error('Erro ao buscar dados do estado:', error));

    // Busque os dados da microrregião da API e adicione-os ao campo de Microrregião
    fetch('https://servicodados.ibge.gov.br/api/v1/localidades/microrregioes?orderBy=nome')
        .then(response => response.json())
        .then(data => {
            data.forEach(item => {
                const option = new Option(item.nome, item.nome, false, false);
                microrregiaoSelect.appendChild(option);
            });

            microrregiaoSelect.value = "{{ db.Microrregiao }}";

            // Atualize o Select2 após adicionar as opções
            $(microrregiaoSelect).trigger('change');
        })
        .catch(error => console.error('Erro ao buscar dados da microrregião:', error));

    // Busque os dados da cidade da API e adicione-os ao campo de Cidade
    fetch('https://servicodados.ibge.gov.br/api/v1/localidades/municipios?orderBy=nome')
        .then(response => response.json())
        .then(data => {
            data.forEach(item => {
                const option = new Option(item.nome, item.nome, false, false);
                cidadeSelect.appendChild(option);
            });

            cidadeSelect.value = "{{ db.Cidade }}";

            // Atualize o Select2 após adicionar as opções
            $(cidadeSelect).trigger('change');
        })
        .catch(error => console.error('Erro ao buscar dados da cidade:', error));
});
