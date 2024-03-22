import discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi, want to know about global warming?")
    elif message.content.startswith('$yes'):
        await message.channel.send("Global warming is the long-term warming of the planet’s overall temperature. Though this warming trend has been going on for a long time, its pace has significantly increased in the last hundred years due to the burning of fossil fuels. As the human population has increased, so has the volume of fossil fuels burned. Fossil fuels include coal, oil, and natural gas, and burning them causes what is known as the “greenhouse effect” in Earth’s atmosphere. anything else? (say: ye)")
    elif message.content.startswith('$ye'):
        await message.channel.send("The greenhouse effect is when the sun’s rays penetrate the atmosphere, but when that heat is reflected off the surface cannot escape back into space. Gases produced by the burning of fossil fuels prevent the heat from leaving the atmosphere. These greenhouse gasses are carbon dioxide, chlorofluorocarbons, water vapor, methane, and nitrous oxide. The excess heat in the atmosphere has caused the average global temperature to rise overtime, otherwise known as global warming. Global warming has presented another issue called climate change. Sometimes these phrases are used interchangeably, however, they are different. Climate change refers to changes in weather patterns and growing seasons around the world. It also refers to sea level rise caused by the expansion of warmer seas and melting ice sheets and glaciers. Global warming causes climate change, which poses a serious threat to life on Earth in the forms of widespread flooding and extreme weather. Scientists continue to study global warming and its impact on Earth.")
    elif message.content.startswith('$no'):
        await message.channel.send("ok then, bye")
    else:
        await message.channel.send("XDD")
client.run("aqui debe ir tu tocken")
