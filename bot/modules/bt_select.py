from telegram.ext import CommandHandler, CallbackQueryHandler
from os import remove, path as ospath

from bot import aria2, BASE_URL, download_dict, dispatcher, download_dict_lock, SUDO_USERS, OWNER_ID
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.message_utils import sendMessage, sendMarkup, sendStatusMessage
from bot.helper.ext_utils.bot_utils import getDownloadByGid, MirrorStatus, bt_selection_buttons

def select(update, context):
    user_id = update.message.from_user.id
    if len(context.args) == 1:
        gid = context.args[0]
        dl = getDownloadByGid(gid)
        if not dl:
            sendMessage(f"GID: <code>{gid}</code> Not Found.", context.bot, update.message)
            return
    elif update.message.reply_to_message:
        mirror_message = update.message.reply_to_message
        with download_dict_lock:
            if mirror_message.message_id in download_dict:
                dl = download_dict[mirror_message.message_id]
            else:
                dl = None
        if not dl:
            sendMessage("This is not an active task!", context.bot, update.message)
            return
    elif len(context.args) == 0:
        msg = "𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐚𝐧 𝐚𝐜𝐭𝐢𝐯𝐞 /𝐜𝐦𝐝 𝐰𝐡𝐢𝐜𝐡 𝐰𝐚𝐬 𝐮𝐬𝐞𝐝 𝐭𝐨 𝐬𝐭𝐚𝐫𝐭 𝐭𝐡𝐞 𝐪𝐛-𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐨𝐫 𝐚𝐝𝐝 𝐠𝐢𝐝 𝐚𝐥𝐨𝐧𝐠 𝐰𝐢𝐭𝐡 𝐜𝐦𝐝\n\n"
        msg += "𝐓𝐡𝐢𝐬 𝐜𝐨𝐦𝐦𝐚𝐧𝐝 𝐦𝐚𝐢𝐧𝐥𝐲 𝐟𝐨𝐫 𝐬𝐞𝐥𝐞𝐜𝐭𝐢𝐨𝐧 𝐢𝐧𝐜𝐚𝐬𝐞 𝐲𝐨𝐮 𝐝𝐞𝐜𝐢𝐝𝐞𝐝 𝐭𝐨 𝐬𝐞𝐥𝐞𝐜𝐭 𝐟𝐢𝐥𝐞𝐬 𝐟𝐫𝐨𝐦 𝐚𝐥𝐫𝐞𝐚𝐝𝐲 𝐚𝐝𝐝𝐞𝐝 𝐭𝐨𝐫𝐫𝐞𝐧𝐭."
        msg += "𝐁𝐮𝐭 𝐲𝐨𝐮 𝐜𝐚𝐧 𝐚𝐥𝐰𝐚𝐲𝐬 𝐮𝐬𝐞 /𝐜𝐦𝐝 𝐰𝐢𝐭𝐡 𝐚𝐫𝐠 `𝐬` 𝐭𝐨 𝐬𝐞𝐥𝐞𝐜𝐭 𝐟𝐢𝐥𝐞𝐬 𝐛𝐞𝐟𝐨𝐫𝐞 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐬𝐭𝐚𝐫𝐭."
        sendMessage(msg, context.bot, update.message)
        return

    if OWNER_ID != user_id and dl.message.from_user.id != user_id and user_id not in SUDO_USERS:
        sendMessage("This task is not for you!", context.bot, update.message)
        return
    if dl.status() not in [MirrorStatus.STATUS_DOWNLOADING, MirrorStatus.STATUS_PAUSED, MirrorStatus.STATUS_WAITING]:
        sendMessage('𝐓𝐚𝐬𝐤 𝐬𝐡𝐨𝐮𝐥𝐝 𝐛𝐞 𝐢𝐧 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐨𝐫 𝐩𝐚𝐮𝐬𝐞 (𝐢𝐧𝐜𝐚𝐬𝐞 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐝𝐞𝐥𝐞𝐭𝐞𝐝 𝐛𝐲 𝐰𝐫𝐨𝐧𝐠) 𝐨𝐫 𝐪𝐮𝐞𝐮𝐞𝐝 (𝐬𝐭𝐚𝐭𝐮𝐬 𝐢𝐧𝐜𝐚𝐬𝐞 𝐲𝐨𝐮 𝐮𝐬𝐞𝐝 𝐭𝐨𝐫𝐫𝐞𝐧𝐭 𝐟𝐢𝐥𝐞)!', context.bot, update.message)
        return
    if dl.name().startswith('[METADATA]'):
        sendMessage('𝐓𝐫𝐲 𝐚𝐟𝐭𝐞𝐫 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐦𝐞𝐭𝐚𝐝𝐚𝐭𝐚 𝐟𝐢𝐧𝐢𝐬𝐡𝐞𝐝!', context.bot, update.message)
        return

    try:
        if dl.listener().isQbit:
            id_ = dl.download().ext_hash
            client = dl.client()
            client.torrents_pause(torrent_hashes=id_)
        else:
            id_ = dl.gid()
            aria2.client.force_pause(id_)
    except:
        sendMessage("This is not a bittorrent task!", context.bot, update.message)
        return

    SBUTTONS = bt_selection_buttons(id_)
    msg = "𝐘𝐨𝐮𝐫 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐩𝐚𝐮𝐬𝐞𝐝. 𝐂𝐡𝐨𝐨𝐬𝐞 𝐟𝐢𝐥𝐞𝐬 𝐭𝐡𝐞𝐧 𝐩𝐫𝐞𝐬𝐬 𝐃𝐨𝐧𝐞 𝐒𝐞𝐥𝐞𝐜𝐭𝐢𝐧𝐠 𝐛𝐮𝐭𝐭𝐨𝐧 𝐭𝐨 𝐫𝐞𝐬𝐮𝐦𝐞 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠."
    sendMarkup(msg, context.bot, update.message, SBUTTONS)

