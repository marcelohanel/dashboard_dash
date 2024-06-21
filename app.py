from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_excel('Vendas.xlsx')

fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
opcoes = list(df["ID Loja"].unique())
opcoes.append("Todas as lojas")

app.layout = html.Div(children=[
    html.H1(children='Faturamento das Lojas'),
    html.H2(children='Gráfico de faturamento com todos os produtos separados por loja'),
    html.Div(children='OBS.: Este gráfico mostra a quantidade de vendas, não o faturamento'),

    dcc.Dropdown(
        id='lista-lojas',
        options=opcoes,
        value=opcoes[0],
    ),
    
    dcc.Graph(
        id='grafico-quantidade-vendas',
        figure=fig
    ),
])

@app.callback(
    Output('grafico-quantidade-vendas', 'figure'),
    Input('lista-lojas', 'value')
)
def update_output(value):
    if value == "Todas as lojas":
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df["ID Loja"] == value]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")

    
    return fig

if __name__ == '__main__':
    app.run(debug=True)
