import discord
from discord.ext import commands
import json

class FAQ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        # Load config
        try:
            with open('config.json', 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = {}

    @commands.command(name='postfaq')
    async def post_faq_command(self, ctx):
        """Post FAQ in the FAQ channel (admin only)"""
        if not ctx.author.guild_permissions.administrator:
            await ctx.send("❌ You don't have permission to post FAQ.")
            return
        
        try:
            faq_channel_id = self.config.get('faq_channel_id')
            if not faq_channel_id:
                await ctx.send("❌ No FAQ channel ID found in config.json")
                return
            
            faq_channel = ctx.guild.get_channel(faq_channel_id)
            if not faq_channel:
                await ctx.send(f"❌ Could not find FAQ channel with ID {faq_channel_id}")
                return
            
            # Create comprehensive FAQ embed
            embed = discord.Embed(
                title="❓ Frequently Asked Questions",
                description="Here are answers to commonly asked questions about our community.",
                color=discord.Color.purple()
            )
            
            embed.add_field(
                name="Q: What version is the server running?",
                value="A: Minecraft Java Edition 1.21.8",
                inline=False
            )
            
            embed.add_field(
                name="⏱️ How long does the application take?",
                value="The application process takes about 2-3 minutes to complete. You can cancel anytime by typing `cancel` during the process.",
                inline=False
            )
            
            embed.add_field(
                name="📋 Are Griefing, Exploiting and PVP allowed?",
                value="Exploiting is not allowed whatsoever. PVP is not only allowed but it is encouraged CHECK THE PVP RULES BEFORE ENGAGING. We have a complex system when it comes to griefing. Read the rule section for clarification.",
                inline=False
            )
            
            embed.add_field(
                name="⏰ How long does review take?",
                value="Applications are typically reviewed within 24 hours. You'll be notified via DM once your application is reviewed.",
                inline=False
            )
            
            embed.add_field(
                name="🎮 Can I create a new Cult",
                value=" Yes you are encouraged to create a new cult and go to war with other cults.",
                inline=False
            )
            
            embed.add_field(
                name="❌ How do I claim an area",
                value="You can claim an area by posting the coords in the claims discord channel.",
                inline=False
            )
            
            embed.add_field(
                name="🛡️ What are the rules?",
                value="Check the rules channel for our complete community guidelines. The main rules are: be respectful, no harassment, follow Discord ToS, and be active in the community.",
                inline=False
            )
            
            embed.add_field(
                name="📞 Need help?",
                value="If you have questions not answered here, feel free to ask in the general chat or contact a staff member directly.",
                inline=False
            )
            
            embed.set_footer(text="This FAQ will be updated regularly. Check back for new questions and answers!")
            embed.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else None)
            
            await faq_channel.send(embed=embed)
            await ctx.send("✅ FAQ posted successfully!")
            
        except Exception as e:
            await ctx.send(f"❌ Error posting FAQ: {e}")
            print(f"Error posting FAQ: {e}")

async def setup(bot):
    await bot.add_cog(FAQ(bot)) 