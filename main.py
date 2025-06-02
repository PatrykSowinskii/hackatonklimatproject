import discord
from discord.ext import commands
import random


intents = discord.Intents.default()
intents.message_content = True


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Lista ciekawostek ekologicznych
eco_facts = [
    "Recykling jednej puszki aluminiowej oszczędza energię potrzebną do zasilenia telewizora przez 3 godziny.",
    "Drzewa mogą obniżać temperaturę powietrza nawet o 8°C w ich cieniu.",
    "Szklana butelka rozkłada się nawet 4000 lat.",
    "Każdego roku zużywamy ponad 1 bilion plastikowych toreb.",
    "Oszczędzając wodę podczas mycia zębów, możesz zaoszczędzić 12 litrów dziennie!"
]

# Lista prostych porad ekologicznych
eco_tips = [
    "Używaj torby wielokrotnego użytku 🛍️",
    "Unikaj plastikowych sztućców 🍴",
    "Gaś światło, gdy wychodzisz z pokoju 💡",
    "Jedź rowerem zamiast samochodem 🚴",
    "Pij wodę z kranu zamiast kupować butelkowaną 💧"
]

# Lista pytań i odpowiedzi do quizu
eco_quiz = [
    {"pytanie": "Ile lat rozkłada się plastikowa butelka?", "odpowiedź": "450"},
    {"pytanie": "Jakiego koloru pojemnik służy do papieru?", "odpowiedź": "niebieski"},
    {"pytanie": "Jakim transportem najlepiej dojechać ekologicznie?", "odpowiedź": "rower"},
]

# Słownik do przechowywania punktów użytkowników
user_points = {}

# Funkcja wywoływana, gdy bot zostanie uruchomiony i połączy się z Discordem
@bot.event
async def on_ready():
    print(f'🌍 Bot ekologiczny zalogowany jako {bot.user}!')

# Komenda: losowa ciekawostka ekologiczna
@bot.command(name='fakt')
async def fakt(ctx):
    fact = random.choice(eco_facts)
    await ctx.send(f'🌿 {fact}')

# Komenda: przypomnienie o prostych czynnościach proekologicznych
@bot.command(name='przypomnij')
async def przypomnij(ctx):
    await ctx.send("🔔 Pamiętaj, żeby dziś:\n- Wyrzucać śmieci do odpowiednich pojemników ♻️\n- Oszczędzać wodę 🚿\n- Zabrać torbę wielokrotnego użytku 🛍️")

# Komenda: losowa porada ekologiczna
@bot.command(name='porada')
async def porada(ctx):
    tip = random.choice(eco_tips)
    await ctx.send(f'💡 Porada: {tip}')

# Komenda: quiz ekologiczny – użytkownik odpowiada na pytanie
@bot.command(name='quiz')
async def quiz(ctx):
    # Wybierz losowe pytanie z listy
    question = random.choice(eco_quiz)
    await ctx.send(f"🧠 Quiz: {question['pytanie']}")

    # Funkcja pomocnicza: sprawdza, czy odpowiedź pochodzi od tego samego użytkownika
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        # Czekaj na odpowiedź użytkownika przez maksymalnie 15 sekund
        msg = await bot.wait_for('message', timeout=15.0, check=check)

        # Sprawdź, czy odpowiedź jest poprawna
        if msg.content.lower().strip() == question['odpowiedź'].lower():
            # Zwiększ punktację użytkownika
            user_points[ctx.author.name] = user_points.get(ctx.author.name, 0) + 1
            await ctx.send(f"✅ Dobrze, {ctx.author.name}! Masz {user_points[ctx.author.name]} punkt(ów).")
        else:
            await ctx.send(f"❌ Zła odpowiedź. Prawidłowa: {question['odpowiedź']}")
    except:
        # Obsługa przypadku, gdy użytkownik nie odpowie na czas
        await ctx.send("⏰ Czas minął! Spróbuj ponownie.")

# Komenda: ranking użytkowników – pokazuje top eko-uczestników quizów
@bot.command(name='ranking')
async def ranking(ctx):
    if not user_points:
        await ctx.send("📊 Nikt jeszcze nie zdobył punktów.")
        return

    # Posortuj użytkowników wg liczby punktów
    sorted_points = sorted(user_points.items(), key=lambda x: x[1], reverse=True)

    # Stwórz czytelną listę rankingową
    ranking_text = '\n'.join([f"{i+1}. {user} – {points} punktów" for i, (user, points) in enumerate(sorted_points)])

    await ctx.send(f"🏆 Ranking ekologów:\n{ranking_text}")

# Komenda: wyświetla listę dostępnych komend
@bot.command(name='pomoc')
async def pomoc(ctx):
    await ctx.send("""
🌱 **Komendy bota ekologicznego**:
!fakt – ciekawostka ekologiczna  
!przypomnij – przypomnienie o eko-zachowaniach  
!porada – losowa porada ekologiczna  
!quiz – quiz ekologiczny  
!ranking – ranking użytkowników z punktami  
!pomoc – pokazuje tę listę
""")

bot.run('TU_WSTAW_TOKEN_BOTA')
