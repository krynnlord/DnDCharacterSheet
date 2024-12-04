import sys, time, os, cursor, pickle
from classes import *

# Set Font Colors
class ColorStyle():
    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    YELLOW = "\033[33m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    RESET = "\033[0m"

# Load Art form DAT file Function
def loadArt(filetitle, data):
    with open(filetitle, 'r') as file:
        data = file.read().rstrip()
        return(data)
    
# Text-Printer Slow
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
        
# Text-Printer Normal
def delay_print2(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)    

# Create New Character Sheet
def createSheet(temp_Player):
    os.system('cls')
    filetitle = 'assets/art/createhero.dat'
    data = ''
    print(f"{ColorStyle.YELLOW}"+loadArt(filetitle, data)+f"{ColorStyle.RESET}")
    print("\nCreating a new character. Please enter a name.")
    cursor.show()
    name = input('Name: ' )
    if name == '':
        cursor.hide()
        print('You must enter a name.')
        time.sleep(2)
        createSheet(temp_Player)
    if len(name) < 3:
        cursor.hide()
        print('Your name must be 3 characters or more in length')
        time.sleep(2)
        createSheet(temp_Player)
    cursor.hide()
    shortname = name[:20]
    
    temp_Player = Player(shortname, "dwarf dude", "Warrior", "Human", "Paladin", 100, 1, 1, 1,1,1,66,0,1)
    temp_Player.hp = Player.hp(122,100,100)
    temp_Player.intelligence(1,10,1,1,1,1,1,1)
    
    return temp_Player

# Save Sheet
def save_character_sheet(newplayer):
    with open('save/player.dat', 'wb') as handle:
        pickle.dump(newplayer, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return

# Load Sheet
def load_character_sheet():
    with open('save/player.dat', 'rb') as handle:
        newplayer = pickle.load(handle)
    return newplayer