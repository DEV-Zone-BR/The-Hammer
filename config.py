import os

from discord import Intents
from environs import Env

env = Env()
env.read_env()

TOKEN = env('DISCORD_TOKEN')

ETERNAL_ROLES = {'@everyone', 'anbu', 'anbu+', 'Admin'}

intents = Intents.default()
intents.members = True
intents.guilds = True
intents.members = True
