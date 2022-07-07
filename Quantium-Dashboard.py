# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

df = pd.read_csv('S:\code\Quantium_proj\quantium-starter-repo-main\Pink Morsel.csv')
print(df.head(10))




app = Dash(__name__)

colors = {
    'background': '#123456',
    'text': '#7FDBFF'
}
fig = px.line(df, x=df['Date'], y=df['Total Sale of Morsel'])

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Total Sales of Mousel since Jan-15-2021 to February-2022',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='By Samuel Waweru , JKUAT', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)