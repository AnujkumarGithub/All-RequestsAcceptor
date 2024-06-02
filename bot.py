import logging, asyncio

from os import environ
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.ERROR)
       
SESSION = environ.get("SESSION", "BQC6kfsAe8NFfnuNvAVx2e9I02qXZ9gYKi1MwgKr4wUgpcLsiUznlE3A6Ppdyd-qSCAW3DRUus1qlNZpD3-rLXG7In6oQXaX3vGpR0_SB7O7v6dx0lxeZ5gChkUCEqT7cF1CCpXF2cGYVBiMXhTPNRcoBJs4DGeMKgEO3A2HkcAnmzQ5A3gRNGufi_lPqGRK5WXHBKpS8cqu00sFOT2rR8w1iRxXVuY-B28_MFGTE_eOe51xLurEB25O2jUcZSJSOFUrW3aamX_IsR9Tc8sMiaAQ-WmiyUf0nlWAActljfxnSIgiYyABAXNeVOOUN762tA6PAp6IgP7ZY8QV3g9O77IOXNSooQAAAAB_2impAA")        
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







