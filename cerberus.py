import discord
import random
import os
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix='+')
client.remove_command('help')


@client.event
async def on_message(message):

	if message.author == client.user:
		return
	
  #HELP
	if message.content == "+help":
		embed = discord.Embed(title="Help", description="Bot Commands (+)", color=discord.Colour.blue())
		embed.add_field(name="General Commands", value= f":star: `+ping - Latency Check`\n"
								f":star: `+8ball <question>- Ask Questions`\n" 
								f":star: `+how to hack - Get a list of useful resources`\n")

		await message.channel.send(content=None, embed=embed)

	#How to Hack
	if message.content == "+how to hack":
		embed = discord.Embed(title="Get started with Hacking!", description=f"""Ethical Hacking is an authorized practice of bypassing system security to identify potential data breaches and threats in a network. The company that owns the system or network allows Cyber Security engineers to perform such activities in order to test the system’s defenses. Thus, unlike malicious hacking, this process is planned, approved, and more importantly, legal. Ethical hackers aim to investigate the system or network weak points that malicious hackers can exploit or destroy. They collect and analyze the information to figure out ways to strengthen the security of the system/network/applications. By doing so,  they can improve the security footprint so that it can better withstand attacks or divert them. Here are some useful resources.""", 
		color=discord.Colour.blue())

		embed.add_field(name="Youtube Channels", value="Hackersploit\n" "Liveoverflow\n" "John Hammond\n" "DC Cybersec\n" "Null Byte\n" "Pwn Function\n" "STOK\n" "The XSS Rat")

		embed.add_field(name="Certifications", value="CEH\n" "OSCP\n" "eCPPT\n" "Security+\n" "eJPT" )
		embed.add_field(name="Programming Languages", value="Python\n" "C, C++\n" "Ruby\n" "Javascript\n" "Go Lang\n")
		embed.add_field(name="Books", value="The Hackers Playbook Series\n" "The Web Application Hacker's Handbook\n" "Hacking the Art of Exploitation\n" "Web Hacking 101\n" "Penetration Testing: A Hands-on Introduction to Hacking\n")
		
		embed.add_field(name='Get Started', value="https://bit.ly/2Qvmmdg")
		embed.set_image(url='https://blog.hyperiondev.com/wp-content/uploads/2019/01/Blog-Hacker-Languages.jpg')
		await message.channel.send(content=None, embed=embed)

    
	#SKIDS
#	words = ["help me hack", "help me break", "i need to hack", "i need to break", "help me hek"]
#	for word in words:
#		if message.content.find(word) != -1:
#			await message.channel.send(embed=embed)
#	else:
#		await client.process_commands(message)
	
#PING
@client.command()
async def ping(ctx):
	await ctx.send(f"`Pong! {round(client.latency * 1000)}ms`")


#8ball
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
	responses = ["It is certain.",
				"It is decidedly so.",
				"Without a doubt.",
				"Yes - definitely.",
				"You may rely on it.",
				"As I see it, yes.",
				"Most likely.",
				"Outlook good.",
				"Yes.",
				"Signs point to yes.",
				"Reply hazy, try again.",
				"Ask again later.",
				"Better not tell you now.",
				"Cannot predict now.",
				"Concentrate and ask again.",
				"Don't count on it.",
				"My reply is no.",
				"My sources say no.",
				"Outlook not so good.",
				"Very doubtful."
				]
	await ctx.send(f"**Question:** {question}\n**Answer:** {random.choice(responses)}")

#WARN MEMBER
@client.command()
async def warn(ctx, member: discord.Member):
    if ctx.message.author.guild_permissions.administrator :
        if member.guild_permissions.administrator:
            embed = discord.Embed(title="Error",
                                  description="You cant warn an Administrator",
                                  color=0xff0000)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Warned!",
            description="**{0}** has been warned by **{1}**!".format(member.name, ctx.message.author),
                                  color=0x00FF00)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error",
                                description="Permission Denied",
                                color=0xff0000)
        await ctx.send(embed=embed)


TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)

#hacekrsarcade.tech