import os
import requests
def send_simple_message():
  	return requests.post(
  		"https://api.mailgun.net/v3/sandbox9075107281e946239d1a8701b8f79707.mailgun.org/messages",
  		auth=("api", os.getenv('API_KEY', '8ed7aac9ed5c58d24403f61dfb5d67e6-d638fab7-eb3229b8')),
  		data={"from": "Mailgun Sandbox <postmaster@sandbox9075107281e946239d1a8701b8f79707.mailgun.org>",
			"to": "Ben Arthur <ben@dmedesk.ai>",
  			"subject": "Hello Ben Arthur",
  			"text": "Congratulations Ben Arthur, you just sent an email with Mailgun! You are truly awesome!"})