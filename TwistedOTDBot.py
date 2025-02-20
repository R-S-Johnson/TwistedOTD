from DataManager import DataManager
from discord.ext import commands
import discord
import logging
import sys
import os


class TwistedOTDBot(commands.Bot):

    def __init__(self, command_prefix='$', **kwargs):
        super().__init__(command_prefix, **kwargs)
                
        if not os.path.isdir("botData"):
            os.mkdir("botData")
        self.data_manager = DataManager("botData/botData.json")
                    
    
    async def on_ready(self):
        ''''''
        print("Twisted OTD Bot is running and ready!!")
        
    
    async def setup_hook(self):
        ''''''
        self.guild_channel_map = self.data_manager.get_data()
        await self.load_extension("CommandsCog")
        await self.load_extension("TimerCog")
    
        
    async def send_message(self, message):
        ''''''
        data = self.data_manager.get_data()
        for guild in self.guilds:
            if guild.id in data.keys():
                print("Sending Twisted Board update!")
                channel_id = data[guild.id]
                channel = guild.get_channel(channel_id)

                await channel.send(message)



if __name__ == '__main__':
    
    intents_dict = {
        'messages': True,
        'message_content': True,
        'guilds': True
    }
    
    discord_key_path = sys.argv[1]
    with open(discord_key_path) as f:
        discord_key = f.read()
        
    logging_handler = logging.FileHandler(filename='logs/discord.log',
                                          encoding='utf-8', mode='w')
    intents = discord.Intents(**intents_dict)
    client = TwistedOTDBot(intents=intents)
    client.run(discord_key, log_handler=logging_handler)