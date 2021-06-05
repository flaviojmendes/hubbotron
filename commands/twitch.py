import os

from discord import Embed
from twitchAPI import Twitch

from annotation.hubotron import command


@command(desc="List all commands")
async def live(ctx, grep=None):
    twitch = Twitch(os.environ['TWITCH_CLIENT'], os.environ['TWITCH_SECRET'])

    embed = Embed(title="Estão Online agora os creators:", color=0x00ff75)

    with open("creators.hub", "r") as fp:
        Streamers = fp.read().split('\n')

    for streamer in Streamers:
        user_info = twitch.get_streams(user_login=streamer)
        if len(user_info['data']) > 0:
            embed.add_field(name=streamer,
                            value=user_info['data'][0]['title'] + "\n" + "https://twitch.tv/" + streamer,
                            inline=False)

    await ctx.author.send(embed=embed)

