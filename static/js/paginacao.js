var table = document.getElementById('myTable');
var rows = table.rows;
var itemsPerPage = 5; // Defina o número de itens por página
var currentPage = 0;

function showPage(pageNum) {
    for (var j = 0; j < rows.length; j++) {
        if (j >= pageNum * itemsPerPage && j < (pageNum + 1) * itemsPerPage) {
            rows[j].style.display = 'table-row';
        } else {
            rows[j].style.display = 'none';
        }
    }
    currentPage = pageNum;

                // Habilitar ou desabilitar os botões "Anterior" e "Próximo"
    document.querySelector('.prev').disabled = currentPage === 0;
    document.querySelector('.next').disabled = (currentPage + 1) * itemsPerPage >= rows.length;
}

var pageCount = Math.ceil(rows.length / itemsPerPage);

            // Adicione os eventos aos botões de navegação
document.querySelector('.prev').addEventListener('click', function () {
    if (currentPage > 0) {
        showPage(currentPage - 1);
    }
});

document.querySelector('.next').addEventListener('click', function () {
    if ((currentPage + 1) * itemsPerPage < rows.length) {
        showPage(currentPage + 1);
    }
});

            // Mostrar a primeira página inicialmente
showPage(0);