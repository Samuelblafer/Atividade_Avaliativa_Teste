import threading
import time
import pytest

from src import app as flask_app

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='module')
def server():
    thr = threading.Thread(target=flask_app.app.run, kwargs={'port': 5003})
    thr.daemon = True
    thr.start()
    time.sleep(0.6)
    yield


@pytest.fixture(scope='module')
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    try:
        driver.quit()
    except Exception:
        pass


def test_ui_add_and_remove(server, driver):
    url = 'http://127.0.0.1:5003/'
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    nome = wait.until(EC.presence_of_element_located((By.ID, 'nome')))
    quantidade = driver.find_element(By.ID, 'quantidade')
    btn_add = driver.find_element(By.ID, 'btn-add')
    btn_remove = driver.find_element(By.ID, 'btn-remove')

    nome.clear()
    nome.send_keys('Caneta')
    quantidade.clear()
    quantidade.send_keys('10')
    btn_add.click()

    produto = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.produto')))
    text = produto.text.lower()
    assert 'caneta' in text
    assert '10' in text

    quantidade.clear()
    quantidade.send_keys('5')
    btn_remove.click()
    time.sleep(0.2)
    produto = driver.find_element(By.CSS_SELECTOR, '.produto')
    assert '5' in produto.text
