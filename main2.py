from discord.ext import commands
import discord, random, datetime 
from datetime import datetime 
from typing import Union, Optional
import copy
import asyncio

bot = commands.Bot(command_prefix="z.", status=discord.Status.idle, activity=discord.Game(name="use z.help"))
token = "NTQ5MzI0NTg1MTU0MjQ4NzIw.XRa6Yw.ygALh3zry0DSD7YDOrPvngSOcvM"

@bot.event
async def on_ready():
	print("bot is on wowza") 

async def on_message(message):
	if message.content == "zen" or message.content == "🇿 🇪 🇳" or message.content == f"<@!549324585154248720>" or message.content == f"<@549324585154248720>" or message.content == "Zen" or message.content == "ZEN":
		await message.channel.send(f"sup bois. my prefix is `z.` and if you wanna see ma commands do `z.help`! epic. awesome....\n\n\n\n\n\n\n\n\n\n\n\n\nbye")
		return


#@bot.command(aliases=['8ball', 'eightball', 'eight_ball'])
#async def ball8(ctx, *, question):
	#"""ask the 8ball a question!"""
	#await ctx.trigger_typing()

	#responses = 

@bot.command(aliases=['mention', 'flood', 'L', 'l', 'eL'])
@commands.has_any_role("Zeniath", "Noir")
async def spam(ctx, user: discord.Member, number: int, *, say=None):
	"""spam someone with the letter L"""
	u = user.mention

	if say is None:
		say = f"L, {u}"
	else:
		say = f"{say}, L, {u}"

	def check(message):
		return message.author.id == user.id

	await ctx.send(f"{u} will be L'ed for the next {number} times they type in the chat\n\n\n\n\nL")

	for i in range(number):
		msg = await bot.wait_for('message', check=check)
		loop = number - 1
		await ctx.send(f"{say} ({loop} more to go)")
		try:
			await user.send(f"{say} ({loop} more to go)")
		except Exception as e:
			print(f'There was an error running this command; {str(e)}') #if error

	await asyncio.sleep(1)
	await ctx.send(f"i apologise... at least that's over now :)\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n1 more HEHE\n{say}")
	try:
		await user.send(f"i apologise... at least that's over now :)\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n1 more HEHE\n{say}")
	except Exception as e:
		print(f'There was an error running this command; {str(e)}') #if error


#@bot.command()
#async def slowmode(ctx, channel: discord.Channel=None)

@bot.command(aliases=['dos'])
async def ddos(ctx, user: discord.Member, *, ip=None):
	"""ddos someone"""
	if user == ctx.author:
		await ctx.send("imagine tryna ddos yourself lmfao can't be me...")
	try:
		if ip is None:
			await ctx.send("maybe wanna put an ip in chat idk??? bit of a clappy 👏")
		else:
			await ctx.send(f"You have successfully DDOSed {user.mention} with the ip {ip}!")
	except Exception as e:
		print(f'There was an error running this command; {str(e)}') #if error

@bot.command(aliases=['cookie'])
async def cookies(ctx, user: discord.Member, *, whispers=None):
	"""give a cookie to someone"""
	try:
		if whispers is None:
			await ctx.send(f"*{ctx.author.mention} passes {user.mention} a 🍪*")
		else:
			await ctx.send(f"*{ctx.author.mention} passes {user.mention} a 🍪 and whispers {whispers}*")
	except Exception as e:
		await ctx.send(f'There was an error running this command; {str(e)}') #if error


@bot.command()
async def poll(ctx, *, question=None):
	"""ask the community a question"""
	try:
		if question is None:
			await ctx.send("might wanna like... maybe... ask a question? ever thought of that u dumbass?")
		else:
			await ctx.message.delete()
			message = await ctx.send(question)
			await message.add_reaction("👍")
			await message.add_reaction("👎")
	except Exception as e:
		await ctx.send(f'There was an error running this command; {str(e)}') #if error

