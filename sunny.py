import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.guilds = True
# intents.members = True

load_dotenv()
TOKEN = os.getenv("TOKEN")

client = commands.Bot(command_prefix="?", intents=intents)


# Check if author is bot owner
def is_it_me(user):
    return user.id == 747361529896239134


invite_url = "https://discord.com/oauth2/authorize?client_id=1377861594356252782&permissions=962073054272&integration_type=0&scope=bot"

# Affirmations
affirmations = [
    "You're the sparkle in the void of the group chat.",
    "You have survived every awkward moment so far. Champion behavior.",
    "Your vibes? Immaculate.",
    "You radiate excellence, chaos, and unmatched energy.",
    "You make existing look cool.",
    "You're basically a walking serotonin dispenser.",
    "You're thriving. The bar is low, but still—you're killing it.",
    "Even your shadow is proud of you.",
    "You are not annoying. You're just passionate, and that’s powerful.",
    "There is no one else like you—and that's your weapon.",
    "You’re a limited edition. Print error? Maybe. But rare.",
    "If overthinking was an Olympic sport, you'd still win gold and deserve it.",
    "You're not behind. You're brewing brilliance at your own pace.",
    "You're not extra. You're the main course.",
    "You’re chaotic good and that’s exactly what this world needs.",
    "Your inner child is fist-bumping you right now.",
    "Being weird is your legacy. Own it.",
    "You're the plot twist in someone’s boring Tuesday.",
    "You have more power than your phone battery at 1%.",
    "If life is a video game, you're already a legendary skin.",
    "Your brain is not broken—it's just playing 4D chess.",
    "You’re not lost. You’re on an epic side quest.",
    "You're made of stardust, caffeine, and 'I got this'.",
    "You're the perfect mix of disaster and delight.",
    "You're not the villain. You're the misunderstood icon.",
    "You’re not lazy—you’re recharging your emotional WiFi.",
    "You're a masterpiece in progress. Bold brushstrokes only.",
    "You're the reason someone smiles at their screen today.",
    "You don’t need fixing. You need more snacks and compliments.",
    "You're a soft chaos storm and I respect that.",
    "You’re proof that being yourself is the best flex.",
    "Your existence breaks boring algorithms. Keep being unpredictable.",
    "Even when you’re doubting yourself, you’re still a whole vibe.",
    "You have permission to romanticize your recovery arc.",
    "You're not too sensitive—you’re emotionally advanced.",
    "You are not small. You’re just zoomed out.",
    "You're magic that forgot it was magic. Surprise!",
    "You deserve the peace you keep giving to others.",
    "You're not procrastinating—you're prioritizing rest in disguise.",
    "You are beautifully unfinished. Keep going.",
    "You're a symphony of silly and sacred.",
    "You’re the unexpected brilliance in a routine scroll.",
    "You're doing amazing, sweetie!",
    "Keep shining like the chaotic gremlin you are!",
    "You're not a mess—you're limited edition!",
    "You survived 100% of your worst days. Iconic behavior.",
    "You are valid. Even if you forgot to eat lunch again.",
    "Reminder: Your brain is sexy. Probably.",
    "Asking for help is a sign of self-respect and self-awareness.",
    "I alone hold the truth of who I am.",
    "I am allowed to ask for what I want and what I need.",
    "I am allowed to feel good.",
    "I am capable of balancing ease and effort in my life.",
    "I am in charge of how I feel and I choose to feel happy.",
    "I am loved and worthy.",
    "I am optimistic because today is a new day.",
    "I can be soft in my heart and firm in my boundaries.",
    "I can control how I respond to things that are confronting.",
    "I do all things in love.",
    "You are the main character and this is your comeback arc.",
    "You radiate chaotic good energy, and we love that.",
    "You are not too much; you were never too much.",
    "Your weirdness is your superpower.",
    "Your presence is a present.",
    "You're not failing, you're evolving.",
    "Messy progress is still progress.",
    "It’s okay to rest. You’re not a robot (yet).",
    "Growth looks different on everyone. You’re doing fine.",
    "Existing is enough. Thriving is a bonus.",
    "Your voice matters, even if it shakes.",
    "You're allowed to take up space.",
    "You don’t need to be perfect to be lovable.",
    "Your feelings are valid, even the silly ones.",
    "You’re built different—in the best way.",
    "You’ve got that main quest energy.",
    "One step at a time is still a whole journey.",
    "You don’t need permission to be proud of yourself.",
    "You're stronger than yesterday’s version of you.",
    "Being you is your superpower.",
    "Every awkward moment is just character development.",
    "You are not behind. You're on your own path.",
    "Resting is radical. Do it unapologetically.",
    "You’re the plot twist nobody saw coming.",
    "You're the easter egg in someone’s otherwise normal day.",
    "You don't need to be perfect—you’re already real, and that’s better.",
    "You’re not a mess. You’re just in beta testing.",
    "You're like a WiFi signal—stronger when you’re around the right people.",
    "You are a walking mood board of greatness.",
    "Your awkwardness is just rare charm in disguise.",
    "You’re the main character even when the plot makes no sense.",
    "Even your typos are endearing.",
    "Your weird is your superpower. Don’t dull it.",
    "You’re doing better than your anxiety tells you.",
    "You’ve got that soft heart, sharp mind combo. Dangerous and divine.",
    "You are more than your productivity. You’re stardust and soul.",
    "You light up the group chat like a disco ball of memes and love.",
    "You’ve grown more than you’ve noticed. That’s magic.",
    "You’re proof that soft and strong can coexist beautifully.",
    "You're a walking playlist of emotional bangers.",
    "You’ve got ancient cosmic energy and snack crumbs on your shirt. Balance.",
    "You are a one-person revolution of healing and humor.",
    "You are not 'too much'—they were just not enough.",
    "You have the audacity of a cat walking on a laptop. Iconic.",
    "Your chaos is part of your aesthetic.",
    "You’ve got that ‘just showed up and still slayed’ energy.",
    "You are not broken. You're just under divine construction.",
    "You make existing more interesting for others just by being here.",
    "Your feelings are real. Your courage is louder.",
    "You’re emotionally bilingual: fluent in memes and meaning.",
    "You’re like WiFi in a forest—rare, valuable, and worth the hunt.",
    "You’ve survived 100% of your overthinking episodes. You win.",
    "You're basically caffeine for the soul.",
    "You're made of galaxies and a little bit of 'oops'.",
    "You’re the kind of tired that only legends get after quests.",
    "Your future self is already proud of you.",
    "Your mind is loud, but your presence is peace.",
    "You’re the poetry behind someone’s favorite memory.",
    "You have main-character healing arcs. Embrace it.",
    "You’re a unicorn in a world that settles for horses.",
    "You exist like plot armor—surprisingly essential.",
    "You’re not failing. You’re fermenting into something legendary."
]


