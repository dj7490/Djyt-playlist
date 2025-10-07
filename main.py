import telebot
from pytube import Playlist

BOT_TOKEN = "8470214067:AAFfkbyL5k4V64PXHtlMNndAxqOgFvMgIDk"  # 🔹 Replace this

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Send me a YouTube playlist URL to download all videos (for personal use only).")

@bot.message_handler(func=lambda m: True)
def download_playlist(message):
    url = message.text.strip()
    try:
        playlist = Playlist(url)
        bot.reply_to(message, f"📋 Playlist found: {playlist.title}\nVideos: {len(playlist.video_urls)}\n\n📥 Downloading, please wait...")
        for video in playlist.videos:
            video.streams.get_highest_resolution().download(output_path="downloads/")
        bot.reply_to(message, f"✅ Download completed!\nSaved in Replit folder: `downloads/`")
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {e}")

print("🤖 Bot is running...")
bot.polling()
