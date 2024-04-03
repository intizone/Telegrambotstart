from telethon import *



api_id = 7075575
api_hash = "07f21eadbd33e594c566d9d0062fde0f"

zoirbek = TelegramClient("session_name", api_id=api_id, api_hash=api_hash)

@zoirbek.on(events.NewMessage(outgoing=True, pattern=r".hi"))
async def hello(event):
    chat = await event.get_chat()
    await zoirbek.send_message(chat, "hello motherfather, how r u?")
    # print(chat)


# @zoirbek.on(events.NewMessage(outgoing=True, pattern=r'(.+)\*(\d+)'))
# async def repeat_message(event):
#     # Extract text and number from the message
#     text, num_str = event.pattern_match.groups()

#     # Convert the number string to an integer
#     num = int(num_str)

#     # Delete the original message
#     await event.delete()

#     # Send the repeated message
#     repeated_message = text * num
#     await event.respond(repeated_message)


@zoirbek.on(events.NewMessage(outgoing=True, pattern=r'(.+)\*(\d+)'))
async def repeat_message(event):
    # Extract text and number from the message
    text, num_str = event.pattern_match.groups()

    # Convert the number string to an integer
    num = int(num_str)

    # Delete the original message
    await event.delete()

    # Send the repeated message
    for _ in range(num):
        await event.respond(text)

print("bot is runnig...")
zoirbek.start()
zoirbek.run_until_disconnected()