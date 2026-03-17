import logging
from telegram import *
from telegram.ext import *

BOT_TOKEN = "8655830918:AAGoSVFsZdZokmYOBImr-ctOeTBsZeDWkdc"
ADMIN_ID = 8398525143
ADMIN_USERNAME = "@diyor_wa"
SALES_CHANNEL = "https://t.me/savdolarkanali"

CARD = "8600666677770000"
CARD_NAME = "Eshmatov Toshmat"

logging.basicConfig(level=logging.INFO)
user_orders = {}
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
        "*Starschi Bot ga xush kelibsiz!* 🚀\n\n"
        "_Kerakli xizmatni tanlang:_",
        parse_mode="Markdown",
        reply_markup=MAIN_MENU
    )

async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "⭐ Stars olish":
        kb = [
            [InlineKeyboardButton("50 ta — 13,990 so'm", callback_data="stars_50")],
            [InlineKeyboardButton("100 ta — 25,990 so'm", callback_data="stars_100")],
            [InlineKeyboardButton("250 ta — 59,990 so'm", callback_data="stars_250")],
            [InlineKeyboardButton("500 ta — 109,990 so'm", callback_data="stars_500")]
        ]

        await update.message.reply_text(
            "*⭐ Telegram Stars narxlari*",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(kb)
        )

    elif text == "💎 Premium olish":
        kb = [
            [InlineKeyboardButton("1 oy — 39,990 so'm", callback_data="premium_1")],
            [InlineKeyboardButton("3 oy — 109,990 so'm", callback_data="premium_3")],
            [InlineKeyboardButton("6 oy — 199,990 so'm", callback_data="premium_6")],
            [InlineKeyboardButton("12 oy — 349,990 so'm", callback_data="premium_12")]
        ]

        await update.message.reply_text(
            "*💎 Telegram Premium*",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(kb)
        )

    elif text == "📢 Reklama xizmati":
        kb = [
            [InlineKeyboardButton("12 soat — 14,990 so'm", callback_data="ads_12")],
            [InlineKeyboardButton("24 soat — 29,990 so'm", callback_data="ads_24")],
            [InlineKeyboardButton("1 hafta — 99,990 so'm", callback_data="ads_week")],
            [InlineKeyboardButton("1 oy — 339,990 so'm", callback_data="ads_month")]
        ]

        await update.message.reply_text(
            "*📢 Reklama xizmati*",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(kb)
        )

    elif text == "📞 Bog'lanish":

        kb = [
            [InlineKeyboardButton("👤 Admin bilan yozish", url=f"https://t.me/{ADMIN_USERNAME.replace('@','')}")]
        ]

        await update.message.reply_text(
            "*📞 Bog'lanish*\n\n"
            "Savollar yoki buyurtma bo'yicha admin bilan bog'laning.",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(kb)
        )

    elif text == "🧾 Savdolar":
        kb = [[InlineKeyboardButton("Kanalga o'tish", url=SALES_CHANNEL)]]

        await update.message.reply_text(
            "*🧾 Qilingan savdolar va isbotlar shu kanalda!*",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(kb)
        )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data.startswith("stars_") or query.data.startswith("premium_") or query.data.startswith("ads_"):
        service, val = query.data.split("_")

        user_orders[query.from_user.id] = (service, val)

        kb = [
            [InlineKeyboardButton("👤 Admin orqali", url=f"https://t.me/{ADMIN_USERNAME.replace('@','')}")],
            [InlineKeyboardButton("💳 Karta orqali", callback_data="card")]
        ]

        await query.message.reply_text(
            "*Qaysi uslubda to'laysiz?*",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(kb)
        )

    elif query.data == "card":

        text = (
            "*To'lov ma'lumotlari*\n\n"
            f"Karta: `{CARD}`\n"
            f"Ega: *{CARD_NAME}*"
        )

        kb = [[InlineKeyboardButton("✅ To'lov qildim", callback_data="paid")]]

        await query.message.reply_text(
            text,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(kb)
        )

    elif query.data == "paid":

        waiting_check.add(query.from_user.id)

        await query.message.reply_text(
            "*Iltimos to'lov chekini yuboring*",
            parse_mode="Markdown"
        )

async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user

    if user.id in waiting_check:

        order = user_orders.get(user.id)

        await context.bot.forward_message(
            ADMIN_ID,
            update.message.chat.id,
            update.message.message_id
        )

        await context.bot.send_message(
            ADMIN_ID,
            "*Yangi buyurtma*\n\n"
            f"User: @{user.username}\n"
            f"ID: {user.id}\n"
            f"Xizmat: {order}",
            parse_mode="Markdown"
        )

        waiting_check.remove(user.id)

        await update.message.reply_text(
            "*Chek qabul qilindi. Admin tekshiradi.*",
            parse_mode="Markdown"
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
