import discord
from discord.ext import commands 
import random
import asyncio
import aiohttp
import json
from insultgenerator import phrases

class Fun:
	def __init__(self, bot):
		self.bot = bot
		self.answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it',
                     'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again',
                     'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
                     'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good',
                     'Very doubtful']
		self.type = ["png", "gif"]

	@commands.command(aliases=['8ball', 'eightball'])
	async def ball(self, ctx, *, question:str):
  		author = ctx.author
  		avatar = author.avatar_url
  		timestamp = ctx.message.created_at
  		embed = discord.Embed(title="8ball", color=0xed, timestamp=timestamp)
  		embed.add_field(name='Question :question:', value=f"{question}")
  		embed.add_field(name="Answer :8ball:", value=random.choice(self.answers))
  		embed.set_footer(text="Asked at")
  		embed.set_thumbnail(url='http://legomenon.com/images/magic-8ball-first-white.jpg')
  		embed.set_author(name=author, icon_url=avatar)
  		await ctx.send(embed=embed)
  		await ctx.message.delete()

	@commands.command()
	async def cat(self, ctx):
		async with aiohttp.ClientSession() as session:
			async with session.get('http://random.cat/meow') as resp:
				data = await resp.json()
		embed = discord.Embed(color=discord.Color.blue())
		embed.set_image(url=data['file'])
		await ctx.send(embed=embed)
		
	@commands.command()
	async def dog(self, ctx):
		async with aiohttp.ClientSession() as session:
			async with session.get('http://dog.ceo/api/breeds/image/random') as resp:
				data = await resp.json()
		embed = discord.Embed(color=discord.Color.blue())
		embed.set_image(url=data['message'])
		await ctx.send(embed=embed)
		
	async def round(self, ctx, player:str):
		await opponent.send('The opponent is going')
		await author.send(f'`Check`, `{option}`, or `Fold`')
		choice = await self.bot.wait_for('message', check=lambda m: m.author.id == author.id)
		if choice.content.lower() == 'check':
			await author.send('You checked. It is the opponents turn now')
			await opponent.send(f'The opponent checked\n`Check`, `Bet` or `Fold`?')
			turn = 'player2'
		if choice.content.lower() == 'fold':
			await author.send(f'You folded. The opponent gets the chips. You have {player1_chips} chips')
			await opponent.send(f'The opponent folded. You get the chips. You now have {player2_chips} chips')
			player2_chips += pot
			turn = 'player2'
		if choice.content.lower() == 'bet':
			await author.send('How much do you want to bet?')
			ammount = await self.bot.wait_for('message', check=lambda m: m.author.id == author.id)
			if int(ammount.content) < 25:
				await author.send('You must bet atleast 25 chips')
			elif int(ammount.content) > player1_chips:
				await author.send(f'You only have {player1_chips} chips')
			else:
				pot += int(ammount.content)
				player1_chips -= int(ammount.content)
				await author.send(f'You raised the bet by {ammount.content}\nIt is now the opponents turn')
				await opponent.send(f'The opponent raised the bet by {ammount.content}\n`Check`, `Bet` or `Fold`?')

			
	@commands.command()
	async def poker(self, ctx, opponent: discord.Member):
		def check(m):
			return m.channel == ctx.channel
		num = random.randint(0, 24)
		num2 = random.randint(0, 24)
		num3 = random.randint(0, 24)
		num4 = random.randint(0, 24)
		author = ctx.author
		pot = 0
		option = 'Bet'
		player1_chips = 1000
		player2_chips = 1000
		cards = ['ace of hearts ',' ace of spades ',' ace of clubs ',' ace of diamonds ',' one of hearts ',' one of spades',' one of hearts',' one of diamonds ',' two of hearts ',' two of spades ',' two of hearts ',' two of diamonds ',' three of hearts ',' three of spades ',' three of clubs',' three of diamonds ',' four of hearts ',' four of spades ',' four of clubs ',' four of diamonds ',' five of hearts ',' five of spades ',' five of clubs ',' five of diamonds ',' six of hearts ',' six of spades ',' six of clubs',' six of diamonds ',' seven of hearts ',' seven of spades ',' seven of clubs ',' seven of diamonds ',' eight of hearts ',' eight of spades ',' eight of clubs ',' eight of diamonds ',' nine of hearts ',' nine of spades ',' nine of clubs ',' nine of diamonds ',' ten of hearts ',' ten of spades ',' ten of clubs ',' ten of diamonds ',' jack of hearts ',' jack of spades ',' jack of clubs ',' jack of diamonds ',' queen of hearts ',' queen of spades ',' queen of clubs ',' queen of diamonds ',' king of hearts ',' king of spades ',' king of clubs ',' king of diamonds']
		hand_1 = [f'{cards[num]}', f'{cards[num2]}']
		hand_2 = [f'{cards[num3]}', f'{cards[num4]}']
		await ctx.send(f'{opponent.mention}, {ctx.author} has challenged you to a round of Texas Holdem Poker. Type `accept` to play')
		res = await self.bot.wait_for('message', check=lambda m: m.author.id == opponent.id)
		if res.content == 'accept':
			await ctx.send('Challenge accepted\n Dealing cards in DM..')
			await ctx.author.send(f'Here is your hand **{hand_1}**\nYou both have 1000 chips')
			await opponent.send(f'Here is your hand **{hand_2}**\nYou both have 1000 chips')
			await asyncio.sleep(5)
			turn = 'player2'
			await self.round(turn)
	
	@commands.command()
	async def roast(self, ctx, user: discord.Member = None):
		async with aiohttp.ClientSession().get('https://insult.mattbas.org/api/insult.json') as resp:
			data = await resp.json(content_type=None)
		await ctx.send(data['insult'])
		
	@commands.command()
	async def yomomma(self, ctx):
		async with aiohttp.ClientSession() as session:
			async with session.get('http://api.yomomma.info') as resp:
				data = await resp.json(content_type=None)
		await ctx.send(data['joke'])
		
	@commands.command()
	async def whosthatpokemon(self, ctx):
		num = random.randint(1, 926)
		async with aiohttp.ClientSession().get(f'https://pokeapi.co/api/v2/pokemon-form/{num}/') as resp:
			data = await resp.json()
		embed = discord.Embed(title='Who\'s that pokemon?', color=discord.Color.blue())
		embed.set_image(url=data['sprites']['front_default'])
		await ctx.send(embed=embed)
		guess = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author)
		if guess.content == data['name']:
			await ctx.send(f'Correct! That pokemon is {data["name"]}')
		else:
			await ctx.send(f'Incorrect! That pokemon is {data["name"]}')
		



def setup(bot):
	bot.add_cog(Fun(bot))