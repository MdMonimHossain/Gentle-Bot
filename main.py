import discord
import os
import class_routine as cr
import days_of_the_week as dotw

client = discord.Client()

routine_commands = '-c sunday, monday,...\n-c sun, mon,...\n-c today, ajk\n-c tomorrow, kalk\n-c 10 6, 11 6,...(day[space]month)'


@client.event
async def on_ready():
	print('{0.user} is connected to discord!'.format(client))
	await client.change_presence(activity=discord.Activity(
	    type=discord.ActivityType.listening, name="Type -help for commands"))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("-hello"):
    await message.channel.send('Hello, ' + message.author.name + '!')
    
  if message.content.startswith("-help"):
    embeded_msg = discord.Embed(title='BOT Commands', description=None)
    embeded_msg.add_field(name='Class Routine', value=routine_commands)
    await message.channel.send(content='Hope it helps, ' + message.author.name + '!', embed=embeded_msg)
    
  if message.content.startswith("-day"):
    msg = message.content.split("-day ", 1)[1]
    await message.channel.send(dotw.days[dotw.get_day_int(msg)])
  
  if message.content.startswith("-c"):
    msg = message.content.split("-c ", 1)[1]
    if message.author.guild.name == 'B Section - Integer\'43':
      roles = []
      for i in message.author.roles:
        roles.append(str(i))
      if 'B1' in roles:
        if dotw.get_week_int(msg) % 2 == 0:
          class_time = cr.classTime2B1[dotw.get_day_int(msg)]
        else:
          class_time = cr.classTime1B1[dotw.get_day_int(msg)]
        embeded_msg = discord.Embed(title=dotw.days[dotw.get_day_int(msg)] + '(B1)', description=class_time)
      else:
        if dotw.get_week_int(msg) % 2 == 0:
          class_time = cr.classTime2B2[dotw.get_day_int(msg)]
        else:
          class_time = cr.classTime1B2[dotw.get_day_int(msg)]
        embeded_msg = discord.Embed(title=dotw.days[dotw.get_day_int(msg)] + '(B2)', description=class_time)
    else:
      if dotw.get_week_int(msg) % 2 == 0:
        class_time = cr.classTime2B1[dotw.get_day_int(msg)]
      else:
        class_time = cr.classTime1B1[dotw.get_day_int(msg)]
      embeded_msg = discord.Embed(title=dotw.days[dotw.get_day_int(msg)], description=class_time)
    
    await message.channel.send(content='Here you go, ' + message.author.name + '!', embed=embeded_msg)
    

client.run(os.environ.get('TOKEN'))