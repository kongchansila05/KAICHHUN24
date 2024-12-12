import os
import telebot
import requests
from keep_alive import keep_alive
keep_alive()
API_KEY = os.getenv('API_KEY',
                    '7738820370:AAGH7alYqkMLpGaiCrSUjkH3Gq6kWzhBn_s')
IMAGE_URL = "https://i.ibb.co/5sxj6wj/KC-2.jpg"
bot = telebot.TeleBot(API_KEY)

url_register = "https://api.kai24.live/api/cs_player/register"
url_login = "https://api.kai24.live/api/cs_player/login_v2"
caption = "សំរាប់ចម្ងល់ឬបញ្ហាផ្សេងៗ នឹង ដាក់/ដក ប្រាក់ ចុចទីនេះ 👉🏻  https://line.me/R/ti/p/@472ljodl  បញ្ជាក់៖ នេះជាម៉ាសុីនសម្រាប់តែបង្កើតអាខោន មិនចេះឆ្លើយតបទេ។ សូមអរគុណ!"
domain = 'kai24.co'

def get_ip():
    # Using a free IP API to get the client's public IP
    response = requests.get("https://api.ipify.org?format=json")
    if response.status_code == 200:
        return response.json().get('ip')
    else:
        return "Error fetching IP"


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name or ""
    last_name = message.from_user.last_name or ""
    full_name = (first_name+last_name).strip()
    password = message.from_user.id
    data_register = {
        "username": full_name,
        "password": password,
        "domain": domain,
        "phone": '',
        "currencyId": '5',
    }

    data_login = {
        "username": full_name,
        "password": password,
        "domain": domain,
        "clientIP": get_ip(),
    }

    response_register = requests.post(
        url_register,
        data=data_register,
    )
    response_data = response_register.json()
    if response_data.get('code') == 200:
        response_login_true = requests.post(
            url_login,
            data=data_login,
        )
        login = response_login_true.json()
        if login.get('status') == 200:
            token = login['data']['token']
            bot.send_message(chat_id, f"អ្នកបង្កើត អាខោន ជោគជ័យ!")
            bot.send_message(
                chat_id, f"Your account: `{full_name}`\n"
                f"Your password: `{password}`\n",
                parse_mode="Markdown")
            bot.send_message(chat_id,
                             f"Login: https://kai24.live?token={token}")
            bot.send_photo(chat_id, photo=IMAGE_URL, caption=caption)
        return
    elif response_data.get('error') == "Duplicate username!":
        response_login = requests.post(
            url_login,
            data=data_login,
        )
        return_login = response_login.json()
        if return_login.get('error') == "Invalid username or password!":
            bot.send_message(
                chat_id,
                f"ឈ្មោះរបស់អ្នកមានរួចហេីយសូមធ្វេីការដូរឈ្មោះតេឡេក្រាមលោកអ្នក")
            return
        else:
            if return_login.get('status') == 200:
                bot.send_message(chat_id, f"អ្នកមាន អាខោន រួចហើយ!")
                bot.send_message(
                    chat_id,
                    f"Your account: `{full_name}`\n"
                    f"Your password: `{password}`\n",
                    parse_mode="Markdown")
                token = return_login['data']['token']
                bot.send_message(chat_id,
                                 f"Login: https://kai24.live?token={token}")
                bot.send_photo(chat_id, photo=IMAGE_URL, caption=caption)


@bot.message_handler(commands=['register'])
def send_register(message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name or ""
    last_name = message.from_user.last_name or ""
    full_name = (first_name+last_name).strip()
    password = message.from_user.id
    data_register = {
        "username": full_name,
        "password": password,
        "domain": domain,
        "phone": '',
        "currencyId": '5',
    }

    data_login = {
        "username": full_name,
        "password": password,
        "domain": domain,
        "clientIP": get_ip(),
    }

    response_register = requests.post(
        url_register,
        data=data_register,
    )
    response_data = response_register.json()
    if response_data.get('code') == 200:
        response_login_true = requests.post(
            url_login,
            data=data_login,
        )
        login = response_login_true.json()
        if login.get('status') == 200:
            token = login['data']['token']
            bot.send_message(chat_id, f"អ្នកបង្កើត អាខោន ជោគជ័យ!")
            bot.send_message(
                chat_id, f"Your account: `{full_name}`\n"
                f"Your password: `{password}`\n",
                parse_mode="Markdown")
            bot.send_message(chat_id,
                             f"Login: https://kai24.live?token={token}")
            bot.send_photo(chat_id, photo=IMAGE_URL, caption=caption)
        return
    elif response_data.get('error') == "Duplicate username!":
        response_login = requests.post(
            url_login,
            data=data_login,
        )
        return_login = response_login.json()
        if return_login.get('error') == "Invalid username or password!":
            bot.send_message(
                chat_id,
                f"ឈ្មោះរបស់អ្នកមានរួចហេីយសូមធ្វេីការដូរឈ្មោះតេឡេក្រាមលោកអ្នក")
            return
        else:
            if return_login.get('status') == 200:
                bot.send_message(chat_id, f"អ្នកមាន អាខោន រួចហើយ!")
                bot.send_message(
                    chat_id,
                    f"Your account: `{full_name}`\n"
                    f"Your password: `{password}`\n",
                    parse_mode="Markdown")
                token = return_login['data']['token']
                bot.send_message(chat_id,
                                 f"Login: https://kai24.live?token={token}")
                bot.send_photo(chat_id, photo=IMAGE_URL, caption=caption)


@bot.message_handler(commands=['contact'])
def send_contact_info(message):
    chat_id = message.chat.id  # Get the chat ID to send the message directly
    bot.send_photo(chat_id, photo=IMAGE_URL, caption=caption)

if __name__ == '__main__':
  bot.polling()
