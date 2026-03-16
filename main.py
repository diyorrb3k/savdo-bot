import logging
from telegram import *
from telegram.ext import *

BOT_TOKEN = "8655830918:AAGoSVFsZdZokmYOBImr-ctOeTBsZeDWkdc"

ADMIN_ID = 8398525143
ADMIN_USERNAME = "@diyor_wa"

CARD = "8600666677774444"
CARD_NAME = "Eshmatov Toshmat"

logging.basicConfig(level=logging.INFO)

orders = {}
waiting_check = set()

MAIN_MENU = ReplyKeyboardMarkup(
    [
        ["⭐ Stars olish", "💎 Premium olish"],
        ["📢 Reklama xizmati", "📞 Bog'lanish"],
        ["🧾 Savdolar"]
    ],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⭐ *Starschi Bot ga xush kelibsiz!*",
        parse_mode="Markdown",
        reply_markup=MAIN_MENU
    )


async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "⭐ Stars olish":

        kb = [
            [InlineKeyboardButton("50 ta", callback_data="stars_50")],
            [InlineKeyboardButton("100 ta", callback_data="stars_100")],
            [InlineKeyboardButton("250 ta", callback_data="stars_250")],
        ]

        await update.message.reply_text(
            "⭐ Stars paketini tanlang",
            reply_markup=InlineKeyboardMarkup(kb)
        )

    elif text == "💎 Premium olish":

        kb = [
            [InlineKeyboardButton("1 oy", callback_data="premium_1")],
            [InlineKeyboardButton("3 oy", callback_data="premium_3")],
            [InlineKeyboardButton("12 oy", callback_data="premium_12")]
        ]

        await update.message.reply_text(
            "💎 Premium paketini tanlang",
            reply_markup=InlineKeyboardMarkup(kb)
        )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    data = query.data
    user_id = query.from_user.id

    if data.startswith("stars") or data.startswith("premium"):

        orders[user_id] = data

        kb = [
            [InlineKeyboardButton("👤 Admin orqali", callback_data="adminpay")],
            [InlineKeyboardButton("💳 Karta orqali", callback_data="cardpay")]
        ]

        await query.message.reply_text(
            "💰 *Qaysi uslubda to'laysiz?*",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(kb)
        )


    elif data == "adminpay":

        kb = [
            [InlineKeyboardButton("Admin ga yozish", url=f"https://t.me/{ADMIN_USERNAME.replace('@','')}")]
        ]

        await query.message.reply_text(
            "Admin orqali to'lov uchun yozing 👇",
            reply_markup=InlineKeyboardMarkup(kb)
        )


    elif data == "cardpay":

        kb = [
            [InlineKeyboardButton("✅ To'lov qildim", callback_data="paid")]
        ]

        await query.message.reply_text(
            f"💳 *Karta orqali to'lov*\n\n"
            f"Karta: `{CARD}`\n"
            f"Ega: *{CARD_NAME}*\n\n"
            f"To'lov qilib pastdagi tugmani bosing",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(kb)
        )


    elif data == "paid":

        waiting_check.add(user_id)

        await query.message.reply_text(
            "📸 Iltimos to'lov chekini yuboring"
        )


async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user

    if user.id in waiting_check:

        await context.bot.forward_message(
            ADMIN_ID,
            update.message.chat.id,
            update.message.message_id
        )

        await context.bot.send_message(
            ADMIN_ID,
            f"Yangi to'lov cheki\nUser: @{user.username}\nID: {user.id}"
        )

        waiting_check.remove(user.id)

        await update.message.reply_text(
            "✅ Chek qabul qilindi\nAdmin tekshiradi."
        )


def main():

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))

    app.add_handler(CallbackQueryHandler(buttons))

    app.add_handler(MessageHandler(filters.PHOTO, photo_handler))

    app.run_polling()


if __name__ == "__main__":
    main()
