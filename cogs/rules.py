import discord
from discord.ext import commands
import json

class Rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        # Load config
        try:
            with open('config.json', 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = {}

    @commands.command(name='postrules')
    async def post_rules_command(self, ctx):
        """Post server rules in the rules channel (admin only)"""
        print(f"Debug: postrules command called by {ctx.author.name} (ID: {ctx.author.id})")
        print(f"Debug: User has admin permissions: {ctx.author.guild_permissions.administrator}")
        
        if not ctx.author.guild_permissions.administrator:
            await ctx.send("❌ You don't have permission to post rules.")
            return
        
        try:
            rules_channel_id = self.config.get('rules_channel_id')
            print(f"Debug: Rules channel ID from config: {rules_channel_id}")
            
            if not rules_channel_id:
                await ctx.send("❌ No rules channel ID found in config.json")
                return
            
            rules_channel = ctx.guild.get_channel(rules_channel_id)
            print(f"Debug: Found rules channel: {rules_channel}")
            
            if not rules_channel:
                await ctx.send(f"❌ Could not find rules channel with ID {rules_channel_id}")
                return
            
            # Create comprehensive rules embed
            embed = discord.Embed(
                title="📜 Server Rules",
                description="Welcome to our Minecraft server! Please read and follow these rules to ensure everyone has a great experience.",
                color=discord.Color.gold()
            )
            
            embed.add_field(
                name="🎮 General Behavior",
                value="• Be respectful and kind to ALL NEW players\n• We have fun here but no direct threats or slurs.\n• No spamming in chat or voice channels\n• No exploiting the server\n• No advertising other servers or services",
                inline=False
            )
            
            embed.add_field(
                name="🏗️ Building",
                value="• Griefing must be done officially through the grief request submissions form.' \n• Ask permission before building near others\n• No inappropriate or offensive builds\n• Respect spawn area and community builds\n• Griefing without permission will result in a ban.",
                inline=False
            )
            
            embed.add_field(
                name="💬 PVP/Cult Wars",
                value="• Cults may officially declare war on other cults.\n• No griefing bases during wars. Griefs are reserved for special situations.\n• No using hacked clients or mods.\n• No killing players in the spawn area.\n• Report issues to staff members",
                inline=False
            )
            
            embed.add_field(
                name="🛡️ Security",
                value="• No sharing account information\n• No using hacked clients or mods\n• No attempting to hack or exploit\n• Report suspicious activity to staff\n• Keep your account secure",
                inline=False
            )
            
            embed.add_field(
                name="⚖️ Consequences",
                value="• First offense: Warning\n• Second offense: Temporary mute/ban\n• Third offense: Permanent ban\n• Severe violations: Immediate ban\n• Appeals can be made to staff",
                inline=False
            )
            
            embed.add_field(
                name="📞 Getting Help",
                value="• Use `!apply` to join the server\n• Contact staff for questions or issues\n• Check pinned messages for updates\n• Join our community events!",
                inline=False
            )
            
            embed.set_footer(text="By joining our server, you agree to follow these rules. Have fun!")
            embed.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else None)
            
            await rules_channel.send(embed=embed)
            await ctx.send("✅ Server rules posted successfully!")
            
        except Exception as e:
            await ctx.send(f"❌ Error posting rules: {e}")
            print(f"Error posting rules: {e}")

async def setup(bot):
    await bot.add_cog(Rules(bot)) 