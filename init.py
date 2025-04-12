import asyncio
import logging
from pyrogram import Client
from vars import API_ID, API_HASH, BOT_TOKEN









bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    sleep_threshold=120,
    workers=50
)