@bot.command()
@commands.has_any_role("Zeniath")
async def zen(ctx, user: discord.Member=None):
	"""give someone the zeniath role"""
	role = "Zeniath"
	non = "non"
	u = user.mention

	if user is None:
		user = await ctx.send("oi mate, mention a member eh?")

	if non in [r.name for r in user.roles]:
		await user.remove_roles(discord.utils.get(user.guild.roles, name=non))

	def check(message):
		return message.author.id == ctx.author.id

	if role in [r.name for r in user.roles]:
		await ctx.send(f"""because {u} already has the role {role}, i will ask you whether you would like to remove it or keep it! :)\n\n"""
			f"""if you would like {u} to keep their role please type "keep" and if you would like to remove it type "remove" """)
		msg = await ctx.bot.wait_for('message', check=check)

		if msg.content == "keep":
			await ctx.send(f"alright, {u} will keep their {role} role :3")
			return
		if msg.content == "remove":
			await ctx.send(f"damn, F in the chat for {u}, they lost their {role} role :/")
			await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
			return

	else:
		try:
			await user.add_roles(discord.utils.get(user.guild.roles, name=role))
		except Exception as e:
			await ctx.send(f'There was an error running this command; {str(e)}') #if error
		else:
			await ctx.send(f"you are now __***zenified***__, {u}")


@bot.command()
@commands.has_any_role("Zeniath", "Noir", "Turbo", "Adem")
async def mod(ctx, user: discord.Member=None):
	"""give someone the mod role"""
	role = "Mod"
	non = "non"
	u = user.mention

	if user is None:
		user = await ctx.send("oi mate, mention a member eh?")

	if non in [r.name for r in user.roles]:
		await user.remove_roles(discord.utils.get(user.guild.roles, name=non))

	def check(message):
		return message.author.id == ctx.author.id

	if role in [r.name for r in user.roles]:
		await ctx.send(f"""because {u} already has the role {role}, i will ask you whether you would like to remove it or keep it! :)\n\n"""
			f"""if you would like {u} to keep their role please type "keep" and if you would like to remove it type "remove" """)
		msg = await ctx.bot.wait_for('message', check=check)

		if msg.content == "keep":
			await ctx.send(f"alright, {u} will keep their {role} role :3")
			return
		if msg.content == "remove":
			await ctx.send(f"damn, F in the chat for {u}, they lost their {role} role :/")
			await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
			return

	else:
		try:
			await user.add_roles(discord.utils.get(user.guild.roles, name=role))
		except Exception as e:
			await ctx.send(f'There was an error running this command; {str(e)}') #if error
		else:
			await ctx.send(f"you are now __***moderatorfied***__, {u}")

@bot.command()
@commands.has_any_role("Zeniath", "Noir", "Turbo", "Adem")
async def random(ctx, user: discord.Member=None):
	"""give someone the random role"""
	role = "Random"
	u = user.mention
	non = "non"

	if user is None:
		user = await ctx.send("oi mate, mention a member eh?")

	if non in [r.name for r in user.roles]:
		await user.remove_roles(discord.utils.get(user.guild.roles, name=non))

	def check(message):
		return message.author.id == ctx.author.id

	if role in [r.name for r in user.roles]:
		await ctx.send(f"""because {u} already has the role {role}, i will ask you whether you would like to remove it or keep it! :)\n\n"""
			f"""if you would like {u} to keep their role please type "keep" and if you would like to remove it type "remove" """)
		msg = await ctx.bot.wait_for('message', check=check)

		if msg.content == "keep":
			await ctx.send(f"alright, {u} will keep their {role} role :3")
			return
		if msg.content == "remove":
			await ctx.send(f"damn, F in the chat for {u}, they lost their {role} role :/")
			await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
			return

	else:
		try:
			await user.add_roles(discord.utils.get(user.guild.roles, name=role))
		except Exception as e:
			await ctx.send(f'There was an error running this command; {str(e)}') #if error
		else:
			await ctx.send(f"you are now __***randomaratorfied***__, {u}")

