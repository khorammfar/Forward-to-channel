from pyrogram import Client
from pyrogram import idle
from pyrogram import filters

api_id, api_hash = 12456789, 'abcdefghij'

app = Client('session', api_id, api_hash)

Source = -100123456789
Destination = -100987654321

@app.on_message(filters.chat(Source))
def copy_from(app, message):
    app.forward_messages(
        chat_id=Destination,
        from_chat_id=message.chat.id,
        message_ids=message.message_id
    )

app.start()
print('Loaded..')
idle()
app.stop()
