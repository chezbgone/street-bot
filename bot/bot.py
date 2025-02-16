import asyncio
import logging

import discord
from discord.ext import commands

from common.config import SECRETS
from cogs.chat_points import ChatPoints
from cogs.command_error_handler import CommandErrorHandler

discord.utils.setup_logging(level=logging.INFO)
LOG = logging.getLogger(__name__)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=['><> ', '><>'], intents=intents)

@bot.event
async def on_ready():
    LOG.info(f'Logged in as {bot.user}')
    await bot.add_cog(CommandErrorHandler(bot))
    await bot.add_cog(ChatPoints(bot))
    await bot.tree.sync()

async def main():
    await bot.start(SECRETS['DISCORD_TOKEN'])

if __name__ == '__main__':
    asyncio.run(main())
