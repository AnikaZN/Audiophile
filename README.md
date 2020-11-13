# Audiophile

## File Structure

audiophile

  |

  --- core

       |

       --- functions.py: Contains all functionality for gameplay

       --- item.py: Contains the Item class

       --- player.py: Contains the Player class

       --- room.py: Contains the Room class, dictionary of all rooms, and ghost_rooms list

  --- data

       |

       --- 2018-07-02_-_Tears_of_Joy_-_David_Fesliyan.mp3: Victory theme

       --- 2020-02-16_-_Anxiety_-_David_Fesliyan.mp3: Death theme

       --- 2020-06-25_-_Dark_Shadows_-_www.FesliyanStudios.com_David_Fesliyan.mp3: Warning theme

       --- AGENCYB.TTF: Font

       --- Gabriola.TTF: Font

       --- MysteriousSuspensefulMusic2018-11-03_-_Dark_Fog_-_David_Fesliyan.mp3: General theme

       --- ui_theme.json: Design details

  --- audiophile.py: Core file for gameplay

  --- christmas_adventure_notes.txt: Notes on reference repository
scratchpad

  --- clips: Miscellaneous voice recordings

  --- archived_playable.py: Function-based version of the game. Not fully playable.

  --- audio_test.py: Code to record audio from a microphone

  --- db_test.py: Code to save audio files and their corresponding text in a SQL database

terminal_game

  --- sound_effects: Same audio clips from audiophile/data

  --- src

       |

       --- adv.py: While-loop-based version of the game. Not fully playable.

       --- item.py: Contains the Item class

       --- playable.py: While-loop-based version of the game. Fully playable.

       --- player.py: Contains the Player class

       --- room.py: Contains the Room class

.gitignore: Python

LICENSE: MIT

Pipfile, Pipfile.lock: Environment dependencies

README.md
