import threading
import time
import pytest

from src import app as flask_app


@pytest.fixture(scope='module')
def server():
    # Start the Flask app on port 5002 for UI tests
    thr = threading.Thread(target=flask_app.app.run, kwargs={'port': 5002})
    thr.daemon = True
    thr.start()
    time.sleep(0.6)
    yield


def test_ui_add_remove(playwright, server):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('http://127.0.0.1:5002/')

    # Precondition: campo
    page.fill('#nome', 'Caneta')
    page.fill('#quantidade', '10')
    page.click('#btn-add')
    page.wait_for_selector('.produto')
    assert 'caneta' in page.text_content('.produto').lower()
    assert '10' in page.text_content('.produto')

    # remover parte
    page.fill('#quantidade', '5')
    page.click('#btn-remove')
    page.wait_for_timeout(200)
    assert '5' in page.text_content('.produto')

    browser.close()
