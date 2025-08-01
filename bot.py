import os
import sys

# Add this before importing discord to avoid audioop issues
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

try:
    import discord
    from discord.ext import commands
except ImportError as e:
    print(f"Error importing discord: {e}")
    print("Try installing discord.py: pip install discord.py==2.3.2")
    sys.exit(1)

from utils.database import init_db

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    """Called when the bot is ready"""
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is in {len(bot.guilds)} guild(s)')
    try:
        await bot.change_presence(activity=discord.Game(name="Cult Bot"))
    except:
        print("Could not set presence (voice features disabled)")

@bot.event
async def on_command_error(ctx, error):
    """Handle command errors"""
    if isinstance(error, commands.CommandNotFound):
        pass  # Ignore command not found
    else:
        print(f"Error: {error}")

async def load_extensions():
    """Load all cogs and events"""
    # Load cogs
    await bot.load_extension("cogs.applications")
    await bot.load_extension("cogs.admin")
    await bot.load_extension("cogs.rules")
    await bot.load_extension("cogs.faq")
    await bot.load_extension("cogs.join_info")
    
    # Load events
    await bot.load_extension("events.member_events")
    
    print("✅ All extensions loaded successfully!")

# Initialize database and run bot
if __name__ == "__main__":
    print("Initializing database...")
    init_db()
    
    # Get token
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        try:
            with open('token.txt', 'r') as f:
                token = f.read().strip()
        except FileNotFoundError:
            print("❌ No Discord token found!")
            print("Create a file called 'token.txt' with your bot token on the first line")
            exit(1)
    
    print("Starting Cult Bot...")
    
    # Load extensions and run
    async def main():
        await load_extensions()
        await bot.start(token)
    
    import asyncio
    asyncio.run(main()) 