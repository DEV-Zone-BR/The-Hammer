from discord import Client

from config import TOKEN, intents


class MyClient(Client):
    async def on_ready(self):
        print(f'Logged as {self.user}')
        for guild in self.guilds:
            print(guild)
            print('  {} members'.format(len([m.name for m in guild.members])))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Bem vindo {0.mention} ao {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)


client = MyClient(intents=intents)

client.run(TOKEN)
