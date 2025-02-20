from TwsistedGrabber import GrabTwisted
from discord.ext import commands
import discord


class CommandsCog(commands.Cog):
    
    def __init__(self, parent_bot, **kwargs):
        super().__init__(**kwargs)
        
        self.parent_bot = parent_bot
        
    
    @commands.command(name="AddChannel")
    async def add_channel(self, ctx, *, channel: discord.TextChannel):
        ''''''
        guild_id = ctx.guild.id
        channel_id = channel.id
        
        self.parent_bot.guild_channel_map[guild_id] = channel_id
        self.parent_bot.data_manager.update_data(guild_id, channel_id)
        
        await ctx.send(f"Channel: {channel.name} recognized and saved!")
        
        
    @commands.command(name="WhoTwisted", aliases=["WHO"])
    async def current_twisted(self, ctx):
        ''''''
        print("Manual call to send twisted!")
        
        twisted_message = GrabTwisted()
        
        print(twisted_message)
        await ctx.send(twisted_message)


async def setup(bot):
    await bot.add_cog(CommandsCog(bot))