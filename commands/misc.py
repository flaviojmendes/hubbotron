from annotation.hubotron import command


@command(desc="Pings", params=["part_of_username"])
async def ping(ctx, arg=""):
    if arg == "":
        await ctx.send("pong")
    else:
        await ctx.send("Pinging " + mention(ctx, arg) + " 🏓")

