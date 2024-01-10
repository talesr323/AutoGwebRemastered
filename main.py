import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from playwright.sync_api import Playwright, sync_playwright, expect

#isPDV  0 = Somente NF-e  //  1 = Somente NFC-e   //   2 = NF-e e NFC-e 


def handledata(datas):
    pdv_0 = [data for data in datas if int(data['isPDV']) == 0]
    pdv_1 = [data for data in datas if int(data['isPDV']) == 1]
    pdv_2 = [data for data in datas if int(data['isPDV']) == 2]
    return pdv_0, pdv_1, pdv_2

def handle_confirm_button(page):
    confirm_button = page.get_by_role("button", name="Confirmar")
    if not confirm_button.is_enabled():
        page.press("body", "Escape")
        return False
    retry = True
    while retry:
        try:
            confirm_button.click()
            page.get_by_role("button", name="Ok").press("Enter")
            return True
        except:
            
            return False
          
def handle_client_enable(page, nome):
    confirm_button = page.get_by_text(nome)
    if confirm_button:
        try:
            confirm_button.click()
            return True
        except:
            pass
    return False

def handle_month(page):
    confirm_button = page.get_by_role("option", name="Outubro/2023").click()
    if confirm_button:
        try:
            confirm_button.click()
            return True
        except:
            pass 
    return False



dados_json = '''
{
  "dados": [
      {
      "nome": "ANA ALVES DOS SANTOS ARAUJO",
      "email": "equilibriocontab.diretoria@gmail.com",
      "nome_email": "Café Baguaçú",
      "isPDV": "0"
    },
    {
      "nome": "JOAQUIM JUNIOR GONCALVES 22950223800",
      "email": "fiscal@dataconcontabil.com.br",
      "nome_email": "Joaquim Ferro e Máquinas",
      "isPDV": "0"
    },
    {
      "nome": "MAICON DA SILVA CAMPOS - ME",
      "email": "alexandre@rjassessoria.com.br",
      "nome_email": "CHURROS DA PRACA",
      "isPDV": "2"
    },
    {
      "nome": "ALDERICO PARDINI MERCEARIA",
      "email": "escritafiscal@martinezcontabil.com.br",
      "nome_email": "Mercearia São Pedro",
      "isPDV": "2"
    },
    {
      "nome": "MANUEL FLUGÊNCIO",
      "email": "fiscal@dataconcontabil.com.br",
      "nome_email": "Manuel Flugêncio",
      "isPDV": "0"
    },
    {
      "nome": "LARISSA GATTI BARBOZA DE SOUZA LTDA",
      "email": "fiscalgonsales@gmail.com",
      "nome_email": "Mercado Bandeira",
      "isPDV": "1"
    },
    {
      "nome": "J C DE O MARQUES EIRELI",
      "email": "fiscal@onixcontabeis.com.br",
      "nome_email": "J C DE O MARQUES EIRELI",
      "isPDV": "0"
    },
    {
      "nome": "RB DIST E REPRES DE PRODUTOS",
      "email": "fiscal@onixcontabeis.com.br",
      "nome_email": "RB INSUMOS HOSPITALARES",
      "isPDV": "0"
    },
    {
      "nome": "LUCAS RODRIGUES DOS SANTOS",
      "email": "suporte6.excelent@gmail.com",
      "nome_email": "MEGA REDES ESPORTIVAS",
      "isPDV": "0"
    },
    {
      "nome": "C & V INJETADOS LTDA",
      "email": "suporte6.excelent@gmail.com",
      "nome_email": "C & V INJETADOS",
      "isPDV": "0"
    },
    {
      "nome": "CAMILA CARLA DE ANDRADE LOPES",
      "email": "carlos@excritorioipiranga.com.br",
      "nome_email": "ZANINI DISTRIBUIDORA DE CONGELADOS",
      "isPDV": "0"
    },
    {
      "nome": "MARIA ANTONIETA DA FONSECA ALVES",
      "email": "escritafiscal@martinezcontabil.com.br",
      "nome_email": "BAZAR PROGRESSO",
      "isPDV": "2"
    },
    {
      "nome": "MAURILIO DE ARIMATEIA",
      "email": "suporte6.excelent@gmail.com",
      "nome_email": "CERVEJARIA 9 DE JULHO",
      "isPDV": "1"
    },
    {
      "nome": "VILSON PEREIRA MINIMERCADO",
      "email": "fiscal@onixcontabeis.com.br",
      "nome_email": "VILSON PEREIRA MINIMERCADO",
      "isPDV": "1"
    },
    {
      "nome": "A J COMERCIO DE AGUA E GAS LTDA",
      "email": "datacon@terra.com.br",
      "nome_email": "MINERAL",
      "isPDV": "1"
    },
    {
      "nome": "DISTRIBUIDORA DE LUBRIFICANTES MARIN LTDA",
      "email": "fiscal.gadecontabil@gmail.com",
      "nome_email": "DISTRIBUIDORA DE LUBRIFICANTES MARIN LTDA",
      "isPDV": "0"
    },
    {
      "nome": "CARLA AFFONSO DIAS OPTICA",
      "email": "fiscal@escritoriomarcotec.com.br",
      "nome_email": "OTICA ELIS",
      "isPDV": "0"
    },
    {
      "nome": "REGINALDO DIAS OPTICA",
      "email": "fiscal@escritoriomarcotec.com.br",
      "nome_email": "A ESPECIALISTA",
      "isPDV": "0"
    },
    {
      "nome": "LARISSA DE BRITO BUZATO LTDA",
      "email": "fiscal@onixcontabeis.com.br",
      "nome_email": "SOFI SHOES",
      "isPDV": "0"
    },
    {
      "nome": "SCARDOVELLI & GOMES ACOUGUE E MERCEARIA LTDA",
      "email": "fiscal.escritoriocoroados@gmail.com",
      "nome_email": "ACOUGUE GUARANI",
      "isPDV": "1"
    },
    {
      "nome": "R. R. M. DE SOUZA PALMILHAS - ME",
      "email": "suporte6.excelent@gmail.com",
      "nome_email": "BRAGHIN PALMILHAS",
      "isPDV": "0"
    },
    {
      "nome": "ALISON LUIZ ZANONATO 26863670836",
      "email": "suporte6.excelent@gmail.com",
      "nome_email": "ZANONATU USINAGEM",
      "isPDV": "0"
    }
  ]
}
'''
dados = json.loads(dados_json)
driver = webdriver.Chrome()

