from TwsistedGrabber import GrabTwisted
from discord.ext import commands, tasks
from datetime import time
from pytz import timezone
import discord



class TimerCog(commands.Cog):
    
    def __init__(self, parent_bot, **kwargs):
        super().__init__(**kwargs)
        
        self.parent_bot = parent_bot
        
        self.get_twisted.start()
        
        
    def cog_unload(self):
        self.get_twisted.cancel()
        
        
    @tasks.loop(time=time(hour=22, minute=33, tzinfo=timezone("US/Eastern")))
    async def get_twisted(self):
        print("Time to update the board!")

        twisted_message = GrabTwisted()     

        print(twisted_message)
        await self.parent_bot.send_message(twisted_message)


async def setup(bot):
    await bot.add_cog(TimerCog(bot))