from datetime import time
from discord.ext import commands, tasks
from pytz import timezone
from TwsistedGrabber import GrabTwisted


class TaskManager(commands.Cog):

    def __init__(self, parent_bot):
        self.parent_bot = parent_bot
        
        self.task = self.get_twisted.start()
        

    def cog_unload(self):
        self.get_twisted.cancel()
        
    
    @tasks.loop(time=time(hour=19, minute=5, tzinfo=timezone("US/Eastern")))
    async def get_twisted(self):
        print("7pm! time to update the board!")

        twisted_message = GrabTwisted()     

        print(twisted_message)
        await self.parent_bot.send_message(twisted_message)