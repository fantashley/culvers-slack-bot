# culvers-slack-bot

This bot scrapes the Flavor of the Day from the Culver's website for a given location and posts it to a Slack channel.

### Input

**slack_token** - Your "Bot User OAuth Access Token" from api.slack.com

**channel** - Channel within your workspace in which to post the Flavor of the Day

**location** - Culver's location to get the Flavor of the Day for. This will match the last portion of the FotD URL: https://www.culvers.com/restaurants/**golden-valley-mn-7th-ave**

### Usage Example
```python
from culversbot import CulversSlackBot

slack_token = os.environ['SLACK_API_TOKEN']
bot = CulversSlackBot(slack_token, "culvers", "golden-valley-mn-7th-ave")
bot.send_fotd()
```
