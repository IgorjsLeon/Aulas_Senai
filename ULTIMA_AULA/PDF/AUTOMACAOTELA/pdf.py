import PyPDF2

#Abrir o arquivo PDF em modo leitura binária

with open('curso_python.pdf', 'rb') as file:
    
    #Criar um objeto PdfFileReader para ler PDF
    leitor_pdf = PyPDF2.PdfReader(file)

    #Obter o número de páginas do pdf
    numero_pagina= len(leitor_pdf.pages)
    print( f" O numero de páginas do pdf é {numero_pagina} ")


 #Obter a primeira página/ qualquer outra
    pagina = leitor_pdf.pages[0]
    #Extrair texto da página

    texto = pagina.extract_text()
    print(f"Conteúndo da página 1:\n{texto}")


