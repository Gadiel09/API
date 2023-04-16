from rick__api import tratar_API, extract_len_ep
import plotly.graph_objects as go
from dash import html
from dash import dcc
from dash import Input
from dash import Output
from dash import ctx
import dash
import requests
import json


global db, colunas, esc
db = [ ]
colunas = [ ]
esc = 0

def buscar_imagem(escopo, num):
	  return escopo.get_asset_url(f'{num}.jpg')

def br():
	return html.Br()

def hr():
  return html.Hr(id = "line")

api = "https://rickandmortyapi.com/api/character"
escolha = "results"
chave = "episode"



app = dash.Dash(__name__)

app.layout = html.Div([
	
	html.Div([
		html.H1("Interactive Morty"),br()], 
		className = "title"),
	br(),
	br(),
	html.Div([
	  
	  
      	html.Div(
      	  html.H1("?"),
      		id = "img", className = "col01"
      		),
      	  
      	html.Div(
      	  html.H1("?"),
      	 id = "dados", className = "col02"
      	 ),
      	 
      	 html.Div(
      	    id= "eps"
      	   ),
      	  
      	  
	  ], className = "coluns"),
	  #
	  #
	  #
	  #
	  #
	  #
	  #
	  #callbacks
	  br(),br(),
	  br(),br(),
	  br(),br(),
	    html.Div([
  	    html.Div([
  	        html.H1("R"),
  	          html.Img(src = buscar_imagem(app, 0), className = "circle_img"),
  	          html.Button("Show Me", id = "btn_click_0", n_clicks = 0),
  	      ], className = "item_call_0 row"),
  	    html.Div([
  	        html.H1("M"),
  	        html.Img(src = buscar_imagem(app, 1), className = "circle_img"),
  	        html.Button("Show Me", id = "btn_click_1", n_clicks = 0),
  	        ], className = "item_call_1 row" ),
  	    html.Div([
  	        html.H1("S"),
  	        html.Img(src = buscar_imagem(app, 2), className = "circle_img"),
  	        html.Button("Show Me", id = "btn_click_2", n_clicks = 0),
  	      ], className = "item_call_2 row"),
  	    html.Div([
  	        html.H1("B"),
  	        html.Img(src = buscar_imagem(app, 3), className = "circle_img"),
  	        html.Button("Show Me", id = "btn_click_3", n_clicks = 0),
  	        ], className = "item_call_3 row" ),
  	        
  	    html.Div([
  	        html.H1("J"),
  	        html.Img(src = buscar_imagem(app, 4), className = "circle_img"),
  	        html.Button("Show Me", id = "btn_click_4", n_clicks = 0),
  	      ], className = "item_call_4 row"),
  	    html.Div([
  	        html.H1("ABP"),
  	        html.Img(src = buscar_imagem(app, 5), className = "circle_img"),
  	        html.Button("Show Me", id = "btn_click_5", n_clicks = 0),
  	        ], className = "item_call_5 row" ),
  	    html.Div([
  	        html.H1("ABL"),
  	        html.Img(src = buscar_imagem(app, 6), className = "circle_img"),
  	        html.Button("Show Me", id = "btn_click_6", n_clicks = 0),
  	      ], className = "item_call_6 row"),
  	    html.Div([
  	        html.H1("ADR"),
  	        html.Img(src = buscar_imagem(app, 7), className = "circle_img"),
  	        html.Button("Show Me", id = "btn_click_7", n_clicks = 0),
  	        ], className = "item_call_7 row" ),
  	        
  	    html.Div([
  	        html.H1("AGD"),
  	        html.Img(src = buscar_imagem(app, 8), className = "circle_img"),
  	        html.Button("Show Me", id = "btn_click_8", n_clicks = 0),
  	      ], className = "item_call_8 row"),
  	    html.Div([
  	        html.H1("AR"),
  	        html.Img(src = buscar_imagem(app, 9), className = "circle_img"),
  	        html.Button("Show Me", id = "btn_click_9", n_clicks = 0),
  	        ], className = "item_call_9 row" ),
  	    html.Div([
  	        html.H1("AB"),
  	        html.Img(src = buscar_imagem(app, 10), className = "circle_img"),
  	        html.Button("Show Me", id = "btn_click_10", n_clicks = 0),
  	      ], className = "item_call_10 row"),
  	    html.Div([
  	        html.H1("ALX"),
  	        html.Img(src = buscar_imagem(app, 11), className = "circle_img"),
  	        html.Button("Show Me", id = "btn_click_11", n_clicks = 0),
  	      ], className = "item_call_11 row"),
  	    html.Div([
  	        html.H1("AGH"),
  	        html.Img(src = buscar_imagem(app, 12), className = "circle_img"),
  	        html.Button("Show Me", id = "btn_click_12", n_clicks = 0),
  	        ], className = "item_call_3 row" ),
  	        
  	        

  	       
	    ], className = "container"),
    br(),br(),
	  br(),br(),
	  br(),br(),
	    html.Div(
	      id= "eps", className = "static_data_ep"
	      ),
	
	
	
	
	
	
], className = "body")


