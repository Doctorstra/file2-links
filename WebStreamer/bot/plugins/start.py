# (c) @EverythingSuckz | @AbirHasan2005

from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from WebStreamer.utils.human_readable import humanbytes
from WebStreamer.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)


@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started !!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="Sorry Sir, You are Banned to use me. Contact my [👥 Support Group](https://t.me/Dads_links).",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🤖 Join Updates Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="Something went Wrong. Contact my [👥 Support Group](https://t.me/Dads_links).",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text='🙋 ℍ𝕖𝕪 𝔹𝕣𝕦𝕙!!\n𝕀 𝕒𝕞 𝕀𝕟𝕤𝕥𝕒𝕟𝕥 𝕋𝕖𝕝𝕖𝕘𝕣𝕒𝕞 𝔽𝕚𝕝𝕖 𝕥𝕠 𝕃𝕚𝕟𝕜 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔹𝕠𝕥.\n\n𝕊𝕖𝕟𝕕 𝕞𝕖 𝕒𝕟𝕪 𝕗𝕚𝕝𝕖 & 𝕤𝕖𝕖 𝕥𝕙𝕖 𝕞𝕒𝕘𝕚𝕔!',
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('🔊 Channel', url='https://t.me/Dads_links'), InlineKeyboardButton('👥  Support Group', url='https://t.me/Dads_links')],
                    [InlineKeyboardButton('🔥 Developer', url='https://t.me/Dads_links')]
                ]
            ),
            disable_web_page_preview=True
        )
    else:
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="Sorry Sir, You are Banned to use me. Contact my [👥 Support Group](https://t.me/Dads_links).",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🤖 Join Updates Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ],
                            [
                                InlineKeyboardButton("🔄 Refresh / Try Again",
                                                     url=f"https://t.me/Dads_links_file2_links?start=uvindu_br_{usr_cmd}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="Something went Wrong. Contact my [👥 Support Group](https://t.me/Dads_links).",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.message_id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.message_id)

        msg_text = "𝔹𝕣𝕦𝕙! 😁\n𝕐𝕠𝕦𝕣 𝕃𝕚𝕟𝕜 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕖𝕕! 🤓\n\n📂 **𝔽𝕚𝕝𝕖 ℕ𝕒𝕞𝕖:** `{}`\n**𝔽𝕚𝕝𝕖 𝕊𝕚𝕫𝕖:** `{}`\n\n📥 **𝔻𝕠𝕨𝕟𝕝𝕠𝕒𝕕 𝕃𝕚𝕟𝕜:** `{}`"
        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Download Now", url=stream_link)]])
        )


@StreamBot.on_message(filters.command('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="Sorry Sir, You are Banned to use me. Contact my [👥 Support Group](https://t.me/Dads_links).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🤖 Join Updates Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="Something went Wrong. Contact my [👥 Support Group](https://t.me/Dads_links).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="𝕊𝕖𝕟𝕕 𝕞𝕖 𝕒𝕟𝕪 𝔽𝕚𝕝𝕖 𝕀 𝕨𝕚𝕝𝕝 𝕡𝕣𝕠𝕧𝕚𝕕𝕖 𝔼𝕩𝕥𝕖𝕣𝕟𝕒𝕝 𝔻𝕚𝕣𝕖𝕔𝕥 𝔻𝕠𝕨𝕟𝕝𝕠𝕒𝕕 𝕃𝕚𝕟𝕜!\n\n𝔸𝕝𝕤𝕠 𝕀 𝕒𝕞 𝕊𝕦𝕡𝕡𝕠𝕣𝕥𝕖𝕕 𝕚𝕟 ℂ𝕙𝕒𝕟𝕟𝕖𝕝𝕤. 𝔸𝕕𝕕 𝕞𝕖 𝕥𝕠 ℂ𝕙𝕒𝕟𝕟𝕖𝕝 𝕒𝕤 𝔸𝕕𝕞𝕚𝕟 𝕥𝕠 𝕄𝕒𝕜𝕖 𝕄𝕖 𝕎𝕠𝕣𝕜𝕒𝕓𝕝𝕖!",
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("👥 Support Group", url="https://t.me/Dads_links"), InlineKeyboardButton("🔊 Channel", url="https://t.me/Dads_links")],
                [InlineKeyboardButton("🔥 Developer", url="https://t.me/Dads_links")]
            ]
        )
    )
