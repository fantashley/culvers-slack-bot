from bs4 import BeautifulSoup
import os
import requests
from slackclient import SlackClient


class CulversSlackBot:

    CULVERS_URL = "https://www.culvers.com/restaurants/"

    def __init__(self, slack_token, channel, location):
        self.slack_token = slack_token
        self.channel = channel
        self.location = location

    @staticmethod
    def get_fotd(location):
        response = requests.get(CulversSlackBot.CULVERS_URL + location)
        soup = BeautifulSoup(response.content, "html.parser")
        fotd = soup.find(class_="ModuleRestaurantDetail-fotd").h2.strong.string
        return fotd

    def send_fotd(self):
        message = "Today's flavor of the day is " + CulversSlackBot.get_fotd(self.location)
        sc = SlackClient(self.slack_token)
        if sc.rtm_connect():
            sc.rtm_send_message(self.channel, message)
        else:
            raise Exception("Connection to Slack API failed")


def main():
    slack_token = os.environ['SLACK_API_TOKEN']
    bot = CulversSlackBot(slack_token, "culvers", "golden-valley-mn-7th-ave")
    bot.send_fotd()
    exit(0)


if __name__ == "__main__":
    main()