@app.callback( 
  Output('dados', 'children'), 
  Output('img', 'children'),
  Output('eps', 'children'),
  Input('btn_click_0', 'n_clicks'),
  Input('btn_click_1', 'n_clicks'),
  Input('btn_click_2', 'n_clicks'),
  Input('btn_click_3', 'n_clicks'),
  Input('btn_click_4', 'n_clicks'),
  Input('btn_click_5', 'n_clicks'),
  Input('btn_click_6', 'n_clicks'),
  Input('btn_click_7', 'n_clicks'),
  Input('btn_click_8', 'n_clicks'),
  Input('btn_click_9', 'n_clicks'),
  Input('btn_click_10', 'n_clicks'),
  Input('btn_click_11', 'n_clicks'),
  Input('btn_click_12', 'n_clicks'),
)


def displayClick(*btn): 
  if "btn_click_0" == ctx.triggered_id:
    esc = 0
    tratar_API(api, escolha, esc),
    src = buscar_imagem(app, esc)
    extract_len_ep(api,esc)
  if "btn_click_1" == ctx.triggered_id:
    esc = 1
    tratar_API(api, escolha, esc),
    src = buscar_imagem(app, esc)
    extract_len_ep(api,esc)
  if "btn_click_2" == ctx.triggered_id:
    esc = 2
    tratar_API(api, escolha, esc),
    src = buscar_imagem(app, esc)
    extract_len_ep(api,esc)
  if "btn_click_3" == ctx.triggered_id:
    esc = 3
    tratar_API(api, escolha, esc),
    src = buscar_imagem(app, esc)
    extract_len_ep(api,esc)
  if "btn_click_4" == ctx.triggered_id:
    esc = 4
    tratar_API(api, escolha, esc),
    src = buscar_imagem(app, esc)
    extract_len_ep(api,esc)
  if "btn_click_5" == ctx.triggered_id:
    esc = 5
    tratar_API(api, escolha, esc),
    src = buscar_imagem(app, esc)
    extract_len_ep(api,esc)
  if "btn_click_6" == ctx.triggered_id:
    esc = 6
    tratar_API(api, escolha, esc),
    src = buscar_imagem(app, esc)
    extract_len_ep(api,esc)
  if "btn_click_7" == ctx.triggered_id:
    esc = 7
    tratar_API(api, escolha, esc),
    src = buscar_imagem(app, esc)
    extract_len_ep(api,esc)
  if "btn_click_8" == ctx.triggered_id:
    esc = 8
    tratar_API(api, escolha, esc),
    src = buscar_imagem(app, esc)
    extract_len_ep(api,esc)
  if "btn_click_9" == ctx.triggered_id:
    esc = 9
    tratar_API(api, escolha, esc),
    src = buscar_imagem(app, esc)
    extract_len_ep(api,esc)
  if "btn_click_10" == ctx.triggered_id:
    esc = 10
    tratar_API(api, escolha, esc),
    src = buscar_imagem(app, esc)
    extract_len_ep(api,esc)
  if "btn_click_11" == ctx.triggered_id:
    esc = 11
    tratar_API(api, escolha, esc),
    src = buscar_imagem(app, esc)
    extract_len_ep(api,esc)
  if "btn_click_12" == ctx.triggered_id:
    esc = 12
    tratar_API(api, escolha, esc),
    src = buscar_imagem(app, esc)
    extract_len_ep(api,esc)
    
    
  return tratar_API(api, escolha, esc), html.Img(src = buscar_imagem(app, esc)), extract_len_ep(api, esc)




app.run_server(debug = False)
		
