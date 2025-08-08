import discord
from discord.ext import commands
from datetime import datetime
import json
from utils.database import submit_application, get_pending_applications

class Applications(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        # Load config
        try:
            with open('config.json', 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = {
                "application_questions": [
                    "What is your Minecraft username?",
                    "How old are you?",
                    "How long have you been playing Minecraft?",
                    "What type of player are you? (Builder, Redstone, PvP, etc.)",
                    "Why do you want to join our server?",
                    "Do you have any experience with other Minecraft servers?",
                ]
            }

    @commands.command(name='apply')
    async def apply_command(self, ctx):
        """Show the application questions"""
        embed = discord.Embed(
            title="📝 Cult Application",
            description="Please answer all the questions below in your response. Copy and paste the questions, then add your answers after each one.",
            color=discord.Color.blue()
        )
        
        # Add all questions to the embed
        questions_text = ""
        for i, question in enumerate(self.config['application_questions'], 1):
            questions_text += f"**{i}. {question}**\n\n"
        
        embed.add_field(
            name="📋 Application Questions",
            value=questions_text,
            inline=False
        )
        
        embed.add_field(
            name="📝 How to Apply",
            value="1. Copy all the questions above\n2. Paste them in a new message\n3. Add your answer after each question\n4. Send your completed application",
            inline=False
        )
        
        embed.add_field(
            name="⏱️ Time Limit",
            value="You have 30 minutes to complete your application. Make sure to answer all questions thoroughly!",
            inline=False
        )
        
        embed.set_footer(text="Example: 1. What is your Minecraft username? Answer: MyUsername")
        
        await ctx.send(embed=embed)

    @commands.command(name='applications')
    async def applications_command(self, ctx):
        """List pending applications (admin only)"""
        if not ctx.author.guild_permissions.administrator:
            await ctx.send("❌ You don't have permission to view applications.")
            return
        
        applications = get_pending_applications()
        
        if not applications:
            await ctx.send("No pending applications.")
            return
        
        embed = discord.Embed(
            title="Pending Applications",
            description=f"Found {len(applications)} pending application(s)",
            color=discord.Color.blue()
        )
        
        for app in applications[:5]:  # Show first 5
            embed.add_field(
                name=f"Application #{app[0]}",
                value=f"**User:** {app[3]}\n**Minecraft:** {app[2]}\n**Submitted:** {app[5]}",
                inline=True
            )
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Applications(bot)) 
