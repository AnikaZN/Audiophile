# Audiophile

## File Structure

```
├─── audiophile
│   ├─── core
│   │   ├─── functions.py: Contains all functionality for gameplay
│   │   ├─── item.py: Contains the Item class
│   │   ├─── player.py: Contains the Player class
│   │   └─── room.py: Contains the Room class, dictionary of all rooms, and ghost_rooms list
│   │   
│   ├─── data
│   │   ├─── 2018-07-02_-_Tears_of_Joy_-_David_Fesliyan.mp3: Victory theme
│   │   ├─── 2020-02-16_-_Anxiety_-_David_Fesliyan.mp3: Death theme
│   │   ├─── 2020-06-25_-_Dark_Shadows_-_www.FesliyanStudios.com_David_Fesliyan.mp3: Warning theme
│   │   ├─── AGENCYB.TTF: Font
│   │   ├─── bathroom.jpg: Photo by David Babayan on Unsplash
│   │   ├─── bedroom.jpg: Photo by Riccardo Retez on Unsplash
│   │   ├─── closet.jpg: Photo by Julija V. on Unsplash
│   │   ├─── dining.jpg: Photo by Daniela on Unsplash
│   │   ├─── foyer.jpg: Photo by Kirk Lai on Unsplash
│   │   ├─── Gabriola.TTF: Font
│   │   ├─── hallway.jpg: Photo by Echo Grid on Unsplash
│   │   ├─── house.jpg: Photo by Matthew T Rader on Unsplash
│   │   ├─── laundry.jpg: Photo by Pau Casals on Unsplash
│   │   ├─── linen.jpg: Photo by Zane Lee on Unsplash
│   │   ├─── living.jpg: Photo by Morgan Vander Hart on Unsplash
│   │   ├─── MysteriousSuspensefulMusic2018-11-03_-_Dark_Fog_-_David_Fesliyan.mp3: General theme
│   │   ├─── pbath.jpg: Photo by Quinton Coetzee on Unsplash
│   │   ├─── piano.jpg: Photo by Richard Ludwig on Unsplash
│   │   ├─── primary.jpg: Photo by Bianca Capeloti on Unsplash
│   │   ├─── nursery.jpg: Photo by freestocks on Unsplash
│   │   ├─── secret.jpg: Photo by Katherine Kromberg on Unsplash
│   │   ├─── stairs.jpg: Photo by Dima Pechurin on Unsplash
│   │   ├─── ui_theme.json: Design details
│   │   ├─── vacant.jpg: Photo by bill wegener on Unsplash
│   │   └─── wall.jpg: Photo by Adi Goldstein on Unsplash
│   │
│   ├─── audiophile.py: Core file for gameplay
│   └─── christmas_adventure_notes.txt: Notes on reference repository
│   
├─── scratchpad
│   ├─── clips: Miscellaneous voice recordings
│   ├─── archived_playable.py: Function-based version of the game. Not fully playable.
│   ├─── audio_test.py: Code to record audio from a microphone
│   └─── db_test.py: Code to save audio files and their corresponding text in a SQL database
|
├─── terminal_game
│   ├── sound_effects: Same audio clips from audiophile/data
│   ├─── src
│   │   ├─── adv.py: While-loop-based version of the game. Not fully playable.
│   │   ├─── item.py: Contains the Item class
│   │   ├─── playable.py: While-loop-based version of the game. Fully playable.
│   │   ├─── player.py: Contains the Player class
│   │   └─── room.py: Contains the Room class
│
├─── .gitignore
├─── LICENSE
├─── Pipfile
├─── Pipfile.lock
└─── README.md
```

## How to Play

### Terminal Only:

- Clone repo

- `cd audiophile`

- `pipenv shell`

- `pipenv install`

- `cd terminal_game/src`

- `python playable.py`

- Have fun!

### PyGame Version:

- Clone repo

- `cd audiophile`

- `pipenv shell`

- `pipenv install`

- `cd audiophile`

- `python audiophile.py`

- Have fun!
