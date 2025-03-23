import telebot
from OpsAi import Ai
bot = telebot.TeleBot("5496942470:AAEC5pzhLnpCTU96GyH389TizovNT1mQxUU")
#############################
@bot.message_handler(commands=["bot","Bot","help"])
def Help(message):
	bot.reply_to(message,"نعم عزيزي رد عليه الان ميحتاج تبحث عن رسائلي ❤️ ")
@bot.message_handler(commands=["code"])
def codeing(message):
	if message.reply_to_message:
	       sp = message.text.split(None,1)[1]
	       s = Ai(query = sp)
	       cd = s.code()
	       bot.reply_to(message,cd)
#############################"""""يمكنك من خلال هذا الامر برمجة الاكواد في جميع لغات البرمجة"""	       
#############################
@bot.message_handler(commands=["Tr"])
def reply_text(message):
    if message.reply_to_message:
       if message.reply_to_message.text:
            s = Ai(query = message.text)
            bot.reply_to(message,s.Ar())
#############################
"""من خلال هذا الامر يمكنك ترجم النصوص من الانكليزي الى العربي"""            
############################# 
@bot.message_handler(func = lambda message : True)
def codeing(message):
	if message.reply_to_message:
	       s = Ai(query = message.text)
	       bot.reply_to(message,s.chat())
#############################
"""كود محادثة بينك وبين الذكاء الاصطناعي يمكنك حل الاسئله من خلاله"""
print("""write of codes : @bbannd
ch : @PJPPPPPP
Ch Library : @OpsLip
Coding Is runing...""")
bot.polling(skip_pending=True)            