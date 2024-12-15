import asyncio
from datetime import datetime
from telethon import TelegramClient, events

api_id = 16006646
api_hash = "1e803b0c61213dd6d8922f804097f5bb"

# Zu überwachende Chats (nur gültige IDs oder @Benutzernamen)
CHAT_LIST = [
    "@solanapoolscanner",
    -1002130000854  
]

# Liste von Suchbegriffen
SEARCH_TERMS = ["KIRBY", "Kirby on Mars", "kirbyonkas", "kirby"]

# Deine eigene Telegram-User-ID
MY_USER_ID = 596333326

# Der andere Bot, dem du den Treffer melden möchtest
OTHER_BOT_ID = 7348325293

client = TelegramClient("session_meine_gruppe", api_id, api_hash)

@client.on(events.NewMessage(chats=CHAT_LIST))
async def listener(event):
    message_text = event.raw_text.lower()  # alles klein, um case-insensitive zu prüfen
    # Prüfe, ob einer der Begriffe in der Nachricht vorkommt
    if any(term.lower() in message_text for term in SEARCH_TERMS):
        # 1) Nachricht an dich selbst
        await client.send_message(
            MY_USER_ID,
            f"Treffer für {SEARCH_TERMS} in Chat {event.chat_id}\n\n{event.raw_text}"
        )
        
        # 2) Nachricht an den anderen Bot
        await client.send_message(
            OTHER_BOT_ID,
            f"Treffer für {SEARCH_TERMS} in Chat {event.chat_id}\n\n{event.raw_text}"
        )

async def main():
    print("Telethon-Client gestartet, lauscht auf Nachrichten ...")

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
