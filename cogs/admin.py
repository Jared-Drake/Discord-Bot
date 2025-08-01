import discord
from discord.ext import commands
import json

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        # Load config
        try:
            with open('config.json', 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = {}

    @commands.command(name='bothelp')
    async def help_command(self, ctx):
        """Show help information"""
        print(f"Debug: bothelp command called by {ctx.author.name}")
        embed = discord.Embed(
            title="Cult Bot",
            description="Welcome to the application system!",
            color=discord.Color.blue()
        )
        
        embed.add_field(
            name="User Commands",
            value="`!apply` - Start an application\n`!bothelp` - Show this help message",
            inline=False
        )
        
        embed.add_field(
            name="Admin Commands",
            value="`!applications` - List pending applications\n`!postrules` - Post server rules\n`!postfaq` - Post FAQ",
            inline=False
        )
        
        await ctx.send(embed=embed)

    @commands.command(name='test')
    async def test_command(self, ctx):
        """Test command to check if bot is working"""
        print(f"Debug: test command called by {ctx.author.name}")
        await ctx.send("✅ Bot is working! Commands are being processed.")

async def setup(bot):
    await bot.add_cog(Admin(bot)) 