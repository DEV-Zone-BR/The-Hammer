import os

from discord import Intents
from environs import Env

env = Env()
env.read_env()

TOKEN = env("DISCORD_TOKEN")

ETERNAL_ROLES = {"anbu", "anbu+", "Admin"}

ALLOWED_ROLES = {"ban": ["admin", "anbu", "anbu+"]}

intents = Intents.default()
intents.members = True
intents.guilds = True
intents.members = True