# goofy lines ------------------------------------------------------
"""
IDs:
aashirwad = 395923336443723777
aashwin = 486761188609228811
aleena = 849305173339799582
ashwin = 449096139573035009
christine = 1219277340517990433
hafsa = 557589868314886144
karan = 666648289307000832
sulaimaan = 900249978470019082
me = 747361529896239134
"""

# Dictionary mapping user IDs to custom goofy lines
user_goofy_lines = {

    # aashirwad
    395923336443723777: [
        " entered like a mysterious NPC with maxed-out stats",
        " has joined, one of the biggest god complexes",
        " the heavenly tech support has arrived 🎧",
        " from heaven has dropped to grace us 🧚🏻‍♂️",
        " has spwaned in . . . did someone mention his name?"
    ],

    # aashwin
    486761188609228811: [
        " the server jester has arrived! :tada:",
        " the rookie with . . . skills, iykyk :smirk:",
        " the man who never pay his bills, the rookie with skills!"
    ],

    # aleena
    849305173339799582: [
        " has entered the VC, beware of her sneeze",
        " has joined the call - rarer than Ganyu's banner",
        " has joined - hide your feelings, she aint a therapist"
    ],

    # ashwin
    449096139573035009: [
        ", mister 'i join twice a month'",
        ", the straightest gay male has arrived",
        " the cheating gay has arrived - pick a guy already you can't have all",
        " the male gulab jamun"
    ],

    # christine
    1219277340517990433: [
        " the grandma with her crochet has arrived",
        " has entered, hide your beers!",
        ", did someone mention 'drama'?? the tea gatherer has come"
    ],

    # hafsa
    557589868314886144: [
        " has come to grace your taste buds",
        " the sarcastic fairy queen has arrived 🧚🏻‍♀️",
        " - COME INTO THE UNKNOWN! SCATTER! the Sov-en has come",
        " has come! The E3 demo queen"
    ],

    # karan
    666648289307000832: [
        " entered the VC with Jhol background music",
        " has spawned, be on your best behaviour!", " प्रकट हुऐ हैं"
    ],

    # sulaimaan
    900249978470019082: [
        ", the half sugar daddy", ", chee syed",
        " has spawned in . . . did someone mention his name?",
        " has come for the roll call! All employees round up!",
        " the owner has arrived"
    ],

    # me
    747361529896239134: [
        " the legendary crybaby has entered — kneel, mortals, with tissues please",
        ", the screecher Banshee has arrived! Lower your volumes",
        " the Gryffindor Fat Lady in Portrait has arrived!",
        " has joined, one of the biggest god complexes",
        " has joined, hide your alcohol",
        ", my mom, apni ma ka bura nahi bolte, chee"
    ],
}


