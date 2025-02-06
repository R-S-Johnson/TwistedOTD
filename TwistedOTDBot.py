from TaskManager import TaskManager
import discord
import logging
import sys


class TwistedOTDBot(discord.ext.commands.Bot):

    def __init__(self, command_prefix='$', **kwargs):
        super().__init__(command_prefix, **kwargs)
                
        self.channel_name = 'twisted-board'
        self.channel_id = 0
        self.channel = None
        self.discord_server = None
                
    
    async def on_ready(self):
        ''''''
        task_manager = TaskManager(self)
        await self.add_cog(task_manager)
        print("Twisted OTD Bot (with cog) is running and ready!!")
    
        
    async def send_message(self, message):
        ''''''
        for channel in self.guilds[0].text_channels:
            if channel.name == 'twisted-board':
                print("Sending Twisted Board update!")
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