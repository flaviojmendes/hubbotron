import os

import discord
from discord.ext import commands
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects import postgresql
from twitchAPI import UserAuthenticator

client = discord.Client()
bot = commands.Bot(command_prefix='.')


# bot.run(os.environ['DISCORD_API_KEY'])


from twitchAPI.pubsub import PubSub
from twitchAPI.twitch import Twitch
from twitchAPI.types import AuthScope
from pprint import pprint
from uuid import UUID

def callback_whisper(uuid: UUID, data: dict) -> None:
    print('got callback for UUID ' + str(uuid))
    pprint(data)
#
# # setting up Authentication and getting your user id
# twitch = Twitch('r1g10agwmyy9mxg4t97g8xzfyhutnb', '2qtufsomu9clrxyf5fexu4idosecaa')
# twitch.authenticate_app([])
# twitch.set_user_authentication('my_user_auth_token', [AuthScope.WHISPERS_READ], 'my_user_auth_refresh_token')
# user_id = twitch.get_users(logins=['my_username'])['data'][0]['id']
#
# # starting up PubSub
# pubsub = PubSub(twitch)
# pubsub.start()
# # you can either start listening before or after you started pubsub.
# uuid = pubsub.listen_whispers(user_id, callback_whisper)w
#
# from twitchAPI.twitch import Twitch


def user_refresh(token: str, refresh_token: str):
    print(f'my new user token is: {token}')


def app_refresh(token: str):
    print(f'my new app token is: {token}')


twitch = Twitch(os.environ['TWITCH_CLIENT'], os.environ['TWITCH_SECRET'])

user_info = twitch.get_streams(user_login='em1dio')
user_id = user_info['data'][0]['id']


# target_scope = [AuthScope.BITS_READ]
# auth = UserAuthenticator(twitch, target_scope, force_verify=False)
# # this will open your default browser and prompt you with the twitch verification website
# token, refresh_token = auth.authenticate()
# # add User authentication
# twitch.set_user_authentication(token, target_scope, refresh_token)
#
#
# # starting up PubSub
# pubsub = PubSub(twitch)
# pubsub.start()
# # you can either start listening before or after you started pubsub.
# user_id = twitch.get_users(logins=['flaviojmendes'])['data'][0]['id']
#
# uuid = pubsub.listen_whispers(user_id, callback_whisper)