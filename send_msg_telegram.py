from telethon import TelegramClient

def send_msg_telegram(address, msg):

    # Initializtion to Telegram API
    api_id = 29326243
    api_hash = "0717db2ab38b4779e265f3ab854d28ca"
    HR_userbot = TelegramClient("Invite_to_Hackathon", api_id = api_id, api_hash = api_hash)

    async def main():
        # Send the individual invitation to the candidate via Telegram
        await HR_userbot.send_message(address, msg)

    with HR_userbot:
        HR_userbot.loop.run_until_complete(main())