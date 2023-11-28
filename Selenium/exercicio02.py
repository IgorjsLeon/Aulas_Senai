from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Abrindo o navegador
options = webdriver.ChromeOptions()
options.add_argument('--disable-web-security')
navegador = webdriver.Chrome(options=options)

#Abrindo o site pelo navegador
navegador.get('https://www.anhanguera.com/inscricao?utm_source=google&utm_medium=cpc&utm_term=anhanguera+faculdade&utm_content=sch-l1_aedu_aon_institucional-exata_perf_inhouse_gads_texto_texto_exata_inscrever_texto_cpa&utm_campaign=google_semadserver_sch-l1_aedu_aon_institucional-exata_perf_inhouse_conversao_valor-cpa_inscrever_cpa&gad_source=1&gclid=EAIaIQobChMIuqTZhprlggMVeCqtBh1J-QboEAAYASAAEgJmN_D_BwE&gclsrc=aw.ds')
time.sleep(1)

#seleciona o campo email
try:
    elemento = navegador.find_element(By.XPATH, '//*[@id="a"]').click()
    time.sleep(3)

    #Digite no campo email
    

    #Da enter
   
finally:
    navegador.close()
