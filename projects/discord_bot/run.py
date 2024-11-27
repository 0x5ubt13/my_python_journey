# -*- coding: utf-8 -*-
"""
MIT License

Copyright (c) 2019-2020 Arthur

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from configparser import ConfigParser
from datetime import datetime
from glob import glob
from os import name, execv, system, environ
from sys import argv, executable, stdout, exit
from pathlib import Path

from discord import LoginFailure, Status, Activity, ActivityType, Intents
from utilsx.console import Prettier, Colors
from utilsx.discord import BotX
from discord.ext import commands

from utils import VersionHandler, PrintHandler

# Check if the operating system is linux or windows. (nt = windows)
# If its windows, change the console clear command and the filepath delimiter.
clear, back_slash = "clear", "/"
if name == "nt":
    clear, back_slash = "cls", "\\"

# Read our configuration
cfg = ConfigParser()
cfg.read("./config/config.cfg")

if list(cfg) == ["DEFAULT"]:
    msg = "No valid config was loaded! (did you forget to change the names in the config folder?)"
    raise RuntimeError(msg)


class Bot(BotX):
    """
    The main bot object, this contains our handlers and loads our extensions
    """

    def __init__(self, _p: Prettier, _ph: PrintHandler):
        super().__init__(Intents().all())
        system(clear)
        stdout.flush()
        self.prettier = _p
        self.ph = _ph
        self.ph.info("Initializing client...")
        self.prefix = cfg["BOT"].get("prefix", "$")

        self.description = "This is Subtle Labs's Bot!\nIf you have any suggestion or special request please tell 0x5ubt13."

        self.ph.info("Started loading extensions.")

    @staticmethod
    def restart():
        system(clear)
        stdout.flush()
        execv(executable, ['python'] + argv)

    async def on_ready(self):
        await self.change_presence(activity=Activity(type=ActivityType.listening,
                                                     name="#selection-roles"),
                                   status=Status.online,
                                   )


if __name__ == "__main__":
    prettier = Prettier(colors_enabled=False,auto_strip_message=True)
    ph = PrintHandler(prettier, False)

    token = cfg["TOKEN"]["token"]
    
    bot = Bot(prettier, ph)

    bot.load_extension("extensions.ReactionRoles")
    #bot.load_extension("extensions.ReactionLogger")

    print("All loaded. Running now...")

    bot.run(token)

    print("Closing...")
