import json
import datetime
import requests

import utils as tools
from time import sleep

from bs4 import BeautifulSoup


class ScrapEmpregaSjc():
    '''
        Classe para realizar scrap do site Emprega São José
    '''

    def __init__(self):
    
        self.urlBase = "https://www.empregasaojosecampos.com"


    def make_soup(self, url): #funcao para instanciar objetos "soup", para o reaproveitamento de codigo
        '''

        '''

        page = requests.get(url)
        return BeautifulSoup(page.content, 'html.parser')


    def empregos_api(self, url):  #
        '''
            :Core do programa: este método é responsavel por navegar no codigo fonte do html e 
                                filtrar os dados condizentes com o ideal do programa
        '''

        soup = make_soup(url)
        lista_vagas = soup.findAll("div", class_ = "blog-post")
        k = 0
        
        while(k <= len(lista_vagas[:-1]) ) :
            headerVaga = lista_vagas[k].find("span", class_ = "blog-post-title") #Filtra apenas os dados respectivos ao titulo da vaga
            dadosVaga = lista_vagas[k].find("div", class_ = "metadata")
            caracteristicas = dadosVaga.findAll("span")
            nomeVaga = headerVaga.getText()[1:-1]
            data = dadosVaga.find("time", class_ = "value-title").getText()[-10:]

            print ( {
                    'nomeVaga': nomeVaga,
                    'local': caracteristicas[2].getText() + ', ' + caracteristicas[3].getText() + ' - ' + caracteristicas[4].getText(),
                    'data': data,
                    'diffData': tools.calcular_data(data),
                    'linkVaga': headerVaga.find("a").get("href"),
                    'salario': caracteristicas[5].getText(),
                    'nivelAcademico': caracteristicas[7].getText(),
                    'statusVaga': caracteristicas[8].getText()
                }  )

            print("\n\n")
            k += 1
            sleep(2)


    def pes_ultimas_vagas():
        '''

        '''

        k = 1
        
        while (k <= 3):
            pageNumber = str(k)
            if pageNumber == '1':
                empregos_api(self.urlBase)
                k+=1
            else:
                empregos_api(self.urlBase + "/page/" + pageNumber)
                k+=1


    def pes_vaga_nome(vaga):
        '''

        '''

        k = 1

        while (k <= 2):
            pageNumber = str(k)
            if pageNumber == '1':
                empregos_api(self.urlBase + "/?s=" + vaga)
                k += 1
            else:
                empregos_api(self.urlBase + "/page/" + pageNumber + "?s=" + vaga)
                k+=1


if __name__ == '__main__':
    categorias = ['Ajudante','Analista','Assistente','Atendente','Auxiliar','Balconista','Caixa','Comercial','Coordenador','Copeira','Cozinheiro','Departamento Pessoal','Empilhadeira','Eletricista','Encarregado','Enfermagem','Estoquista','Farmacêutico','Jovem Aprendiz','Mecânico','Manutenção','Motorista','Nutricionista','Produção','Operador','Pedreiro','Secretária','Promotor','Recepcionista','RHServiços Gerais','Telemarketing','Técnico','Vendedor']
    