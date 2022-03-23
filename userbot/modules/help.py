# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import ALIVE_NAME, CMD_HELP, REPO_NAME, EMOJI_HELP
from userbot.utils import ren_cmd
from platform import uname

modules = CMD_HELP

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@ren_cmd(pattern="help(?: |$)(.*)")
async def help(renbot):
    """ For .help command,"""
    args = renbot.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await renbot.edit(str(CMD_HELP[args]))
        else:
            await renbot.edit("**`NGETIK YANG BENER NGENTOT!`**")
            await asyncio.sleep(50)
            await renbot.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += f"`\t {EMOJI_HELP}  "
        await renbot.edit(f"**{REPO_NAME}**\n\n"
                         f"**{EMOJI_HELP} 𝙿𝙴𝙼𝙸𝙻𝙸𝙺 𝙱𝙾𝚃 : {DEFAULTUSER}**\n**{EMOJI_HELP}  𝙼𝙾𝙳𝚄𝙻𝙴𝚂 : {len(modules)}**\n\n"
                         f"**{EMOJI_HELP} 𝚂𝙴𝙼𝚄𝙰 𝙼𝙴𝙽𝚄 :**\n\n ══════════╣❃ ♕ ❃╠══════════\n\n"
                         f"{EMOJI_HELP} {string}\n\n ══════════╣❃ ♕ ❃╠══════════\n\nSupport @notsupports\n\n")
        await rambot.reply(f"\n**Contoh** : Ketik <`.help ping`> Untuk Informasi Pengunaan.\nJangan Lupa Berdoa Sebelum Mencoba wahahaha..")
        await asyncio.sleep(50)
        await rambot.delete()
