from culversbot import CulversSlackBot
import os

slack_token = os.environ['SLACK_API_TOKEN']
channel = os.environ['SLACK_CHANNEL']
location = os.environ['CULVERS_LOCATION']

bot = CulversSlackBot(slack_token, channel, location)
bot.send_fotd()
