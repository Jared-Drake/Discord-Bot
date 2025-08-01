import discord
from discord.ext import commands
import json

class JoinInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        # Load config
        try:
            with open('config.json', 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = {}

    @commands.command(name='postjoininfo')
    async def post_join_info_command(self, ctx):
        """Post How to Join information in the How to Join channel (admin only)"""
        if not ctx.author.guild_permissions.administrator:
            await ctx.send("❌ You don't have permission to post join information.")
            return
        
        try:
            join_channel_id = self.config.get('join_channel_id')
            if not join_channel_id:
                await ctx.send("❌ No join channel ID found in config.json")
                return
            
            join_channel = ctx.guild.get_channel(join_channel_id)
            if not join_channel:
                await ctx.send(f"❌ Could not find join channel with ID {join_channel_id}")
                return
            
            # Create comprehensive How to Join embed
            embed = discord.Embed(
                title="🎮 How to Join Our Minecraft Server",
                description="Follow these steps to join our Paper Minecraft 1.21.8 server!",
                color=discord.Color.green()
            )
            
            embed.add_field(
                name="📋 Prerequisites",
                value="• Minecraft Java Edition (not Bedrock)\n• A Discord account\n• Completed application process",
                inline=False
            )
            
            embed.add_field(
                name="🖥️ Step 1: Open Minecraft Launcher",
                value="Launch Minecraft Java Edition using the official launcher or your preferred launcher (like MultiMC, Prism, etc.)",
                inline=False
            )
            
            embed.add_field(
                name="🌐 Step 2: Add Server",
                value="1. Click 'Multiplayer' in the main menu\n2. Click 'Add Server'\n3. Enter a name for the server (e.g., 'Cult Server')\n4. Enter the server address: **`notacult.playit.pub`**",
                inline=False
            )
            
            embed.add_field(
                name="🎯 Step 3: Connect",
                value="1. Select the server from your server list\n2. Click 'Join Server'\n3. Wait for the connection to establish",
                inline=False
            )
            
            embed.add_field(
                name="⚠️ Important Notes",
                value="• Make sure you're using Minecraft Java Edition 1.21.8\n• You must have completed the application process first\n• If you can't connect, check your internet connection\n• Contact staff if you encounter any issues",
                inline=False
            )
            
            embed.add_field(
                name="🔧 Troubleshooting",
                value="• **Can't connect?** Check if the server is online\n• **Wrong version?** Make sure you're on 1.21.8\n• **Still having issues?** Ask in the #general channel",
                inline=False
            )
            
            embed.add_field(
                name="📞 Need Help?",
                value="If you're having trouble connecting, feel free to ask for help in the general chat or contact a staff member.",
                inline=False
            )
            
            embed.set_footer(text="Welcome to our community! We hope you enjoy your time on the server!")
            embed.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else None)
            
            await join_channel.send(embed=embed)
            await ctx.send("✅ How to Join information posted successfully!")
            
        except Exception as e:
            await ctx.send(f"❌ Error posting join information: {e}")
            print(f"Error posting join information: {e}")

async def setup(bot):
    await bot.add_cog(JoinInfo(bot)) 