def run(playwright: Playwright, nome: str, email: str, nome_email: str) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.gdoorweb.com.br/login")
    page.get_by_label("E-mail *").click()
    page.get_by_label("E-mail *").fill("suporte3.excelent@gmail.com")
    page.get_by_label("E-mail *").press("Enter")
    page.get_by_label("Senha *").fill("parceria94@")
    page.get_by_label("Senha *").press("Enter")
    pdv_0_list, pdv_1_list, pdv_2_list = handledata(dados['dados'])
    if any(data['nome'] == nome for data in pdv_0_list):
        if handle_client_enable(page, nome):
            page.get_by_role("button", name="Movimentações").click()
            page.get_by_role("link", name="NF-e").click()
            page.get_by_role("heading", name="XML do mês").click()
            page.get_by_label("Escolha o mês").locator("div").nth(2).click()
            time.sleep(2)
            handle_month(page)
            time.sleep(2)
            page.get_by_text("Enviar por e-mail").click()
            page.get_by_label("E-mail *").click()
            page.get_by_label("E-mail *").fill(email)
            page.get_by_label("E-mail *").press("Tab")
            page.get_by_label("Nome").fill(nome_email)
            handle_confirm_button(page)
    elif any(data['nome'] == nome for data in pdv_1_list):
        if handle_client_enable(page, nome):
            page.get_by_role("button", name="Movimentações").click()
            page.get_by_role("link", name="PDV").click()
            page.get_by_role("heading", name="XML do mês").click()
            page.get_by_label("Escolha o mês").locator("div").nth(2).click()
            time.sleep(2)
            handle_month(page)
            time.sleep(2)
            page.get_by_text("Enviar por e-mail").click()
            page.get_by_label("E-mail *").click()
            page.get_by_label("E-mail *").fill(email)
            page.get_by_label("E-mail *").press("Tab")
            page.get_by_label("Nome").fill(nome_email)
            handle_confirm_button(page)
    else:
        if handle_client_enable(page, nome):
            page.get_by_role("button", name="Movimentações").click()
            page.get_by_role("link", name="NF-e").click()
            page.get_by_role("heading", name="XML do mês").click()
            page.get_by_label("Escolha o mês").locator("div").nth(2).click()
            time.sleep(2)
            handle_month(page)
            time.sleep(2)
            page.get_by_text("Enviar por e-mail").click()
            page.get_by_label("E-mail *").click()
            page.get_by_label("E-mail *").fill(email)
            page.get_by_label("Nome").click()
            page.get_by_label("Nome").fill(nome_email)
            handle_confirm_button(page)
            page.get_by_role("link", name="PDV").click()
            page.get_by_role("heading", name="XML do mês").click()
            time.sleep(2)
            handle_month(page)
            time.sleep(2)
            page.get_by_text("Enviar por e-mail").click()
            page.get_by_label("Nome").click()
            page.get_by_label("Nome").fill(nome_email)
            page.get_by_label("E-mail *").click()
            page.get_by_label("E-mail *").fill(email)
            handle_confirm_button(page)

    context.close()
    browser.close()

with sync_playwright() as playwright:
    pessoa_index = 0  # Inicializa o índice da pessoa

    while pessoa_index < len(dados['dados']):  # Loop enquanto houver pessoas a serem processadas
        pessoa = dados['dados'][pessoa_index]
        nome_pessoa = pessoa['nome']
        email = pessoa['email']
        nome_email = pessoa['nome_email']

        try:
            run(playwright, nome_pessoa, email, nome_email)
        except Exception as e:
            print(f"Ocorreu uma exceção: {e}")

        pessoa_index += 1