def get_confirm(update, context):
    query = update.callback_query
    user_id = query.from_user.id
    data = query.data
    data = data.split()
    dl = getDownloadByGid(data[2])
    if not dl:
        query.answer(text="𝐓𝐡𝐢𝐬 𝐭𝐚𝐬𝐤 𝐡𝐚𝐬 𝐛𝐞𝐞𝐧 𝐜𝐚𝐧𝐜𝐞𝐥𝐥𝐞𝐝!", show_alert=True)
        query.message.delete()
        return
    if hasattr(dl, 'listener'):
        listener = dl.listener()
    else:
        query.answer(text="Not in download state anymore! Keep this message to resume the seed if seed enabled!", show_alert=True)
        return
    if user_id != listener.message.from_user.id:
        query.answer(text="𝐓𝐡𝐢𝐬 𝐭𝐚𝐬𝐤 𝐢𝐬 𝐧𝐨𝐭 𝐟𝐨𝐫 𝐲𝐨𝐮!", show_alert=True)
    elif data[1] == "pin":
        query.answer(text=data[3], show_alert=True)
    elif data[1] == "done":
        query.answer()
        id_ = data[3]
        if len(id_) > 20:
            client = dl.client()
            tor_info = client.torrents_info(torrent_hash=id_)[0]
            path = tor_info.content_path.rsplit('/', 1)[0]
            res = client.torrents_files(torrent_hash=id_)
            for f in res:
                if f.priority == 0:
                    f_paths = [f"{path}/{f.name}", f"{path}/{f.name}.!qB"]
                    for f_path in f_paths:
                       if ospath.exists(f_path):
                           try:
                               remove(f_path)
                           except:
                               pass
            client.torrents_resume(torrent_hashes=id_)
        else:
            res = aria2.client.get_files(id_)
            for f in res:
                if f['selected'] == 'false' and ospath.exists(f['path']):
                    try:
                        remove(f['path'])
                    except:
                        pass
            aria2.client.unpause(id_)
        sendStatusMessage(listener.message, listener.bot)
        query.message.delete()


select_handler = CommandHandler(BotCommands.BtSelectCommand, select,
                                filters=(CustomFilters.authorized_chat | CustomFilters.authorized_user), run_async=True)
bts_handler = CallbackQueryHandler(get_confirm, pattern="btsel", run_async=True)
dispatcher.add_handler(select_handler)
dispatcher.add_handler(bts_handler)