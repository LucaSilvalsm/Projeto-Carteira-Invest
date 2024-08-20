

function permitirApenasUmCheckbox(checkbox) {
    const checkboxes = document.getElementsByName(checkbox.name);
    checkboxes.forEach((cb) => {
        if (cb !== checkbox) {
            cb.checked = false;
        }
    });
}

const form = document.getElementById('form-hamburguer');
form.addEventListener('submit', function() {
    const checkboxes = document.getElementsByName('setor');
    let selected = false;
    checkboxes.forEach((checkbox) => {
        if (checkbox.checked) {
            selected = true;
        }
    });
    if (!selected) {
        alert('Selecione um setor para o ativo.');
        event.preventDefault();
    }
});
