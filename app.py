import os 
import logging
from dotenv import load_dotenv
import google.generativeai as genai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = ""
GEMINI_API_KEY = os.getenv("GENAI_API_KEY")

if not BOT_TOKEN or not GEMINI_API_KEY:
    raise ValueError("Please set the BOT_TOKEN and GENAI_API_KEY environment variables.")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-2.5-pro-exp-03-25')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Hello! I'm a bot who can provide summary of video by URL. How can I assist you today?"
    )

if __name__ == "__main__":
    logger.info("Starting the bot...")
    
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    