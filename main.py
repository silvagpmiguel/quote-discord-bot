from classes.discord import Client
from dotenv import load_dotenv
import os

# https://discordapp.com/api/oauth2/authorize?client_id=737684380847440022&permissions=1611123776&scope=bot

load_dotenv(dotenv_path=".env")
Client(
    db=os.getenv("DATABASE"), u=os.getenv("USR"),
    passw=os.getenv("PASSWORD"), host=os.getenv("HOST"), port=os.getenv("PORT")
).run(os.getenv("TOKEN"))
