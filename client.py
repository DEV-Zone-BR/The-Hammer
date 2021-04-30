from discord import Client

from config import TOKEN, intents


class MyClient(Client):
    async def on_ready(self):
        print(f'Logged as {self.user}')
        for guild in self.guilds:
            print(guild)
            print('  {} members'.format(len([m.name for m in guild.members])))

    async def on_message(self, message):
        print('on message')
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

    async def on_member_join(self, member):
        print('on member join')
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Bem vindo {0.mention} ao {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)

    async def on_member_update(self, before, after):
        print('on_member_update')
        print(self)
        print(before)
        print(after)

    async def on_user_update(self, before, after):
        print('on_user_update')
        print(self)
        print(before)
        print(after)


client = MyClient(intents=intents)

client.run(TOKEN)
