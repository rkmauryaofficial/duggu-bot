from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8902004333:AAEgK-DmzPG2iR4HDaM2u5o8-s9R54MaoS8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to BDGPLAY Duggu Bot\n\n"
        "/register - Register BDGWIN\n"
        "/agent - Contact Agent\n"
        "/priya - Contact Head Agent Priya\n"
        "/vip - VIP Channel"
    )

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "BDGWIN Register:\nhttps://bdgsh.com//#/register?invitationCode=14163232483"
    )

async def agent(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Contact Agent:\nhttps://t.me/rkmaurya_official"
    )

async def priya(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Head Agent Priya:\nhttps://t.me/bdgplaypriya"
    )

async def vip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "VIP Channel:\nhttps://t.me/bdgwin_rkmaurya"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("register", register))
app.add_handler(CommandHandler("agent", agent))
app.add_handler(CommandHandler("priya", priya))
app.add_handler(CommandHandler("vip", vip))

app.run_polling()

