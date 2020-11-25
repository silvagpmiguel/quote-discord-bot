from classes.discord import Client
import sys

# https://discordapp.com/api/oauth2/authorize?client_id=737684380847440022&permissions=1611123776&scope=bot
if len(sys.argv) == 2:
    Client().run(sys.argv[1])
else:
    print('Error. Usage: python3.6 main.py <YOUR_BOT_TOKEN>')