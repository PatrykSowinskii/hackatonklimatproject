import discord
from discord.ext import commands
import random

eco_facts = [
    "♻️ Recykling jednej puszki aluminiowej oszczędza energię potrzebną do zasilania telewizora przez 3 godziny.",
    "🌳 Jedno drzewo może wchłonąć aż 22 kg CO2 rocznie.",
    "💧 Zakręcenie kranu podczas mycia zębów może zaoszczędzić nawet 20 litrów wody dziennie.",
    "🚴‍♀️ Jazda rowerem zamiast samochodem pomaga ograniczyć emisję CO2.",
    "🛍️ Wybierając torbę wielokrotnego użytku, ograniczasz zużycie plastiku."
]

bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'✅ Bot {bot.user} jest online i gotowy do działania!')

@bot.command(name='ekofart')
async def ekofart(ctx):
    fakt = random.choice(eco_facts)
    await ctx.send(f"🌱 **Fakt ekologiczny:** {fakt}")

@bot.command(name='eko')
async def eko(ctx):
    poradnik = (
        "**Jak możesz pomóc planecie? 🌍**\n"
        "- Używaj mniej plastiku.\n"
        "- Oszczędzaj wodę i energię.\n"
        "- Wybieraj transport publiczny lub rower.\n"
        "- Segreguj odpady.\n"
        "- Kupuj lokalne i sezonowe produkty.\n"
        "Drobne zmiany robią wielką różnicę!"
    )
    await ctx.send(poradnik)

@bot.command(name='pomoc')
async def pomoc(ctx):
    await ctx.send(
        "**Dostępne komendy:**\n"
        "`!ekofakt` - losowy fakt ekologiczny 🌿\n"
        "`!eko` - jak możesz dbać o środowisko ♻️\n"
        "`!pomoc` - lista dostępnych komend ℹ️"
    )

bot.run('token')