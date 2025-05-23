/* ===================== Remoção de Área ===================== */
function confirmRemove(id, nome) {
    document.getElementById('areaName').textContent = nome;

    const modal = new bootstrap.Modal(document.getElementById('confirmModal'));
    modal.show();

    document.getElementById('confirmRemoveButton').onclick = function () {
        window.location.replace(`/area/remover/${id}`);
    }
}


/* ===================== Remoção de Curso ===================== */
function confirmRemove(id, nome) {
    document.getElementById('courseName').textContent = nome;

    const modal = new bootstrap.Modal(document.getElementById('confirmModal'));
    modal.show();

    document.getElementById('confirmRemoveButton').onclick = function () {
        window.location.replace(`/curso/remover/${id}`);
    }
}

/* ===================== Remoção de Equipamento ===================== */
function confirmRemove(id, nome) {
    document.getElementById('equipmentName').textContent = nome;

    const modal = new bootstrap.Modal(document.getElementById('confirmModal'));
    modal.show();

    document.getElementById('confirmRemoveButton').onclick = function () {
        window.location.replace(`/equipamento/remover/${id}`);
    }
}

/* ===================== Remoção de funcionário ===================== */
function confirmRemove(id, nome) {
    document.getElementById('employeeName').textContent = nome;

    const modal = new bootstrap.Modal(document.getElementById('confirmModal'));
    modal.show();

    document.getElementById('confirmRemoveButton').onclick = function () {
        window.location.replace(`/funcionario/remover/${id}`);
    }
}

/* ===================== Remoção de Ocupação ===================== */
function confirmRemove(id, equipamento) {
    document.getElementById('equipmentName').textContent = equipamento;

    const modal = new bootstrap.Modal(document.getElementById('confirmModal'));
    modal.show();

    document.getElementById('confirmRemoveButton').onclick = function () {
        window.location.replace(`/ocupado/remover/${id}`);
    }
}

