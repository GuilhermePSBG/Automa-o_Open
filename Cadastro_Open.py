from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import time


def login(navegador, email, senha):
    navegador.get("https://app.openferramentaria.com.br/Home")
    
    WebDriverWait(navegador,10).until(
        EC.visibility_of_element_located((By.ID, "Email"))
    )

    for letra in email:
        navegador.find_element(By.ID, "Email").send_keys(letra)
        time.sleep(0.03)

    WebDriverWait(navegador,10).until(
        EC.visibility_of_element_located((By.ID, "pass"))
    )

    for letra in senha:
        navegador.find_element(By.ID, "pass").send_keys(letra)
        time.sleep(0.03)

    WebDriverWait(navegador,10).until(
        EC.element_to_be_clickable((By.XPATH,'//button[text()[contains(.,"Entrar")]]'))
    )
    navegador.find_element(By.XPATH, '//button[text()[contains(.,"Entrar")]]').click()
  
def cadastrar_itens(navegador, dados, pasta):

    WebDriverWait(navegador,10).until(
        EC.element_to_be_clickable((By.XPATH,'//a[@data-id="89"]'))
    )
    navegador.find_element(By.XPATH, '//a[@data-id="89"]').click()

    WebDriverWait(navegador,10).until(
        EC.element_to_be_clickable((By.XPATH,'//a[.//span[text()="Cadastro"]]'))
    )
    navegador.find_element(By.XPATH, '//a[.//span[text()="Cadastro"]]').click()
    navegador.find_element(By.XPATH, '//a[span[text()="Ferramentas"]]').click()
    

    for index, row in dados.iterrows():
        try:
            WebDriverWait(navegador,10).until(
                EC.element_to_be_clickable((By.XPATH,'//button[text()="Novo [+]"]'))
            )
            navegador.find_element(By.XPATH, '//button[text()="Novo [+]"]').click()
            
            WebDriverWait(navegador,10).until(
                EC.visibility_of_element_located((By.ID, "CodInterno"))
            )
            
            codigos = row["Código Interno"]
            DesS = row["Descrição Simples"]
            DesC = row["Descrição Completa"]
            categoria = row["Catégoria"]
            unidade = row["Unidade"]
 
            
            navegador.find_element(By.ID, "CodInterno").send_keys(codigos)
                
            navegador.find_element(By.ID, "Descricao").send_keys(DesS)
                                
            navegador.find_element(By.ID, "DescricaoCompleta").send_keys(DesC)

           
            navegador.find_element(By.ID, "select-categorias").send_keys(categoria, Keys.ENTER)
            navegador.find_element(By.ID, "Unidade").send_keys(unidade, Keys.ENTER)

            navegador.find_element(By.XPATH, '//input[@value="Cadastrar ferramenta"]').click()
            
            WebDriverWait(navegador,10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']"))
            ).click()

            WebDriverWait(navegador,10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Voltar"))
            )

            navegador.find_element(By.LINK_TEXT, "Voltar").click()
            print(f"Codigo existente: {codigos}, pulando....")

            caminho_completo = os.path.join(pasta, "codigo_repetidos.txt")
            with open(caminho_completo, "a") as f:
                f.write(f"{codigos}\n")
            with open(caminho_completo, "r") as f:
                print(f.read())

            continue

        except Exception as erro:
            print(f"Codigo cadastra com sucesso: {codigos} → {type(erro).__name__}: {erro}")

            caminho_completo = os.path.join(pasta, "codigo_novos.txt")
            with open(caminho_completo, "a") as f:
                f.write(f"{codigos}\n")

if __name__ == "__main__":
    dados = pd.read_excel(r"C:\Users\Hydrostec\OneDrive\Documentos\Estudo (G)\Automação básica com Python (sem framework ainda)\test.xlsx")

    pasta = r"coloque o local da pasta"

    dados.columns = dados.columns.str.strip()
   
    navegador = webdriver.Chrome()
    navegador.maximize_window()
    

    email = "xxx"
    senha = "xxx"

    login(navegador, email, senha)
    cadastrar_itens(navegador, dados, pasta)

    time.sleep(2)