exit_lines = [
    " has left the VC, the server is now a ghost town",
    " has gone to take a shit", ", दफा हो गए हैं",
    ", अच्छा चलता हूं दुआओं में याद रखना", ", has rage quit",
    " would have loved to stay and chat but they would need to lower their standards",
    " has ran out of social battery", " has gone to get the milk",
    " has gone to doom scroll", " has been kissed by the Dementors"
]


@client.event
async def on_ready():
    print(f"{client.user} is now online!")


@client.event
async def on_disconnect():
    print("Bot disconnected!")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title="COOLDOWN", color=0xF0AAA6)
        embed.add_field(
            name="You are still on cooldown so hold ya horses mate",
            value="Try again after {:.2f}s".format(error.retry_after),
            inline=False)
        await ctx.channel.send(embed=embed)


@client.command(name="ping", help="checks latency/sped ponging u in ur brain")
async def ping(ctx, arg=None):
    if arg == "pong":
        await ctx.channel.send("🏓 Marvelous u ponged yourself-")
    else:
        await ctx.channel.send(f"🏓 Pong {round(client.latency * 1000)}ms")


@client.command(name="cmd")
async def cmd(ctx, cmds):
    if cmds == "av":
        embed = discord.Embed(title="Avatar", color=0x9BF080)
        embed.add_field(name="Well to see the avatar's of users",value="in big picture",inline=False)
        embed.add_field(name='Use for this cmd:',value="`?av <user>`",inline=False)
        await ctx.channel.send(embed=embed)

    elif cmds == "tag me":
        embed = discord.Embed(title="Tagging me")
        embed.add_field(name="Tag me to get affirmations",value="Let me try to make ur day",inline=False)
        await ctx.channel.send(embed=embed)

    elif cmds == "whois":
        embed = discord.Embed(title="Waaait a minute... Who are you?",color=0x9BF080)
        embed.add_field(name="Wanna know about some user",value="You came to the right place",inline=False)
        embed.add_field(name='Use for this cmd:',value="`?whois <user>`",ine=False)
        await ctx.channel.send(embed=embed)


@client.command(name="aid")
async def aid(ctx):
    embed = discord.Embed(title='Helping your brain here',description='all commands',color=0xAC5436)
    embed.add_field(name='Tag Me', value='tag me to get affirmations')
    embed.add_field(name='Miscellaneous', value='intro', inline=False)
    embed.add_field(name='Fun', value='av, whois', inline=False)
    embed.set_footer(text='if you need more help then use ?cmd <cmd name>')
    await ctx.channel.send(embed=embed)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user in message.mentions:
        affirmation = random.choice(affirmations)
        await message.channel.send(f"{message.author.mention} {affirmation}")

        if is_it_me(
                message.author) and message.content.lower().endswith("dm me"):
            ping_ms = round(client.latency * 1000)
            bot_user = client.user
            bot_member = message.guild.get_member(bot_user.id)

            permissions = bot_member.guild_permissions
            perm_list = [
                f"✅ {perm.replace('_', ' ').title()}"
                for perm, value in permissions if value
            ]
            perm_text = "\n".join(perm_list) or "No permissions found 🤷"

            embed = discord.Embed(title="🤖 Sunny Bot Status", color=0xF4C542)
            embed.add_field(name="Bot Name",value=f"{bot_user.name}#{bot_user.discriminator}",inline=False)
            embed.add_field(name="Bot ID",value=str(bot_user.id),inline=False)
            embed.add_field(name="Ping", value=f"{ping_ms} ms", inline=False)
            embed.add_field(name="Invite Link",value=f"[Click here]({invite_url})",inline=False)
            embed.add_field(name="Server Permissions",value=perm_text[:1024],inline=False)
            embed.set_footer(text="Summoned on mention by the boss 👑")

            try:
                await message.author.send(embed=embed)
            except discord.Forbidden:
                await message.channel.send(
                    "Boss, I couldn't DM you. Maybe your DMs are off? 😢")

    await client.process_commands(message)


@client.event
async def on_voice_state_update(member, before, after):
    # Check if user joined or left the specific VC
    target_vc_id = 1338890681908727839
    send_channel_id = 937845389271371788
    send_channel = member.guild.get_channel(send_channel_id)
    
    if not send_channel:
        return
    
    # User JOINED the VC
    if (before.channel is None or before.channel.id != target_vc_id) and (after.channel and after.channel.id == target_vc_id):
        if member.id in user_goofy_lines:
            user_lines = [
                line for line in user_goofy_lines[member.id] if line.strip()
            ]
            if user_lines:
                line = random.choice(user_lines)
                await send_channel.send(f"🔊 **{member.display_name}**{line}")
    
    # User LEFT the VC
    elif (before.channel and before.channel.id == target_vc_id) and (after.channel is None or after.channel.id != target_vc_id):
        # Use exit lines for users leaving
        exit_line = random.choice(exit_lines)
        await send_channel.send(f"🔇 **{member.display_name}**{exit_line}")

# This line must be at the end of your script
client.run(TOKEN)
