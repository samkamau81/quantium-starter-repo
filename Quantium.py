from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv('S:\code\Quantium_proj\quantium-starter-repo-main\Pink Morsel.csv')
df=df[(df['Date']>'2021-01-15')] #filtering date to 15th january 2021


app = Dash(__name__)

colors = {
    'background': '#123456',
    'text': '#7FDBFF'
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Total Sales of Mousel since Jan-15-2021 to February-2022 By Region',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='By Samuel Waweru , JKUAT', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(id='graph-with-radio'),
    dcc.RadioItems(
        [
            {
                "label": html.Div(['North'], style={'color': 'Gold', 'font-size': 20, 'font-weight':900}),
                "value": "north",
            },
            {
                "label": html.Div(['South'], style={'color': 'MediumTurqoise', 'font-size': 20, 'font-weight':900}),
                "value": "south",
            },
            {
                "label": html.Div(['East'], style={'color': 'LightGreen', 'font-size': 20, 'font-weight':900}),
                "value": "east",
            },
            {
                "label": html.Div(['West'], style={'color': 'LightGreen', 'font-size': 20, 'font-weight':900}),
                "value": "west",
            },
        ], value='north', id='region_radio'
    )


])


@app.callback(
    Output('graph-with-radio', 'figure'),
    Input('region_radio', 'value'))



def update_figure(selected_region):
    Date = []
    Tot_Sale = []
    for i in range(len(df)):
       if (selected_region==df.iloc[i,2]):
           Tot_Sale.append(df.iloc[i,0])
           Date.append(df.iloc[i,1])



    fig = px.line(df, x=Date, y=Tot_Sale)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
