import random
import praw
from discord.ext import commands
import discord
import asyncio


reddit = praw.Reddit(client_id="nILEhRzBOkWsUA",
                     client_secret="xCkBoPYyBULhvk1-wq9DjQ0Bw3k",
                     user_agent="TommieBoyRandomDiscord")

@bot.command(name='meme', help='Pakt een epische meme van r/memes')
async def on_meme(ctx):
    memes = reddit.subreddit('memes').hot()
    meme_to_pick = random.randint(1, 10)
    for i in range(0, meme_to_pick):
        submission = next(x for x in memes if not x.stickied)

    await ctx.channel.send(submission.url)


# LINK = discord invite link
@bot.command(name='kick', help='Vote kick iemand uit de discord! (name#0000)')
async def on_kick(ctx, arg):
    if arg == "EDP445#0561":             # prevent admin of being kicked
        await ctx.send("Admin cannot be kicked")
    else:
        for user in ctx.guild.members:      # find the user that needs to be kicked out of all guild members
            if arg == str(user):
                vkmessage = await ctx.send("Kick Player: " + str(user) + "?")  # send a message that gets called back later
                emojies = ['👍', '👎']
                for emoji in emojies:
                    await vkmessage.add_reaction(emoji)     # add the emojies to the vote kick message

                await asyncio.sleep(10)    # wait 10 sec before counting the emojies
                vkmessage = await ctx.fetch_message(vkmessage.id)

                pos, neg = 0, 0
                for emoji in vkmessage.reactions:   # Count reactions
                    if str(emoji) == '👍':
                        pos = emoji.count
                    if str(emoji) == '👎':
                        neg = emoji.count
                if pos/neg > 1:            # When kicked, get link send to join back
                    await discord.Member.send(user, LINK)
                    await discord.Member.kick(user)
                    await ctx.send("Kicking Player: " + str(user) + "...")
                else:
                    await ctx.send(str(user) + " has not been kicked")
