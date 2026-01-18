import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8181761121:AAEpxUwDBiE20uyQGXH-qb-ig4uFvndXTFs"

async def ipinfo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text(" :\n/ip 8.8.8.8")
        return

    ip = context.args[0]
    url = f"http://ip-api.com/json/{ip}"
    data = requests.get(url).json()

    if data["status"] != "success":
        await update.message.reply_text(" Invalid IP")
        return

    text = f"""
 IP Info

IP: {data['query']}
Country: {data['country']}
Region: {data['regionName']}
City: {data['city']}
ISP: {data['isp']}
ASN: {data['as']}
Latitude: {data['lat']}
Longitude: {data['lon']}
Timezone: {data['timezone']}
"""

    await update.message.reply_text(text)

    # Send Map Location
    await context.bot.send_location(
        chat_id=update.effective_chat.id,
        latitude=data['lat'],
        longitude=data['lon']
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("ip", ipinfo))

print("Bot is running...")
app.run_polling()
