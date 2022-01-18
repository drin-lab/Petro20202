from dash import Dash
from dash import dcc
from dash import html
import pandas as pd
data = pd.read_csv("PETR4.SA.csv")

external_stylesheets = [
    {
        "href":"https://fonts.googleapis.com/css2?"
        "family=Lato:wgt@400;700&display=swap",
        "rel":"stylesheet",
    },
]

app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = "Análise ação PETR4: preços ações Petrobrás"

app.layout = html.Div(
    children=[
        html.Div(
            children =[
                html.H1(children = "Evolução de valores PETR4 (2018/2020)",
                className="header-title"),
                html.P(
                    children = "Análise do comportamento do preço das ações PETR4 entre 2018 e 2020",
                className="header-description",),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(children=dcc.Graph(
                            id="price-chart",
                            config={"displayModeBar":False},
                            figure={
                                "data":[
                                    {
                                        "x":data["Date"],
                                        "y":data["Close"],
                                        "type":"lines",
                                        "hovertemplate":"Data: %{x} - R$%{y:.2f}<extra></extra>",
                                    },
                                ],
                                "layout":{
                                    "title":{
                                        "text":"Série temporal (2018-2020): preço fechamento PETR4",
                                        "x":0.05,
                                        "xanchor":"left",
                                    },
                                    "xaxis":{"fixedrange":True},
                                    "yaxis":{"tickprefix":"R$","fixedrange":True},
                                    "colorway":["#17B897"],
                                },
                            },
                ),
                className="card",
            ),
            
            ],
            className="wrapper",
        ),
    ]
)



        
if __name__=="__main__":
    app.run_server(debug=True)
    