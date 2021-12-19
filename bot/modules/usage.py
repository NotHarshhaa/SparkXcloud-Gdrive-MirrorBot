import math

import requests
import heroku3

from bot import dispatcher, HEROKU_APP_NAME, HEROKU_API_KEY
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.message_utils import sendMessage
from telegram import update
from telegram.ext import CommandHandler


def dyno_usage(update, context):
    heroku_api = "https://api.heroku.com"
    if HEROKU_API_KEY is not None and HEROKU_APP_NAME is not None:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        sendMessage(
            "𝐏𝐥𝐞𝐚𝐬𝐞 𝐢𝐧𝐬𝐞𝐫𝐭 𝐲𝐨𝐮𝐫 𝐇𝐄𝐑𝐎𝐊𝐔_𝐀𝐏𝐏_𝐍𝐀𝐌𝐄 𝐚𝐧𝐝 𝐇𝐄𝐑𝐎𝐊𝐔_𝐀𝐏𝐈_𝐊𝐄𝐘 𝐢𝐧 𝐕𝐚𝐫𝐬",
            context.bot,
            update
        )
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/81.0.4044.117 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    session = requests.Session()
    with session as ses:
        with ses.get(heroku_api + path, headers=headers) as r:
            result = r.json()
            """Account Quota."""
            quota = result["account_quota"]
            quota_used = result["quota_used"]
            quota_remain = quota - quota_used
            quota_percent = math.floor(quota_remain / quota * 100)
            minutes_remain = quota_remain / 60
            hours = math.floor(minutes_remain / 60)
            minutes = math.floor(minutes_remain % 60)
            day = math.floor(hours / 24)

            """App Quota."""
            Apps = result["apps"]
            for apps in Apps:
                if apps.get("app_uuid") == app.id:
                    AppQuotaUsed = apps.get("quota_used") / 60
                    AppPercent = math.floor(apps.get("quota_used") * 100 / quota)
                    break
            else:
                AppQuotaUsed = 0
                AppPercent = 0

            AppHours = math.floor(AppQuotaUsed / 60)
            AppMinutes = math.floor(AppQuotaUsed % 60)

            sendMessage(
                f"<b>ℹ️ 𝐃𝐲𝐧𝐨 𝐔𝐬𝐚𝐠𝐞 ℹ️</b>\n\n<code>App name:{app.name}</code>\n"
                f"🕐 <code>{AppHours}</code> <b>Hours</b> <code>{AppMinutes}</code> <b>Minutes\nPercentage: {AppPercent}%</b>\n\n"
                "<b>⚠️ 𝐃𝐲𝐧𝐨 𝐑𝐞𝐦𝐚𝐢𝐧𝐢𝐧𝐠 ⚠️</b>\n"
                f"🕐 <code>{hours}</code> <b>Hours </b> <code>{minutes}</code> <b>Minutes\nPercentage: {quota_percent}%</b>\n\n"
                "<b>❌ 𝐄𝐬𝐭𝐢𝐦𝐚𝐭𝐞𝐝 𝐄𝐱𝐩𝐢𝐫𝐞𝐝 ❌</b>\n"
                f"📅 <code>{day}</code> <b>Days</b>",
                f"<b>👏 𝐂𝐫𝐞𝐝𝐢𝐭𝐬 : 𝐒𝐩𝐚𝐫𝐤𝐱𝐂𝐥𝐨𝐮𝐝 👏</b>\n"
                context.bot,
                update
            )
            return True


dyno_usage_handler = CommandHandler(command=BotCommands.UsageCommand, callback=dyno_usage,
                                    filters=CustomFilters.owner_filter | CustomFilters.sudo_user, run_async=True)

dispatcher.add_handler(dyno_usage_handler)