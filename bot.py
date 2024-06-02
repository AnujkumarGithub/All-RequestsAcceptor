import logging, asyncio

from os import environ
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.ERROR)
       
SESSION = environ.get("SESSION", "BQEnIgcAM9Vj3vokmxIXaMY2SOGoBRzWl8T2HzTga9qDgHWrSGJQvyvHH3ZBAUYcRRhLvIJnVZvm7M47yUzd0rBHY3P4sRrJvvJC_6vzCJlIq0xxTIR0O3lQ23pP5dubw1DuMIVeP4wJzI7UaS5M7ZYis6tYvzCckbIKFnN7QXMwMSkHK23rgfsYOHSrCscJeHmNnHEDHeJpNMvBo6_CxxNixtdVl-_vpiCU-0wPjsXiknT-1mIdgeyQJO1ouiFKNhy3N-Z1jTsvTtJ34SuspGtAW4nfippqim3FS2gczfBwqAej1mswkPTxbNioHkAub0anSc0N4eGZxEQlv6cW8VXaNZQOSAAAAAB_2impAA")        
User = Client(name="AcceptUser", session_string=SESSION)


@User.on_message(filters.command(["run", "approve"], [".", "/"]))                     
async def approve(client, message):
    Id = message.chat.id
    await message.delete(True)
 
    try:
       while True: # create loop is better techniq to accept within seconds 💀
           try:
               await client.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))
    except FloodWait as s:
        asyncio.sleep(s.value)
        while True:
           try:
               await client.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))

    msg = await client.send_message(Id, "**Task Completed** ✓ **Approved Pending All Join Request**")
    await msg.delete()


logging.info("Bot Started....")
User.run()







