import logging
from telegram import *
from telegram.ext import *

BOT_TOKEN = "8655830918:AAGoSVFsZdZokmYOBImr-ctOeTBsZeDWkdc" 
ADMIN_ID = 8398525143
ADMIN_USERNAME = "@diyor_wa"
SALES_CHANNEL = "https://t.me/savdolarkanali"

CARD = "8600111133338888"
CARD_NAME = "Eshmatov Toshmat"

logging.basicConfig(level=logging.INFO)
user_orders = {}

# 🔹 Asosiy persistent menu (doim ekranda)
MAIN_MENU = InlineKeyboardMarkup([
    [InlineKeyboardButton("⭐ Stars olish", callback_data="stars"),
     InlineKeyboardButton("💎 Premium olish", callback_data="premium")],
    [InlineKeyboardButton("📢 Reklama xizmati", callback_data="ads"),
     InlineKeyboardButton("📞 Bog'lanish", callback_data="contact")],
    [InlineKeyboardButton("🧾 Savdolar", callback_data="sales")]
])

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "*Starschi Bot ga xush kelibsiz!* 🚀\n\n"
        "_Kerakli xizmatni tanlang:_",
        parse_mode="Markdown",
        reply_markup=MAIN_MENU
    )

# BUTTON HANDLER
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "stars":
        text = "*⭐ Telegram Stars narxlari*"
        kb = [
            [InlineKeyboardButton("50 ta — 13,990 so'm", callback_data="stars_50")],
            [InlineKeyboardButton("100 ta — 25,990 so'm", callback_data="stars_100")],
            [InlineKeyboardButton("250 ta — 59,990 so'm", callback_data="stars_250")],
            [InlineKeyboardButton("500 ta — 109,990 so'm", callback_data="stars_500")]
        ]
        await query.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    
    elif query.data == "premium":
        text = "*💎 Telegram Premium*"
        kb = [
            [InlineKeyboardButton("1 oy — 39,990 so'm", callback_data="premium_1")],
            [InlineKeyboardButton("3 oy — 109,990 so'm", callback_data="premium_3")],
            [InlineKeyboardButton("6 oy — 199,990 so'm", callback_data="premium_6")],
            [InlineKeyboardButton("12 oy — 349,990 so'm", callback_data="premium_12")]
        ]
        await query.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    
    elif query.data == "ads":
        text = "*📢 Reklama xizmati*"
        kb = [
            [InlineKeyboardButton("12 soat — 14,990 so'm", callback_data="ads_12")],
            [InlineKeyboardButton("24 soat — 29,990 so'm", callback_data="ads_24")],
            [InlineKeyboardButton("1 hafta — 99,990 so'm", callback_data="ads_week")],
            [InlineKeyboardButton("1 oy — 339,990 so'm", callback_data="ads_month")]
        ]
        await query.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    
    elif query.data == "contact":
        text = f"*📞 Bog'lanish*\n\nAdmin: {ADMIN_USERNAME}\nQo'llab quvvatlash: +998XXXXXXXXX"
        await query.message.reply_text(text, parse_mode="Markdown")
    
    elif query.data == "sales":
        kb = [[InlineKeyboardButton("📢 Kanalga o'tish", url=SALES_CHANNEL)]]
        await query.message.reply_text("*🧾 Qilingan savdolar va isbotlar shu kanalda!*",
                                     parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    
    # Buyurtma berish inline tugmalari
    elif query.data.startswith("stars_") or query.data.startswith("premium_") or query.data.startswith("ads_"):
        service, val = query.data.split("_")
        user_orders[query.from_user.id] = (service, val)
        price = val.replace("_"," ") + (" so'm" if service!="premium" else " oy")
        text = f"*To'lov ma'lumotlari*\n\nKarta: `{CARD}`\nEga: *{CARD_NAME}*\nSumma: {price}"
        kb = [[InlineKeyboardButton("✅ To'lov qildim", callback_data="paid")]]
        await query.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    
    elif query.data == "paid":
        user = query.from_user
        await context.bot.send_message(
            ADMIN_ID,
            f"*Yangi buyurtma*\n\nUser: @{user.username}\nID: {user.id}\nXizmat: {user_orders.get(user)}",
            parse_mode="Markdown"
        )
        await query.message.reply_text("*To'lov qabul qilindi, sizga 1-6 soat ichida javob beramiz*", parse_mode="Markdown")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))
    app.run_polling()

if __name__ == "__main__":
    main()
