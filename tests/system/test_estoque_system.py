import threading
import time
import requests
import pytest

from src import app as flask_app


@pytest.fixture(scope='module', autouse=True)
def run_server():
    # Start Flask app in a thread for testing
    server = threading.Thread(target=flask_app.app.run, kwargs={'port': 5001})
    server.daemon = True
    server.start()
    time.sleep(0.5)  # small delay to ensure server starts
    yield
    # Flask dev server will stop when process ends


BASE = 'http://127.0.0.1:5001'


def test_adicionar_e_verificar():
    # verificar inicialmente zero
    r = requests.get(f'{BASE}/produto/Caneta')
    assert r.status_code == 200
    assert r.json()['quantidade'] == 0

    # adicionar
    r = requests.post(f'{BASE}/produto', json={'nome': 'Caneta', 'quantidade': 10})
    assert r.status_code == 201

    r = requests.get(f'{BASE}/produto/caneta')
    assert r.status_code == 200
    assert r.json()['quantidade'] == 10


def test_remover_e_erro():
    # remover parcialmente
    r = requests.delete(f'{BASE}/produto', json={'nome': 'Caneta', 'quantidade': 5})
    assert r.status_code == 200

    r = requests.get(f'{BASE}/produto/caneta')
    assert r.json()['quantidade'] == 5

    # tentar remover produto inexistente
    r2 = requests.delete(f'{BASE}/produto', json={'nome': 'Lapis', 'quantidade': 1})
    assert r2.status_code == 400
    assert 'não está cadastrado' in r2.json().get('error', '')


def test_quantidade_invalida():
    # adicionar com quantidade inválida
    r = requests.post(f'{BASE}/produto', json={'nome': 'Borracha', 'quantidade': 0})
    assert r.status_code == 400
    assert 'A quantidade deve ser' in r.json().get('error', '')