@bot.command()
@commands.has_any_role("Zeniath", "Noir", "Turbo", "Adem")
async def dj(ctx, user: discord.Member=None):
	"""give someone the dj role"""
	role = "DJ"
	u = user.mention
	non = "non"

	if user is None:
		user = await ctx.send("oi mate, mention a member eh?")

	def check(message):
		return message.author.id == ctx.author.id

	if non in [r.name for r in user.roles]:
		await user.remove_roles(discord.utils.get(user.guild.roles, name=non))

	if role in [r.name for r in user.roles]:
		await ctx.send(f"""because {u} already has the role {role}, i will ask you whether you would like to remove it or keep it! :)\n\n"""
			f"""if you would like {u} to keep their role please type"keep" and if you would like to remove it type "remove" """)
		msg = await ctx.bot.wait_for('message', check=check)

		if msg.content == "keep":
			await ctx.send(f"alright, {u} will keep their {role} role :3")
			return
		if msg.content == "remove":
			await ctx.send(f"damn, F in the chat for {u}, they lost their {role} role :/")
			await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
			return

	else:
		try:
			await user.add_roles(discord.utils.get(user.guild.roles, name=role))
		except Exception as e:
			await ctx.send(f'There was an error running this command; {str(e)}') #if error
		else:
			await ctx.send(f"you are now __***djafied***__, {u}")


@bot.command()
@commands.has_any_role("Zeniath", "Noir", "Turbo", "Adem")
async def say(ctx, *, message):
	"""make the bot say anything you want"""
	await ctx.send(message)
	await ctx.message.delete()


@bot.command(aliases=['die'])
@commands.is_owner()
async def kill(ctx):
	"""i think it's kind of obvious... incase you don't know, it kills the bot!"""
	await ctx.send("what a dick... okay bye")
	await ctx.bot.logout()

@bot.command(aliases=['pfp'])
async def avatar(ctx, *, user: discord.User=None):
	"""displays the users avatar"""
	if user is None:
		user = ctx.author

	e = discord.Embed(colour=discord.Colour.gold())
	e.set_image(url=user.avatar_url)
	await ctx.send(embed=e)

@bot.command(aliases=['server_members', 'users'])
async def members(ctx):
	"""displays the amount of members in zeniath's discord server"""
	guild = discord.Guild
	await ctx.send(f"There are currently **{len(guild.members)}** members in **{guild}**.")

@bot.command(aliases=['user'])
async def userinfo(ctx, *, user: discord.Member=None):
	"""displays information about a member"""
	if user is None:
		user = ctx.author

	roles = [role.mention for role in user.roles if not role.is_default()]

	voice = user.voice
	if voice is not None:
		vc = voice.channel
		other_people = len(vc.members) - 1
		voice = f'In {vc.name} with {other_people} other(s)' if other_people else f'In {vc.name} all by themselves'
	else:
		voice = 'Not connected'

	pos = sorted(ctx.guild.members, key=lambda m: m.joined_at).index(user)+1

	e = discord.Embed(color=user.color)
	e.set_thumbnail(url=user.avatar_url)
	e.add_field(name='User:', value=f"{user}")
	e.add_field(name='User ID:', value=f"{user.id}")
	e.add_field(name='Status:', value=f"{user.status}".title())
	e.add_field(name='Join Position:', value=f"#{pos}")
	e.add_field(name='Created at:', value=f"{user.created_at.strftime('%b %d, %Y')}")
	e.add_field(name='Joined server at:', value=f"{user.joined_at.strftime('%b %d, %Y')}")
	e.add_field(name='Voice:', value=f"{voice}")
	e.add_field(name=f'Roles: ({len(roles)})', value=f"{chr(173)}{', '.join(roles)}" if len(roles) < 15 else f"{len(roles)} Roles")
	await ctx.send(embed=e)

bot.run(token)