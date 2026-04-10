import telebot
import requests

# --- 🛠️ AAPKI CONFIGURATION ---
TOKEN = '8649293699:AAGD9oP0UWEOOOVqOvWzOuyNy4pMFpBntCI'
bot = telebot.TeleBot(TOKEN)

# Servers ki Details
ST_LOGIN = "2d118cd3d1f4c865c0fb" 
ST_KEY = "1WdkRWKV3kiegeG" 
DOOD_KEY = "493206pge8v68l0w5979f4"
MIXDROP_KEY = "KSqxYO1jS6mVMXwV5EW"
MIXDROP_EMAIL = "Pranjitborah41651@gmail.com"

@bot.message_handler(commands=['start'])
def welcome(message):
    welcome_text = (
        "🔥 **Boss! Aapka All-in-One Uploader Zinda Hai!**\n\n"
        "Bas mujhe video ka **Direct Link** bhejo, main use niche diye teeno servers par phenk dunga:\n"
        "1. Streamtape ✅\n"
        "2. Doodstream ✅\n"
        "3. Mixdrop ✅\n\n"
        "Mission: New Phone! 📱💰"
    )
    bot.reply_to(message, welcome_text, parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def multi_upload(message):
    url = message.text
    if not url.startswith("http"):
        bot.reply_to(message, "❌ Bhai, link sahi nahi hai. Link http se shuru hona chahiye!")
        return

    msg = bot.reply_to(message, "⏳ **Process Shuru...** Teeno servers ko command bhej raha hoon!")
    results = "🚀 **Upload Status:**\n\n"

    # 1. Streamtape Upload
    try:
        s_res = requests.get(f"https://api.streamtape.com/remotedl/add?login={ST_LOGIN}&key={ST_KEY}&url={url}").json()
        if s_res['status'] == 200:
            results += "✅ **Streamtape:** Added! (ID: " + s_res['result']['id'] + ")\n"
        else:
            results += "❌ **Streamtape:** Error (" + s_res['msg'] + ")\n"
    except: results += "❌ **Streamtape:** Connection Failed\n"

    # 2. Doodstream Upload
    try:
        d_res = requests.get(f"https://doodapi.com/api/upload/url?key={DOOD_KEY}&url={url}").json()
        if d_res['status'] == 200:
            results += "✅ **Doodstream:** Added successfully!\n"
        else:
            results += "❌ **Doodstream:** API Error\n"
    except: results += "❌ **Doodstream:** Connection Failed\n"

    # 3. Mixdrop Upload
    try:
        m_res = requests.get(f"https://api.mixdrop.ag/remoteupload?email={MIXDROP_EMAIL}&key={MIXDROP_KEY}&url={url}").json()
        if m_res['success']:
            results += "✅ **Mixdrop:** Uploading started!\n"
        else:
            results += "❌ **Mixdrop:** " + m_res['error'] + "\n"
    except: results += "❌ **Mixdrop:** Connection Failed\n"

    bot.edit_message_text(results, message.chat.id, msg.message_id, parse_mode="Markdown")

print("Bot is running...")
bot.polling()
