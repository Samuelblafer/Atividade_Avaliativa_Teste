async function atualizarLista() {
  const lista = document.getElementById('produtos');
  lista.innerHTML = '';
  // aqui poderíamos manter uma lista no servidor; pra simplicidade, pedimos nomes conhecidos
}

async function fetchQuantidade(nome) {
  const r = await fetch(`/produto/${encodeURIComponent(nome)}`);
  const j = await r.json();
  return j.quantidade;
}

document.getElementById('btn-add').addEventListener('click', async () => {
  const nome = document.getElementById('nome').value.trim();
  const quantidade = parseInt(document.getElementById('quantidade').value, 10);
  const status = document.getElementById('mensagem');
  const r = await fetch('/produto', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ nome, quantidade })
  });
  const j = await r.json();
  if (r.ok) {
    status.style.color = 'green';
    status.textContent = j.message;
  } else {
    status.style.color = 'red';
    status.textContent = j.error || 'Erro';
  }
  // mostrar quantidade atual
  const qtd = await fetchQuantidade(nome);
  const produtos = document.getElementById('produtos');
  produtos.innerHTML = `<div class="produto">${nome.toLowerCase()} — ${qtd}</div>`;
});

document.getElementById('btn-remove').addEventListener('click', async () => {
  const nome = document.getElementById('nome').value.trim();
  const quantidade = parseInt(document.getElementById('quantidade').value, 10);
  const status = document.getElementById('mensagem');
  const r = await fetch('/produto', {
    method: 'DELETE',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ nome, quantidade })
  });
  const j = await r.json();
  if (r.ok) {
    status.style.color = 'green';
    status.textContent = j.message;
  } else {
    status.style.color = 'red';
    status.textContent = j.error || 'Erro';
  }
  const qtd = await fetchQuantidade(nome);
  const produtos = document.getElementById('produtos');
  produtos.innerHTML = `<div class="produto">${nome.toLowerCase()} — ${qtd}</div>`;
});
