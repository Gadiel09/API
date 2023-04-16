import requests
import json
from dash import html
from dash import dcc
import dash

global db
db = [ ]

api = "https://rickandmortyapi.com/api/character"
escolha = "results"
chave = "episode"


def tratar_API(api, escolha,idenficador):
	link = requests.get(api)
	trat = link.json()
	col = trat[escolha]
	for item in col:
	  db.append(item)
	  
	  
	coluns = [ ]
	for y in db:
	  coluns.append(y)
	  
	  
	data = {}
	for h in coluns[idenficador]:
	  data["status"] = coluns[idenficador]['status']
	  data["gender"] = coluns[idenficador]['gender']
	  data["Name"] = coluns[idenficador]['name']
	  data["species"] = coluns[idenficador]['species']
	  data["planet"] = coluns[idenficador]['origin']["name"]
	  #data["location"] = coluns[idenficador]['location']["name"]
	  
	  
	return html.H3(["STATUS"], id = "h3"), html.Ul([
	  html.Li([
          "Status : "f'{data["status"]}'
        ]),
	  html.Li([
         "Sex : " f'{data["gender"]}'
        ]),
	  html.Li([
          "Name : " f'{data["Name"]}'
        ]),
	  html.Li([
          "Specie :" f'{data["species"]}'
        ]),
	  html.Li([
          "Planet : " f'{data["planet"]}'
        ]),
      ], className = "lista"),
	
	
	
	
	
	
def extract_len_ep(api, cont):
  link = requests.get(api)
  trat = link.json()
  col = trat[escolha]
  for item in col:
    db.append(item)
    
    
  coluns = [ ]
  for y in db:
    coluns.append(y)
    
  
  qtd_ep = 0
  for y in range(len(coluns[cont][chave])):
    qtd_ep += 1
  ep = qtd_ep

  return html.H1(" Episodes"),html.P(f"Quantidade : {ep}")
  



  

	
  

