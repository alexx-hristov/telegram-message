import requests
# API of the bot
TELEGRAM_TOKEN = # Telegram Token
# Chat ID
TELEGRAM_CHAT_ID = # Telegram Chat ID

def send_message(msg):
	payload = {
		'chat_id': TELEGRAM_CHAT_ID,
		'text': msg,
		'parse_mode': 'HTML'

	}
	return requests.post('https://api.telegram.org/bot{token}/sendMessage' .format(token=TELEGRAM_TOKEN),
						 data=payload).content
print('start sending message')
# adding the message here
send_message('message')