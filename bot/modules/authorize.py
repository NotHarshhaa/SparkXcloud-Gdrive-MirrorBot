from bot import AUTHORIZED_CHATS, SUDO_USERS, dispatcher, DB_URI
from bot.helper.telegram_helper.message_utils import sendMessage
from telegram.ext import CommandHandler
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.ext_utils.db_handler import DbManger


def authorize(update, context):
    reply_message = None
    message_ = None
    reply_message = update.message.reply_to_message
    message_ = update.message.text.split(' ')
    if len(message_) == 2:
        user_id = int(message_[1])
        if user_id in AUTHORIZED_CHATS:
            msg = '𝐔𝐬𝐞𝐫 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝! 💃'
        elif DB_URI is not None:
            msg = DbManger().user_auth(user_id)
            AUTHORIZED_CHATS.add(user_id)
        else:
            AUTHORIZED_CHATS.add(user_id)
            msg = '𝐔𝐬𝐞𝐫 𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝'
    elif reply_message is None:
        # Trying to authorize a chat
        chat_id = update.effective_chat.id
        if chat_id in AUTHORIZED_CHATS:
            msg = '𝐂𝐡𝐚𝐭 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝! ♨'
        elif DB_URI is not None:
            msg = DbManger().user_auth(chat_id)
            AUTHORIZED_CHATS.add(chat_id)
        else:
            AUTHORIZED_CHATS.add(chat_id)
            msg = '𝐂𝐡𝐚𝐭 𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝'
    else:
        # Trying to authorize someone by replying
        user_id = reply_message.from_user.id
        if user_id in AUTHORIZED_CHATS:
            msg = '𝐔𝐬𝐞𝐫 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝! 💃'
        elif DB_URI is not None:
            msg = DbManger().user_auth(user_id)
            AUTHORIZED_CHATS.add(user_id)
        else:
            AUTHORIZED_CHATS.add(user_id)
            msg = '𝐔𝐬𝐞𝐫 𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 💮'
    sendMessage(msg, context.bot, update.message)

def unauthorize(update, context):
    reply_message = None
    message_ = None
    reply_message = update.message.reply_to_message
    message_ = update.message.text.split(' ')
    if len(message_) == 2:
        user_id = int(message_[1])
        if user_id in AUTHORIZED_CHATS:
            if DB_URI is not None:
                msg = DbManger().user_unauth(user_id)
            else:
                msg = '𝐔𝐬𝐞𝐫 𝐔𝐧𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 💮'
            AUTHORIZED_CHATS.remove(user_id)
        else:
            msg = '𝐔𝐬𝐞𝐫 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐔𝐧𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝!☠️'
    elif reply_message is None:
        # Trying to unauthorize a chat
        chat_id = update.effective_chat.id
        if chat_id in AUTHORIZED_CHATS:
            if DB_URI is not None:
                msg = DbManger().user_unauth(chat_id)
            else:
                msg = '𝐂𝐡𝐚𝐭 𝐔𝐧𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 ♨'
            AUTHORIZED_CHATS.remove(chat_id)
        else:
            msg = '𝐂𝐡𝐚𝐭 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐔𝐧𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝!☠️'
    else:
        # Trying to authorize someone by replying
        user_id = reply_message.from_user.id
        if user_id in AUTHORIZED_CHATS:
            if DB_URI is not None:
                msg = DbManger().user_unauth(user_id)
            else:
                msg = '𝐔𝐬𝐞𝐫 𝐔𝐧𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 🔥'
            AUTHORIZED_CHATS.remove(user_id)
        else:
            msg = '𝐔𝐬𝐞𝐫 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐔𝐧𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝! 🔥'
    sendMessage(msg, context.bot, update.message)

