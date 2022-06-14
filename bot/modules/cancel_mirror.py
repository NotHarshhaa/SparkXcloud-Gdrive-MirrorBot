from telegram import InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler
from time import sleep

from bot import download_dict, dispatcher, download_dict_lock, QB_SEED, SUDO_USERS, OWNER_ID
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.message_utils import sendMessage, sendMarkup
from bot.helper.ext_utils.bot_utils import getDownloadByGid, MirrorStatus, getAllDownload
from bot.helper.telegram_helper import button_build


def cancel_mirror(update, context):
    args = update.message.text.split(" ", maxsplit=1)
    user_id = update.message.from_user.id
    if len(context.args) == 1:
        gid = context.args[0]
        dl = getDownloadByGid(gid)
        if not dl:
            return sendMessage(f"GID: <code>{gid}</code> 𝐍𝐨𝐭 𝐅𝐨𝐮𝐧𝐝.", context.bot, update.message)
    elif update.message.reply_to_message:
        mirror_message = update.message.reply_to_message
        with download_dict_lock:
            keys = list(download_dict.keys())
            if mirror_message.message_id in keys:
                dl = download_dict[mirror_message.message_id]
            else:
                dl = None
        if not dl:
            return sendMessage("𝐓𝐡𝐢𝐬 𝐢𝐬 𝐧𝐨𝐭 𝐚𝐧 𝐚𝐜𝐭𝐢𝐯𝐞 𝐭𝐚𝐬𝐤!", context.bot, update.message)
    elif len(context.args) == 0:
        msg = f"𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐚𝐧 𝐚𝐜𝐭𝐢𝐯𝐞 <code>/{BotCommands.MirrorCommand}</code> 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐰𝐡𝐢𝐜𝐡 𝐰𝐚𝐬 𝐮𝐬𝐞𝐝 𝐭𝐨 𝐬𝐭𝐚𝐫𝐭 𝐭𝐡𝐞 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐨𝐫 𝐬𝐞𝐧𝐝 <code>/{BotCommands.CancelMirror} GID</code> 𝐭𝐨 𝐜𝐚𝐧𝐜𝐞𝐥 𝐢𝐭!"
        return sendMessage(msg, context.bot, update.message)

    if OWNER_ID != user_id and dl.message.from_user.id != user_id and user_id not in SUDO_USERS:
        return sendMessage("This task is not for you!", context.bot, update.message)

    if dl.status() == MirrorStatus.STATUS_ARCHIVING:
        sendMessage("𝐀𝐫𝐜𝐡𝐢𝐯𝐚𝐥 𝐢𝐧 𝐏𝐫𝐨𝐠𝐫𝐞𝐬𝐬, 𝐘𝐨𝐮 𝐂𝐚𝐧'𝐭 𝐂𝐚𝐧𝐜𝐞𝐥 𝐈𝐭.", context.bot, update.message)
    elif dl.status() == MirrorStatus.STATUS_EXTRACTING:
        sendMessage("𝐄𝐱𝐭𝐫𝐚𝐜𝐭 𝐢𝐧 𝐏𝐫𝐨𝐠𝐫𝐞𝐬𝐬, 𝐘𝐨𝐮 𝐂𝐚𝐧'𝐭 𝐂𝐚𝐧𝐜𝐞𝐥 𝐈𝐭.", context.bot, update.message)
    elif dl.status() == MirrorStatus.STATUS_SPLITTING:
        sendMessage("𝐒𝐩𝐥𝐢𝐭 𝐢𝐧 𝐏𝐫𝐨𝐠𝐫𝐞𝐬𝐬, 𝐘𝐨𝐮 𝐂𝐚𝐧'𝐭 𝐂𝐚𝐧𝐜𝐞𝐥 𝐈𝐭.", context.bot, update.message)
    else:
        dl.download().cancel_download()

def cancel_all(status):
    gid = ''
    while True:
        dl = getAllDownload(status)
        if dl:
            if dl.gid() != gid:
                gid = dl.gid()
                dl.download().cancel_download()
                sleep(1)
        else:
            break

def cancell_all_buttons(update, context):
    buttons = button_build.ButtonMaker()
    buttons.sbutton("Downloading", "canall down")
    buttons.sbutton("Uploading", "canall up")
    if QB_SEED:
        buttons.sbutton("Seeding", "canall seed")
    buttons.sbutton("Cloning", "canall clone")
    buttons.sbutton("All", "canall all")
    button = InlineKeyboardMarkup(buttons.build_menu(2))
    sendMarkup('Choose tasks to cancel.', context.bot, update.message, button)

def cancel_all_update(update, context):
    query = update.callback_query
    user_id = query.from_user.id
    data = query.data
    data = data.split()
    if CustomFilters._owner_query(user_id):
        query.answer()
        query.message.delete()
        cancel_all(data[1])
    else:
        query.answer(text="𝐘𝐨𝐮 𝐝𝐨𝐧'𝐭 𝐡𝐚𝐯𝐞 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧 𝐭𝐨 𝐮𝐬𝐞 𝐭𝐡𝐞𝐬𝐞 𝐛𝐮𝐭𝐭𝐨𝐧𝐬!", show_alert=True)



cancel_mirror_handler = CommandHandler(BotCommands.CancelMirror, cancel_mirror,
                                       filters=(CustomFilters.authorized_chat | CustomFilters.authorized_user), run_async=True)

cancel_all_handler = CommandHandler(BotCommands.CancelAllCommand, cancell_all_buttons,
                                    filters=CustomFilters.owner_filter | CustomFilters.sudo_user, run_async=True)

cancel_all_buttons_handler = CallbackQueryHandler(cancel_all_update, pattern="canall", run_async=True)

dispatcher.add_handler(cancel_all_handler)
dispatcher.add_handler(cancel_mirror_handler)
dispatcher.add_handler(cancel_all_buttons_handler)