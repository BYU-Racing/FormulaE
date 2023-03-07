from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
import main
import time

app = Dash(__name__)

file_name = 'Data/Master.csv'
all_sensors = main.readData(file_name)

fig = main.display_dashboard(all_sensors, dark_mode=True)
time_end = 5
freq = 250
spd = main.speedometer(0)
pdl = main.pedals()

app.layout = html.Div([
    html.Div([
        html.H1('Car Go Fast!', style={'color': main.themes["Dark"]["color"][3][2],
                                       'paddingLeft': '30px', 'paddingTop': '10px',
                                       'paddingBottom': '0px', 'margin': '0px',
                                       'display': 'inline-block', 'width': '33%'},
                id='dashboard-title'),
        dcc.Input(
            id='input-time',
            type='text',
            placeholder='Enter a time in seconds',
            value='',
            style={'width': '15%', 'margin': '10px', 'font': main.themes["Dark"]["font"]["p"], }
        )
    ]),
    dcc.Graph(
        id='car_go_fast',
        figure=fig,
        style={'width': '100%', 'height': '120vh', 'margin': '0px'}
    ),
    html.Div([
        dcc.Slider(id='time-slider', min=0, max=time_end, step=0.001, value=0,
                   marks={0: "0", time_end / 2: str(time_end / 2), time_end: str(time_end)}),
        # dcc.Interval(id='interval-component', interval=freq, n_intervals=0)
    ], style={'marginLeft': '50px', 'width': '162vh'}),
    html.Div([
        dcc.Graph(
            id='speedometer',
            figure=spd,
            style={'width': '50vh', 'height': '40vh', 'display': 'inline-block', }
        ),
        dcc.Graph(
            id='pedals',
            figure=pdl,
            style={'width': '50vh', 'height': '40vh', 'display': 'inline-block', }
        ),
        dcc.Graph(id='steering-wheel',
                  config={'displayModeBar': False},
                  style={'width': '50vh', 'height': '40vh', 'display': 'inline-block', }),
        html.P(id='output-values',
               style={'width': '50vh', 'height': '40vh', 'display': 'inline-block',
                      'color': main.themes["Dark"]["color"][3][2],
                      'font-family': main.themes["Dark"]["font"]["p"],
                      'font-size': main.themes["Dark"]["size"]["small"]+"px",
                      'vertical-align': 'top', 'white-space': 'pre-line'}),
    ])
],
    style={'background-color': main.themes["Dark"]["color"][0][2],
           'color': main.themes["Dark"]["color"][0][2],
           'margin': '0px', 'padding': '0px', 'border': '0px', 'outline': '0px'})


# # Define the callback function
# @app.callback(Output('time-slider', 'value'),
#               Input('interval-component', 'n_intervals'))
# def update_slider_graph(n):
#     return ((n*freq) % (time_end * 1000)) / 1000


# define a callback function to update the output values based on the input time
@app.callback(
    Output(component_id='output-values', component_property='children'),
    Output(component_id='speedometer', component_property='figure'),
    Output(component_id='pedals', component_property='figure'),
    Output(component_id='steering-wheel', component_property='figure'),
    Input(component_id='time-slider', component_property='value')
)
def update_output_div(input_value):
    # parse the input time and convert it to an integer
    # time = int(input_value) if input_value.isdigit() else None
    try:
        time = float(input_value)
    except ValueError:
        time = None
    # if the input is not a valid integer, display an error message
    if time is None:
        return 'Please enter a valid decimal time greater than zero.', \
               main.speedometer(0, maxim=10), \
               main.pedals(), \
               main.steering()

    else:
        # get the values of each subplot at the input time
        values = []
        for i in range(1, len(main.legend) + 1):
            trace = fig['data'][i - 1]
            value = round(trace['y'][int(time * 1000)], 4) if time * 1000 < len(trace['y']) else None
            values.append(f'{main.legend[i - 1]}: {value}')

        # compute the average speed to display
        speed = np.mean([float(values[i].split(":")[1][1:]) for i in range(4, 8)])

        # get brake and accelerator values
        brake = float(values[2].split(":")[1][1:])
        acceleration = np.mean([float(values[i].split(":")[1][1:]) for i in range(0, 2)])

        # display extra values
        extra = html.P("Time: " + str(input_value) + "\n\n" + '\n'.join(values[-5:]),
                       id='output-values',
                       style={'width': '50vh', 'height': '40vh', 'display': 'inline-block',
                              'color': main.themes["Dark"]["color"][3][2],
                              'font-family': main.themes["Dark"]["font"]["p"],
                              'font-size': main.themes["Dark"]["size"]["small"]+"px",
                              'vertical-align': 'top', 'white-space': 'pre-line'}
                       )

        # get steering angle
        angle = float(values[9].split(":")[1][1:])

        # return figures
        return extra, \
               main.speedometer(speed, maxim=10), \
               main.pedals(brake, acceleration, maxim=5), \
               main.steering(angle=angle)


if __name__ == '__main__':
    app.run_server(debug=True)
