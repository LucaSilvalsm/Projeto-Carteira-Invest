document.getElementById('categoria').addEventListener('change', function() {
    var categoria = this.value;

    // Ocultar todos os setores
    document.querySelectorAll('.setorAtivo').forEach(function(element) {
        element.style.display = 'none';
    });

    // Mostrar o setor correspondente à categoria selecionada
    if (categoria === 'Acao') {
        document.getElementById('setor-acao').style.display = 'block';
    } else if (categoria === 'FIIs') {
        document.getElementById('setor-fiis').style.display = 'block';
    } else if (categoria === 'ETF') {
        document.getElementById('setor-etf').style.display = 'block';
    } else if (categoria === 'Renda Fixa') {
        document.getElementById('setor-rendafixa').style.display = 'block';
    }
});
function permitirApenasUmCheckbox(checkbox) {
    const checkboxes = document.getElementsByName(checkbox.name);
    checkboxes.forEach((item) => {
        if (item !== checkbox) item.checked = false;
    });
    console.log("Checkbox selecionado:", checkbox.value);
}
