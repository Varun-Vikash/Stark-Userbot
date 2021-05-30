import pyrogram
from pyrogram import Client

friday_ = """

▒▄█▀▀█▒█▀█▀█─░▄█▀▄─▒▐█▀▀▄▒▐█▒▐▀
▒▀▀█▄▄░░▒█░░░▐█▄▄▐█▒▐█▒▐█▒▐██▌░
▒█▄▄█▀░▒▄█▄░░▐█─░▐█▒▐█▀▄▄▒▐█▒▐▄



Copyright (C) 2020-2021 by Varun-Vikash@Github, < https://github.com/Varun-Vikash >.
This file is part of < https://github.com/Varun-Vikash/StarkUserbot > project,
and is released under the "The MIT License Agreement".
Please see < https://github.com/Varun-Vikash/blob/master/LICENSE >
All rights reserved.
"""

print(Stark_)
api_id = input("Enter Your API ID: \n")
api_hash = input("Enter Your API HASH : \n")

with Client("StarkUB", api_id=api_id, api_hash=api_hash) as bot_:
    first_name = (bot_.get_me()).first_name
    string_session_ = f"<b>String Session For {first_name}</b> \n<code>{bot_.export_session_string()}</code>"
    bot_.send_message("me", string_session_, parse_mode="html")
    print(f"String Has Been Sent To Your Saved Message : {first_name}")
