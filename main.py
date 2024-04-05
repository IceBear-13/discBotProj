import settings
from weather import get_weather
from discord import app_commands
import discord
from discord.ext import commands
import generateimage

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    
    bot = commands.Bot(command_prefix = "!", intents=intents)

    
    @bot.event
    async def on_ready():
        print(f'{bot.user} makan kontol')
            
    @bot.command()
    async def sync(ctx: commands.Context):
        await ctx.send('Syncing')
        await bot.tree.sync()
        await ctx.send('Done')
        
    @bot.command()
    async def ping(ctx):
        await ctx.send("pong")
    
    @bot.tree.command(name = "hello")
    async def hello(interaction: discord.Interaction):
        await interaction.response.send_message(f"Hey {interaction.user.mention}!")
    
    @bot.tree.command(name = "say")
    @app_commands.describe(thing_to_say = "What should I say?")
    async def say(interaction: discord.Interaction, thing_to_say: str):
        await interaction.response.send_message(f"{thing_to_say}")
        
    @bot.tree.command(name = "weather")
    @app_commands.describe(country = "Which country's weather would you like to know?")
    async def weather(interaction: discord.Interaction, country: str):
        await interaction.response.send_message(f'{get_weather(country)} in celsius ofc')
    
    @bot.tree.command(name = "image")
    @app_commands.describe(prompt = "What kind of image would you like to see?")
    async def weather(interaction: discord.Interaction, prompt: str):
        await interaction.response.send_message(f'{generateimage.get_random(prompt)}')
    
    bot.run(settings.DISCORD_API_SECRET)

if __name__ == "__main__":
    run()