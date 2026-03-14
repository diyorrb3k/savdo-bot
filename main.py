import logging
from telegram import *
from telegram.ext import *

BOT_TOKEN = "8655830918:AAGoSVFsZdZokmYOBImr-ctOeTBsZeDWkdc"
ADMIN_ID = 8398525143
ADMIN_USERNAME = "@diyor_wa"
SALES_CHANNEL = "https://t.me/savdolarkanali"

CARD = "8600666688881111"
CARD_NAME = "Eshmatov Toshmat"

logging.basicConfig(level=logging.INFO)

user_orders = {}

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("⭐ Stars olish", callback_data="stars")],
        [InlineKeyboardButton("💎 Premium olish", callback_data="premium")],
        [InlineKeyboardButton("📢 Reklama xizmati", callback_data="ads")],
        [InlineKeyboardButton("📞 Bog'lanish", callback_data="contact")],
        [InlineKeyboardButton("🧾 Savdolar", callback_data="sales")]
    ]

    await update.message.reply_text(
        "*Starschi Bot ga xush kelibsiz!* 🚀\n\n"
        "_Kerakli xizmatni tanlang:_",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# BUTTON HANDLER
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "stars":

        text = (
            "*⭐ Telegram Stars narxlari*\n\n"
            "`50 ta` — *13,990 so'm*\n"
            "`100 ta` — *25,990 so'm*\n"
            "`250 ta` — *59,990 so'm*\n"
            "`500 ta` — *109,990 so'm*\n\n"
            "_Eng tez va ishonchli xizmat!_"
        )

        kb = [[InlineKeyboardButton("🛒 Buyurtma berish", callback_data="buy_stars")]]

        await query.message.edit_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))


    elif query.data == "premium":

        text = (
            "*💎 Telegram Premium*\n\n"
            "`1 oy` — *39,990 so'm*\n"
            "`3 oy` — *109,990 so'm*\n"
            "`6 oy` — *199,990 so'm*\n"
            "`12 oy` — *349,990 so'm*\n\n"
            "_Premium bilan Telegramdan maksimal foydalaning!_"
        )

        kb = [[InlineKeyboardButton("🛒 Buyurtma berish", callback_data="buy_premium")]]

        await query.message.edit_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))


    elif query.data == "ads":

        text = (
            "*📢 Reklama xizmati*\n\n"
            "*Avto habar bilan reklama*\n\n"
            "`12 soat` — *14,990 so'm*\n"
            "`24 soat` — *29,990 so'm*\n"
            "`1 hafta` — *99,990 so'm*\n"
            "`1 oy` — *339,990 so'm*\n\n"
            "*Batafsil:* "
            f"{ADMIN_USERNAME}"
        )

        kb = [[InlineKeyboardButton("🛒 Buyurtma qilish", callback_data="buy_ads")]]

        await query.message.edit_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))


    elif query.data == "contact":

        text = (
            "*📞 Bog'lanish*\n\n"
            f"Admin: {ADMIN_USERNAME}\n"
            "Qo'llab quvvatlash: +998XXXXXXXXX"
        )

        await query.message.edit_text(text, parse_mode="Markdown")


    elif query.data == "sales":

        kb = [[InlineKeyboardButton("📢 Kanalga o'tish", url=SALES_CHANNEL)]]

        await query.message.edit_text(
            "*🧾 Qilingan savdolar va isbotlar shu kanalda!*",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(kb)
        )

    elif query.data == "buy_stars":

        user_orders[query.from_user.id] = "stars"

        await query.message.reply_text(
            "*Nechta Stars sotib olasiz?*\n\n"
            "_Masalan:_ `100`",
            parse_mode="Markdown"
        )


    elif query.data == "buy_premium":

        user_orders[query.from_user.id] = "premium"

        await query.message.reply_text(
            "*Necha oylik Premium kerak?*\n\n"
            "_Masalan:_ `3`",
            parse_mode="Markdown"
        )


    elif query.data == "buy_ads":

        kb = [
            [InlineKeyboardButton("12 soat", callback_data="ads_12")],
            [InlineKeyboardButton("24 soat", callback_data="ads_24")],
            [InlineKeyboardButton("1 hafta", callback_data="ads_week")],
            [InlineKeyboardButton("1 oy", callback_data="ads_month")]
        ]

        await query.message.reply_text(
            "*Reklama paketini tanlang:*",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(kb)
        )


# TEXT MESSAGE
async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user.id
    text = update.message.text

    if user_orders.get(user) == "stars":

        price = "25,990 so'm"

        pay_text = (
            "*To'lov ma'lumotlari*\n\n"
            f"Karta: `{CARD}`\n"
            f"Ega: *{CARD_NAME}*\n\n"
            f"*Summa:* {price}\n\n"
            "_To'lov qilgach pastdagi tugmani bosing._"
        )

        kb = [[InlineKeyboardButton("✅ To'lov qildim", callback_data="paid")]]

        await update.message.reply_text(pay_text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))


    elif user_orders.get(user) == "premium":

        price = "109,990 so'm"

        pay_text = (
            "*To'lov ma'lumotlari*\n\n"
            f"Karta: `{CARD}`\n"
            f"Ega: *{CARD_NAME}*\n\n"
            f"*Summa:* {price}\n\n"
            "_To'lov qilgach tugmani bosing._"
        )

        kb = [[InlineKeyboardButton("✅ To'lov qildim", callback_data="paid")]]

        await update.message.reply_text(pay_text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))


# CHECK
async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user

    await context.bot.send_photo(
        ADMIN_ID,
        update.message.photo[-1].file_id,
        caption=(
            "*Yangi buyurtma*\n\n"
            f"User: @{user.username}\n"
            f"ID: `{user.id}`"
        ),
        parse_mode="Markdown"
    )

    await update.message.reply_text(
        "*To'lov qabul qilindi.*\n\n"
        "_1-6 soat ichida javob beramiz._",
        parse_mode="Markdown"
    )


def main():

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))
    app.add_handler(MessageHandler(filters.TEXT, text_handler))
    app.add_handler(MessageHandler(filters.PHOTO, photo_handler))

    app.run_polling()


if __name__ == "__main__":
    main()