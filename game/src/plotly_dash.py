import dash
import dash_core_components as dcc
import os
import pygame
import random
from dash.dependencies import Input, Output
import dash_html_components as html
from room import Room
from player import Player
from item import Item
from adv import room, item

# Put items in rooms
room['outside'].add_item('pebble')
room['living'].add_item('dog collar')
room['piano'].add_item('knife')
room['dining'].add_item('broken chair leg')
room['kitchen'].add_item('moldy bread')
room['nursery'].add_item('teddy bear')
room['vacant'].add_item('chunk of concrete')
room['laundry'].add_item('key')
room['bedroom'].add_item('journal')
room['bath'].add_item('crystal goblet')
room['pbath'].add_item('dead bird')
room['primary'].add_item('brooch')
room['closet'].add_item('hanger')
room['secret'].add_item('crumpled photo')
room['linen'].add_item('damp towel')

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['stairs']
room['foyer'].e_to = room['dining']
room['foyer'].w_to = room['living']
room['living'].n_to = room['piano']
room['living'].e_to = room['foyer']
room['piano'].s_to = room['living']
room['dining'].n_to = room['kitchen']
room['dining'].w_to = room['foyer']
room['kitchen'].s_to = room['dining']
room['stairs'].w_to = room['whall']
room['stairs'].e_to = room['ehall']
room['stairs'].n_to = room['primary']
room['stairs'].s_to = room['foyer']
room['whall'].s_to = room['nursery']
room['whall'].w_to = room['whall2']
room['whall'].n_to = room['linen']
room['whall'].e_to = room['stairs']
room['nursery'].n_to = room['whall']
room['whall2'].s_to = room['vacant']
room['whall2'].n_to = room['laundry']
room['whall2'].e_to = room['whall']
room['vacant'].n_to = room['whall2']
room['laundry'].s_to = room['whall2']
room['linen'].s_to = room['whall']
room['primary'].w_to = room['closet']
room['primary'].e_to = room['pbath']
room['primary'].s_to = room['stairs']
room['closet'].e_to = room['primary']
room['closet'].w_to = room['secret']
room['secret'].e_to = room['closet']
room['pbath'].w_to = room['primary']
room['ehall'].e_to = room['ehall2']
room['ehall'].s_to = room['bedroom']
room['ehall'].w_to = room['stairs']
room['ehall2'].s_to = room['bath']
room['ehall2'].w_to = room['ehall']
room['bath'].n_to = room['ehall2']
room['bedroom'].n_to = room['ehall']

ghost_rooms = ['living', 'piano', 'dining', 'kitchen', 'nursery', 'laundry',
               'bedroom', 'bath', 'pbath', 'primary', 'closet', 'vacant',
               'linen']

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config.suppress_callback_exceptions = True # see https://dash.plot.ly/urls
app.title = 'Audiophile' # appears in browser title bar
server = app.server

app.layout = html.Div([
    # dcc.Input(
    #     id='name',
    #     placeholder='What is your name?',
    #     type='text',
    #     value=''
    # ),
    dcc.Markdown('## Choose a direction.', className='mb-5'),
    html.Div(id='container-button-timestamp'),
    html.Div([
        html.Button('North', id='north', n_clicks=0),
    ]),
    html.Div([
        html.Button('West', id='west', n_clicks=0),
        html.Button('East', id='east', n_clicks=0),
    ]),
    html.Div([
        html.Button('South', id='south', n_clicks=0),
    ])
])

def start():
    # Main
    pygame.init()
    # pygame.mixer.music.load('../sound_effects/MysteriousSuspensefulMusic2018-11-03_-_Dark_Fog_-_David_Fesliyan.mp3')
    # pygame.mixer.music.play()

    return(f'--- Welcome! Your current location is: {player.room_info()}')

@app.callback(Output('container-button-timestamp', 'children'),
              [Input('north', 'n_clicks'),
               Input('west', 'n_clicks'),
               Input('east', 'n_clicks'),
               Input('south', 'n_clicks')],
               prevent_initial_call=True)

def move(btn1, btn2, btn3, btn4):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'north' in changed_id:
        direction = 'n'
    elif 'west' in changed_id:
        direction = 'w'
    elif 'east' in changed_id:
        direction = 'e'
    elif 'south' in changed_id:
        direction = 's'

    os.system(f'python adv2.py -d {direction}')

if __name__ == '__main__':
    player = Player(room['outside'])
    ghost = Player(room[random.choice(ghost_rooms)])
    print(start())
    app.run_server(debug=True)
