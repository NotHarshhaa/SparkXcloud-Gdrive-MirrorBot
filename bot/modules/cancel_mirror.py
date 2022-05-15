from telegram.ext import CommandHandler
from bot import download_dict, dispatcher, download_dict_lock, DOWNLOAD_DIR, SUDO_USERS, OWNER_ID
from bot.helper.ext_utils.fs_utils import clean_download
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.message_utils import sendMessage, sendMarkup
from bot.helper.ext_utils.bot_utils import getDownloadByGid, MirrorStatus, getAllDownload
from bot.helper.telegram_helper import button_build
from bot.helper.telegram_helper.message_utils import *

from time import sleep
from bot.helper.ext_utils.bot_utils import getDownloadByGid, MirrorStatus, getAllDownload


def cancel_mirror(update, context):
    args = update.message.text.split(" ", maxsplit=1)
    user_id = update.message.from_user.id
    if len(args) > 1:
        gid = args[1]
        dl = getDownloadByGid(gid)
        if not dl:
            return sendMessage(f"GID: <code>{gid}</code> 𝐍𝐨𝐭 𝐅𝐨𝐮𝐧𝐝.", context.bot, update.message)
    elif update.message.reply_to_message:
        mirror_message = update.message.reply_to_message
        with download_dict_lock:
            keys = list(download_dict.keys())
            try:
                dl = download_dict[mirror_message.message_id]
            except:
                dl = None
        if not dl:
            return sendMessage(f"𝐓𝐡𝐢𝐬 𝐢𝐬 𝐧𝐨𝐭 𝐚𝐧 𝐚𝐜𝐭𝐢𝐯𝐞 𝐭𝐚𝐬𝐤!", context.bot, update.message)
    elif len(args) == 1:
        msg = f"𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐚𝐧 𝐚𝐜𝐭𝐢𝐯𝐞 <code>/{BotCommands.MirrorCommand}</code> 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐰𝐡𝐢𝐜𝐡 𝐰𝐚𝐬 𝐮𝐬𝐞𝐝 𝐭𝐨 𝐬𝐭𝐚𝐫𝐭 𝐭𝐡𝐞 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐨𝐫 𝐬𝐞𝐧𝐝 <code>/{BotCommands.CancelMirror} GID</code> 𝐭𝐨 𝐜𝐚𝐧𝐜𝐞𝐥 𝐢𝐭!"
        return sendMessage(msg, context.bot, update.message)

    if OWNER_ID == user_id or dl.message.from_user.id == user_id or user_id in SUDO_USERS:
        pass
    else:
        return sendMessage("𝐓𝐡𝐢𝐬 𝐭𝐚𝐬𝐤 𝐝𝐨𝐞𝐬𝐧'𝐭 𝐛𝐞𝐥𝐨𝐧𝐠 𝐭𝐨 𝐲𝐨𝐮!", context.bot, update.message)

    if dl.status() == MirrorStatus.STATUS_ARCHIVING:
        sendMessage("𝐀𝐫𝐜𝐡𝐢𝐯𝐚𝐥 𝐢𝐧 𝐏𝐫𝐨𝐠𝐫𝐞𝐬𝐬, 𝐘𝐨𝐮 𝐂𝐚𝐧'𝐭 𝐂𝐚𝐧𝐜𝐞𝐥 𝐈𝐭.", context.bot, update)
    elif dl.status() == MirrorStatus.STATUS_EXTRACTING:
        sendMessage("𝐄𝐱𝐭𝐫𝐚𝐜𝐭 𝐢𝐧 𝐏𝐫𝐨𝐠𝐫𝐞𝐬𝐬, 𝐘𝐨𝐮 𝐂𝐚𝐧'𝐭 𝐂𝐚𝐧𝐜𝐞𝐥 𝐈𝐭.", context.bot, update)
    else:
        dl.download().cancel_download()
        sleep(3)  # incase of any error with ondownloaderror listener
        clean_download(f'{DOWNLOAD_DIR}{mirror_message.message_id}/')


def cancel_all(update, context):
    count = 0
    gid = 0
    while True:
        dl = getAllDownload()
        if dl:
            if dl.gid() != gid:
                gid = dl.gid()
                dl.download().cancel_download()
                count += 1
                sleep(0.3)
        else:
            break
    sendMessage(f'{count} 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝(𝐬) 𝐡𝐚𝐬 𝐛𝐞𝐞𝐧 𝐂𝐚𝐧𝐜𝐞𝐥𝐥𝐞𝐝!', context.bot, update)
    


cancel_mirror_handler = CommandHandler(BotCommands.CancelMirror, cancel_mirror,
                                    filters=(CustomFilters.authorized_chat | CustomFilters.authorized_user), run_async=True)
cancel_all_handler = CommandHandler(BotCommands.CancelAllCommand, cancel_all,
                                    filters=CustomFilters.owner_filter | CustomFilters.sudo_user, run_async=True)
dispatcher.add_handler(cancel_all_handler)
dispatcher.add_handler(cancel_mirror_handler)
