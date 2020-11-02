import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from datetime import datetime as dt

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



markdown="""

Nagłóki
# h1
## h2
### h3
#### h4
##### h5
###### h6

znaczki tesktu:    
~~przekreselnie~~, *kursywa* lub _tekst kursywa_ , **tekst pogrubiony** , **_tekst pogrubiony i kursywa_**   

Listy numeryczna:  
1. Python  
2. SQL  
3. Java  

Listy punktowa:  
* Python
* SQL
* Java

Linkowanie:  
[Google.com](http://www.google.com)

blok kodu:  
```
print("hello word!")
print("hello word!")
print("hello word!")
```   

Tabele: 
 
|User id | Order  | Age    |
|--------|--------|--------|
|id:232      | 3233  |23 lat     |
|id:132      | 33  |25 lat     |
|id:238      | 2233  |278 lat     |


  
linia horyzontalna:   
___
lub  
***  

cytowanie:  
> hej ho to jest cytat  



"""




app.layout = html.Div([

    dcc.Dropdown(
        options=[
            {"label": "Python", "value": "py"},
            {"label": "SQL", "value": "sql"},
            {"label": "Java", "value": "java"}

        ],
        value="py",
        placeholder="Wybierz technologie ..."
    ),

    html.Br(),

    dcc.Dropdown(
        options=[
            { "label" : "Python", "value":"py" },
            { "label" : "SQL", "value":"sql" },
            {"label": "Java", "value": "java"}

        ],
        value="py",
        placeholder="Wybierz technologie ...",
        multi=True
    ),

    html.Br(),

    dcc.Slider(
        min=0,
        max=100,
        step=5,
        value=35,
        # marks={0:"0",25:"25",50:"50",75:"75", 100:"100"},
        marks={i: f'{i}' for i in range(0,101,25)}
    ),

    html.Div([
       dcc.Input(
            type="text",
            placeholder="Wpisz teskt"
        ),

        dcc.Input(
            type="number",
            placeholder="Wpisz liczbe"
        ),

        dcc.Input(
            type="password",
            placeholder="Wpisz hasło"
        ),

        dcc.Input(
            type="email",
            placeholder="Wpisz email",
        )
    ]),


    html.Br(),html.Br(),

    dcc.Textarea(
        placeholder="Wpisz teskt",
        style={"width":"100%"}
    ),

    html.Br(),

    dcc.Checklist(
        options=[
            {'label': "Python", "value":"py", "disabled":True},
            {'label': "Java", "value": "java"},
            {'label': "SQL", "value": "sql"},
        ],
        value=["java","sql"]
    ),

    html.Br(),

    dcc.RadioItems(
        options=[
            {'label': "Python", "value":"py"},
            {'label': "Java", "value": "java"},
            {'label': "SQL", "value": "sql", "disabled":True},
        ],
        value="java",
        labelStyle={"display":"inline-block"}  #ustawia całośc w pozomie
    ),

    html.Br(),

    html.Button("Przycisk",
                type="submit"
    ),

    html.Br(),html.Br(),

    dcc.DatePickerSingle(
        date= dt(2019,1,1),
        display_format="YYYY-MM-DD"
    ),

    html.Br(), html.Br(),

    dcc.DatePickerRange(
        start_date=dt(2019, 1, 1),
        end_date=dt(2020, 1, 1),
        display_format="DD-MM-YYYYY"
    ),

    html.Br(),

    dcc.Markdown(markdown),

    dcc.Tabs(
        children=[
            dcc.Tab(
                label="Java",
                children=[
                    dcc.Markdown(
                        """
                        ```
                        print("hello word!")
                        ```   
                        """
                    )
                ]
            ),
            dcc.Tab(
                label="Kod",
                children=[
                    dcc.Markdown(
                        """
                        ```
                        print("jooł !")
                        ```   
                        """
                    )
                ]
            )
        ]
    ),

    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Bar(
                    x=[2017,2018,2019],
                    y=[233,435,235],
                    name="Sprzedaż USA",
                    marker=go.bar.Marker(
                        color="red"
                    )
                ),
                go.Bar(
                    x=[2017,2018,2019],
                    y=[133,135,535],
                    name="Sprzedaż Europa",
                    marker=go.bar.Marker(
                        color="rgb(55,84,123)"
                    )
                )
            ],
            layout=go.Layout(
                title="Sprzedaz USA vs. Europa"
            )
        )
    )

],
style={"width":"33%", "margin-left":"auto","margin-right":"auto", "margin-top":"50px"})

if __name__ == '__main__':
    app.run_server(debug=True)