def addSudo(update, context):
    reply_message = None
    message_ = None
    reply_message = update.message.reply_to_message
    message_ = update.message.text.split(' ')
    if len(message_) == 2:
        user_id = int(message_[1])
        if user_id in SUDO_USERS:
            msg = '𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐒𝐮𝐝𝐨! 🤔'
        elif DB_URI is not None:
            msg = DbManger().user_addsudo(user_id)
            SUDO_USERS.add(user_id)
        else:
            SUDO_USERS.add(user_id)
            msg = '𝐏𝐫𝐨𝐦𝐨𝐭𝐞𝐝 𝐚𝐬 𝐒𝐮𝐝𝐨 🤣'
    elif reply_message is None:
        msg = "𝐆𝐢𝐯𝐞 𝐈𝐃 𝐨𝐫 𝐑𝐞𝐩𝐥𝐲 𝐓𝐨 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐨𝐟 𝐰𝐡𝐨𝐦 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐏𝐫𝐨𝐦𝐨𝐭𝐞."
    else:
        # Trying to authorize someone by replying
        user_id = reply_message.from_user.id
        if user_id in SUDO_USERS:
            msg = '𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐒𝐮𝐝𝐨! 🤔'
        elif DB_URI is not None:
            msg = DbManger().user_addsudo(user_id)
            SUDO_USERS.add(user_id)
        else:
            SUDO_USERS.add(user_id)
            msg = '𝐏𝐫𝐨𝐦𝐨𝐭𝐞𝐝 𝐚𝐬 𝐒𝐮𝐝𝐨 🤣'
    sendMessage(msg, context.bot, update.message)

def removeSudo(update, context):
    reply_message = None
    message_ = None
    reply_message = update.message.reply_to_message
    message_ = update.message.text.split(' ')
    if len(message_) == 2:
        user_id = int(message_[1])
        if user_id in SUDO_USERS:
            if DB_URI is not None:
                msg = DbManger().user_rmsudo(user_id)
            else:
                msg = '𝐃𝐞𝐦𝐨𝐭𝐞𝐝 😅'
            SUDO_USERS.remove(user_id)
        else:
            msg = '𝐍𝐨𝐭 𝐬𝐮𝐝𝐨 𝐮𝐬𝐞𝐫 𝐭𝐨 𝐝𝐞𝐦𝐨𝐭𝐞! 😅'
    elif reply_message is None:
        msg = "𝐆𝐢𝐯𝐞 𝐈𝐃 𝐨𝐫 𝐑𝐞𝐩𝐥𝐲 𝐓𝐨 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐨𝐟 𝐰𝐡𝐨𝐦 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐫𝐞𝐦𝐨𝐯𝐞 𝐟𝐫𝐨𝐦 𝐒𝐮𝐝𝐨"
    else:
        user_id = reply_message.from_user.id
        if user_id in SUDO_USERS:
            if DB_URI is not None:
                msg = DbManger().user_rmsudo(user_id)
            else:
                msg = '𝐃𝐞𝐦𝐨𝐭𝐞𝐝 💌'
            SUDO_USERS.remove(user_id)
        else:
            msg = '𝐍𝐨𝐭 𝐬𝐮𝐝𝐨 𝐮𝐬𝐞𝐫 𝐭𝐨 𝐝𝐞𝐦𝐨𝐭𝐞! 💌'
    sendMessage(msg, context.bot, update.message)

def sendAuthChats(update, context):
    user = sudo = ''
    user += '\n'.join(f"<code>{uid}</code>" for uid in AUTHORIZED_CHATS)
    sudo += '\n'.join(f"<code>{uid}</code>" for uid in SUDO_USERS)
    sendMessage(f'<b><u>𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 𝐂𝐡𝐚𝐭𝐬 💃:</u></b>\n{user}\n<b><u>𝐒𝐮𝐝𝐨 𝐔𝐬𝐞𝐫𝐬:</u></b>\n{sudo}', context.bot, update.message)


send_auth_handler = CommandHandler(command=BotCommands.AuthorizedUsersCommand, callback=sendAuthChats,
                                    filters=CustomFilters.owner_filter | CustomFilters.sudo_user, run_async=True)
authorize_handler = CommandHandler(command=BotCommands.AuthorizeCommand, callback=authorize,
                                    filters=CustomFilters.owner_filter | CustomFilters.sudo_user, run_async=True)
unauthorize_handler = CommandHandler(command=BotCommands.UnAuthorizeCommand, callback=unauthorize,
                                    filters=CustomFilters.owner_filter | CustomFilters.sudo_user, run_async=True)
addsudo_handler = CommandHandler(command=BotCommands.AddSudoCommand, callback=addSudo,
                                    filters=CustomFilters.owner_filter, run_async=True)
removesudo_handler = CommandHandler(command=BotCommands.RmSudoCommand, callback=removeSudo,
                                    filters=CustomFilters.owner_filter, run_async=True)

dispatcher.add_handler(send_auth_handler)
dispatcher.add_handler(authorize_handler)
dispatcher.add_handler(unauthorize_handler)
dispatcher.add_handler(addsudo_handler)
dispatcher.add_handler(removesudo_handler)