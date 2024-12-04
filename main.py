# Python D&D Character Sheet
# (C)RLM Productions

import pygame, os, time, sys, cursor
from rich.console import Console
from rich.theme import Theme
from functions import *
from classes import *

# Metadata
GameDescInfo = { 
'GameTitle' : 'D&D Character Sheet',
'GameSubtitle' : '5e',
'GameVersion' : '0.1',
'Copyright' : 'RLM Productions',
'Author' : 'Richard Miller'
}

# Create Temp Player Sheet
newplayer = Player("Rich", "dwarf dude", "Warrior", "Paladin", 10, 100, 1, 1, 1,1,1,66,0,1)
newplayer.hp = Player.hp(100,100,100)
newplayer.intelligence(1,10,1,1,1,1,1,1)


def openSheet():
    os.system('cls')
    newplayer = load_character_sheet()
    print(newplayer.name,newplayer.hp.current_hp)
    exit(0)
    return

# Main Menu
while True:
    os.system('cls')
    ans = ''
    filetitle = 'assets/art/title.dat'
    data = ''
    custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
    console = Console(theme=custom_theme, highlight=None)
    console.print("[red]"+loadArt(filetitle, data)+"[/red]"+"  [green]"+GameDescInfo['GameVersion']+"[/green]")
    console.print('')

    # Print Choices
    
    console.print("([red]1[/red]) Open Character Sheet")     
    console.print("([red]2[/red]) New Character Sheet")
    console.print("([red]3[/red]) Quit")
    ans = console.input("\n[yellow]Selection> [/yellow]")

    # Run Choices
    if ans == '1':
        openSheet()
    elif ans == '2':
        newplayer = createSheet(newplayer)
    elif ans == '3':
        save_character_sheet(newplayer)
        break

### EXIT CODE ###
os.system('cls')