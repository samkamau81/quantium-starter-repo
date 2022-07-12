# 1. imports of your dash app
from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
# add this in the conftest.py under tests folder
from selenium.webdriver.chrome.options import Options

def pytest_setup_options():
    options = Options()
    options.add_argument('--disable-gpu')
    return options
# 2. give each testcase a tcid, and pass the fixture

# as a function argument, less boilerplate
def test_bsly001_falsy_child(dash_duo):
    # 3. define your app inside the test function
    app = Dash(__name__)

    df = pd.read_csv('S:\code\Quantium_proj\quantium-starter-repo-main\Pink Morsel.csv')
    print(df.head(10))

    df = df[(df['Date'] > '2021-01-15')]  # filtering date to 15th january 2021

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
    app.layout = html.Div(id="nully-wrapper", style={'backgroundColor': colors['background']}, children=[
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
    # 4. host the app locally in a thread, all dash server configs could be
    # passed after the first app argument
    dash_duo.start_server(app)
    # 5. use wait_for_* if your target element is the result of a callback,
    # keep in mind even the initial rendering can trigger callbacks
    dash_duo.wait_for_text_to_equal("#nully-wrapper", "0", timeout=10)
    # 6. use this form if its present is expected at the action point
    assert dash_duo.find_element("#nully-wrapper").text == "0"
    # 7. to make the checkpoint more readable, you can describe the
    # acceptance criterion as an assert message after the comma.
    assert dash_duo.get_logs() == [], "browser console should contain no error"
    # 8. visual testing with percy snapshot
    dash_duo.percy_snapshot("bsly001-layout")