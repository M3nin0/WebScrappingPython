import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.empregasaojosecampos.com")
soup = BeautifulSoup(page.content, 'html.parser')

[print (item.getText()) for item in list(soup.findAll("span", {"itemprop": "title"}))] #Ultimas vagas de empregos
nomeDaVaga = soup.find("span", {"itemprop": "title"})
enunciados = soup.find("div", {"class": "content-area col-sm-12 col-md-8"})


nomeDaVaga = xxx[xx:xxx.index('–')]


enunciados = soup.findAll("div", class_="blog-post") #procura os post das vagas
enunciados[0]  # primeira vaga
enunciados[1]  # segunda vaga


>>> type (soup)
<class 'bs4.BeautifulSoup'>

>>> type(enunciados)                #Contem uma lista de elementos de resultante de um findAll, ou seja, eh apenas uma lista, seus atributos sao de lista
<class 'bs4.element.ResultSet'>

>>> type(enunciados[0])             #o item desta lista é um 'bs4.element.Tag' nele tem as opcoes de getText, findAll etc...
<class 'bs4.element.Tag'>           #seus atributos sao de 'bs4.element.Tag'

vaga = enunciados[0]

'''CONTEUDO: vaga.find("span", class_="blog-post-title")
<a
  href="https://www.empregasaojosecampos.com/2018/02/operador-de-pa-carregadeira-e-empilhadeira-sao-jose-dos-campos-sp.html"
  rel="bookmark"
  title="Permanent Link to Operador De Pá Carregadeira E Empilhadeira – São José Dos Campos – Sp"
>
  <span itemprop="title">
    Operador De Pá Carregadeira E Empilhadeira – São José Dos Campos – Sp
  </span>
</a>
'''

headerVaga = vaga.find("span", class_="blog-post-title") #Filtra apenas os dados respectivos ao titulo da vaga
nomeDaVaga = headerVaga.getText() #Pega o texto exibido na pagina
linkDaVaga = headerVaga.find("a").get("href") #entra na tag <a ... > acessa o elemento 'href' e retorna o valor atribuido a ela


'''''''''''''

dados = vaga.find("div", class_="metadata")
diaDaVaga = dados.find("time", class_="value-title").getText()

caracteristicas = dados.findAll("span")
cidade = caracteristicas[2]
estado = caracteristicas[3]
pais = caracteristicas[4]
salario = caracteristicas[5]
nivelAcademico = caracteristicas[7]
statusVaga = caracteristicas[8]
tempoContrato = caracteristicas[9]


import requests
import json
from bs4 import BeautifulSoup

def empregaSaoJose_api():
    URL_ULTIMOS_RESULTADOS = "http://www1.caixa.gov.br/loterias/loterias/megasena/megasena_pesquisa_new.asp"
    page = requests.get(URL_ULTIMOS_RESULTADOS)
    bs = BeautifulSoup(page.content, "html.parser")
    numeros_sena = [ n.contents[0] for n in bs.findAll('li')[:6]]
    results = page.content.split('|')

    return {'cidade': results[2], 'estado': results[3], 'pais': results[4],
         'salario': results[5], 'nivelAcademico': results[7], 'statusVaga': results[8]}

print ( json.dumps(megasena_api()) )
