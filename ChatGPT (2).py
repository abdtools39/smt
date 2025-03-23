import requests
import json
import time
import telebot

# إعدادات البوت
API_TOKEN = '7448705162:AAHyXP7RuIvHck3Xqf45MG4C0mzzxL1KsS0'
bot = telebot.TeleBot(API_TOKEN)

# دالة NERO_SIN المعدلة
@bot.message_handler(commands=["start"])
def well(message):
    bot.send_photo(message.chat.id, "https://t.me/Dddddwwqqq/5", caption="Welcome to my bot, which specializes in chat GPT. Send anything and it will answer you . Good Luck 🥷🤍")

def NERO_SIN(message):
    nn = message.text
    
    url = "https://api.binjie.fun/api/generateStream"
    
    payload = json.dumps({
        "prompt": nn,
        "network": True,
        "system": "",
        "withoutContext": False,
        "stream": False
    })
    
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/26.0 Chrome/122.0.0.0 Mobile Safari/537.36",
        'Content-Type': "application/json",
        'sec-ch-ua': "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Samsung Internet\";v=\"26.0\"",
        'sec-ch-ua-mobile': "?1",
        'sec-ch-ua-platform': "\"Android\"",
        'origin': "https://chat18.aichatos8.com",
        'sec-fetch-site': "cross-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://chat18.aichatos8.com/",
        'accept-language': "ar-IQ,ar-AE;q=0.9,ar;q=0.8,en-AU;q=0.7,en;q=0.6,en-US;q=0.5"
    }
    
    response = requests.post(url, data=payload, headers=headers)
    response_text = response.content.decode('utf-8')
    
    return response_text

# إعدادات البوت لاستقبال الرسائل
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # الرد بانتظار ثواني
    wait_message = bot.reply_to(message, "انتظر قليلاً...")

    # تأخير لبعض الوقت (مثلاً 3 ثوانٍ)
    time.sleep(3)

    # الحصول على الرد من دالة NERO_SIN
    response_text = NERO_SIN(message)
    
    # تعديل الرسالة النهائية للمستخدم
    bot.edit_message_text(chat_id=message.chat.id, message_id=wait_message.message_id, text=response_text)

# بدء البوت
bot.infinity_polling()
