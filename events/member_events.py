import discord
from discord.ext import commands
import json

class MemberEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        # Load config
        try:
            with open('config.json', 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = {}

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Automatically assign applicant role to new members"""
        try:
            # Get the applicant role ID from config
            applicant_role_id = self.config.get('applicant_role_id')
            if not applicant_role_id:
                print("Warning: No applicant_role_id found in config.json")
                return
            
            # Get the role object
            applicant_role = member.guild.get_role(applicant_role_id)
            if not applicant_role:
                print(f"Warning: Could not find role with ID {applicant_role_id}")
                return
            
            # Assign the role to the new member
            await member.add_roles(applicant_role)
            print(f"✅ Assigned applicant role to {member.display_name} ({member.id})")
            
            # Send application instructions to the application channel
            try:
                application_channel_id = self.config.get('application_channel_id')
                if application_channel_id:
                    application_channel = member.guild.get_channel(application_channel_id)
                    if application_channel:
                        embed = discord.Embed(
                            title="🎉 New Member Joined!",
                            description=f"Welcome {member.mention} to our cult community!",
                            color=discord.Color.blue()
                        )
                        embed.add_field(
                            name="📝 How to Apply", 
                            value="To join our cult, please use the command:\n\n**`!apply`**\n\nThis will start the application process where you'll answer a few questions about yourself and your experience.", 
                            inline=False
                        )
                        embed.add_field(
                            name="ℹ️ What to Expect",
                            value="• You'll be asked about your Minecraft username\n• Questions about your gaming experience\n• Why you want to join our community\n• Your agreement to follow server rules",
                            inline=False
                        )
                        embed.add_field(
                            name="⏱️ Process Time",
                            value="The application takes about 2-3 minutes to complete. You can cancel anytime by typing `cancel`.",
                            inline=False
                        )
                        embed.set_footer(text="We're excited to review your application!")
                        await application_channel.send(embed=embed)
            except Exception as e:
                print(f"Could not send application instructions: {e}")
                
        except Exception as e:
            print(f"Error assigning applicant role to {member.display_name}: {e}")

async def setup(bot):
    await bot.add_cog(MemberEvents(bot)) 