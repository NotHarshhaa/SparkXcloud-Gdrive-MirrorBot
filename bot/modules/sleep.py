from telegram.ext import CommandHandler

from bot import dispatcher, BASE_URL, alive
from bot.helper.telegram_helper.message_utils import sendMessage
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands


def sleep(update, context):
    if BASE_URL is None:
        sendMessage('𝐁𝐀𝐒𝐄_𝐔𝐑𝐋_𝐎𝐅_𝐁𝐎𝐓 𝐧𝐨𝐭 𝐩𝐫𝐨𝐯𝐢𝐝𝐞𝐝!', context.bot, update.message)
    elif alive.returncode is None:
        alive.kill()
        msg = '𝐘𝐨𝐮𝐫 𝐛𝐨𝐭 𝐰𝐢𝐥𝐥 𝐬𝐥𝐞𝐞𝐩 𝐢𝐧 𝟑𝟎 𝐦𝐢𝐧𝐮𝐭𝐞 𝐦𝐚𝐱𝐢𝐦𝐮𝐦.\n\n'
        msg += '𝐈𝐧 𝐜𝐚𝐬𝐞 𝐜𝐡𝐚𝐧𝐠𝐞𝐝 𝐲𝐨𝐮𝐫 𝐦𝐢𝐧𝐝 𝐚𝐧𝐝 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐮𝐬𝐞 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐚𝐠𝐚𝐢𝐧 𝐛𝐞𝐟𝐨𝐫𝐞 𝐭𝐡𝐞 𝐬𝐥𝐞𝐞𝐩 𝐭𝐡𝐞𝐧 𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐭𝐡𝐞 𝐛𝐨𝐭.\n\n'
        msg += f'𝐎𝐩𝐞𝐧 𝐭𝐡𝐢𝐬 𝐥𝐢𝐧𝐤 𝐰𝐡𝐞𝐧 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐰𝐚𝐤𝐞 𝐮𝐩 𝐭𝐡𝐞 𝐛𝐨𝐭 {BASE_URL}.'
        sendMessage(msg, context.bot, update.message)
    else:
        sendMessage('𝐏𝐢𝐧𝐠 𝐡𝐚𝐯𝐞 𝐛𝐞𝐞𝐧 𝐬𝐭𝐨𝐩𝐩𝐞𝐝, 𝐲𝐨𝐮𝐫 𝐛𝐨𝐭 𝐰𝐢𝐥𝐥 𝐬𝐥𝐞𝐞𝐩 𝐢𝐧 𝐥𝐞𝐬𝐬 𝐭𝐡𝐚𝐧 𝟑𝟎 𝐦𝐢𝐧.', context.bot, update.message)


sleep_handler = CommandHandler(command=BotCommands.SleepCommand, callback=sleep, filters=CustomFilters.owner_filter | CustomFilters.sudo_user, run_async=True)
dispatcher.add_handler(sleep_handler)