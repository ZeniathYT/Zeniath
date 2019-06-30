from discord.ext import commands
import discord, random, datetime 
from datetime import datetime 

bot = commands.Bot(command_prefix="z.", status=discord.Status.idle, activity=discord.Game(name="testing..."))
token = "NTQ5MzI0NTg1MTU0MjQ4NzIw.XRa6Yw.ygALh3zry0DSD7YDOrPvngSOcvM"

@bot.event
async def on_ready():
	print("bot is on wowza") 

@bot.command(aliases=['flip'])
async def coinflip(ctx):
	await ctx.trigger_typing()
	number = random.randint(1,2)

	if number == 1:
		await ctx.send("You flipped the coin. It landed on **tails**")
	else:
		await ctx.send("You flipped the coin. It landed on **heads**")


#@bot.command(aliases=['8ball', 'eightball', 'eight_ball'])
#async def ball8(ctx, *, question):
	#"""ask the 8ball a question!"""
	#await ctx.trigger_typing()

@bot.command()
@commands.has_any_role("Zeniath", "Noir")
async def l(ctx, number: int, user: discord.Member=None):
	"""spam someone with the letter L"""
	if user is None:
		for i in range(number):
			await ctx.send("L")

	else:
		for i in range(number):
			await ctx.send(f"L, {user.mention}")

@bot.command()
@commands.has_any_role("Zeniath")
async def zen(ctx, user: discord.Member=None):
	"""give someone the zeniath role"""
	role = "Zeniath"

	if user is None:
		user = await ctx.send("oi mate, mention a member eh?")

	if role in [r.name for r in user.roles]:
		await ctx.send(f"because {user.mention} already has the role **{role}**, i will remove the role instead! :)")
		await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
		return

	else:
		try:
			await user.add_roles(discord.utils.get(user.guild.roles, name=role))
		except Exception as e:
			await ctx.send(f'There was an error running this command; {str(e)}') #if error
		else:
			await ctx.send(f"you are now __***zenified***__, {user.mention}")


@bot.command()
@commands.has_any_role("Zeniath", "Noir", "Turbo", "Adem")
async def mod(ctx, user: discord.Member=None):
	"""give someone the mod role"""
	role = "Mod"

	if user is None:
		user = await ctx.send("oi mate, mention a member eh?")

	if role in [r.name for r in user.roles]:
		await ctx.send(f"because {user.mention} already has the role **{role}**, i will remove the role instead! :)")
		await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
		return

	else:
		try:
			await user.add_roles(discord.utils.get(user.guild.roles, name=role))
		except Exception as e:
			await ctx.send(f'There was an error running this command; {str(e)}') #if error
		else:
			await ctx.send(f"you are now __***moderatorfied***__, {user.mention}")

@bot.command()
@commands.has_any_role("Zeniath", "Noir", "Turbo", "Adem")
async def random(ctx, user: discord.Member=None):
	"""give someone the random role"""
	role = "Random"

	if user is None:
		user = await ctx.send("oi mate, mention a member eh?")

	if role in [r.name for r in user.roles]:
		await ctx.send(f"because {user.mention} already has the role **{role}**, i will remove the role instead! :)")
		await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
		return

	else:
		try:
			await user.add_roles(discord.utils.get(user.guild.roles, name=role))
		except Exception as e:
			await ctx.send(f'There was an error running this command; {str(e)}') #if error
		else:
			await ctx.send(f"you are now __***randomaratorfied***__, {user.mention}")

@bot.command()
@commands.has_any_role("Zeniath", "Noir", "Turbo", "Adem")
async def dj(ctx, user: discord.Member=None):
	"""give someone the dj role"""
	role = "DJ"

	if user is None:
		user = await ctx.send("oi mate, mention a member eh?")

	if role in [r.name for r in user.roles]:
		await ctx.send(f"because {user.mention} already has the role **{role}**, i will remove the role instead! :)")
		await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
		return

	else:
		try:
			await user.add_roles(discord.utils.get(user.guild.roles, name=role))
		except Exception as e:
			await ctx.send(f'There was an error running this command; {str(e)}') #if error
		else:
			await ctx.send(f"you are now __***djafied***__, {user.mention}")


@bot.command()
@commands.has_any_role("Zeniath", "Noir", "Turbo", "Adem")
async def say(ctx, *, message):
	"""make the bot say anything you want"""
	await ctx.send(message)


@bot.command(aliases=['die'])
@commands.is_owner()
async def kill(ctx):
	"""i think it's kind of obvious... incase you don't know, it kills the bot!"""
	await ctx.send("what a dick... okay bye")
	await ctx.bot.logout()

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