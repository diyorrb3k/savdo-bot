import logging
from telegram import *
from telegram.ext import *

BOT_TOKEN = "8655830918:AAGoSVFsZdZokmYOBImr-ctOeTBsZeDWkdc" 
ADMIN_ID = 8398525143
ADMIN_USERNAME = "@diyor_wa"
SALES_CHANNEL = "https://t.me/savdolarkanali"

CARD = "8600999988880000"
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
    
    # Stars narxlari
    if query.data == "stars":
        text = (
            "*⭐ Telegram Stars narxlari*\n\n"
            "50 ta — *13,990 so'm*\n"
            "100 ta — *25,990 so'm*\n"
            "250 ta — *59,990 so'm*\n"
            "500 ta — *109,990 so'm*"
        )
        kb = [[InlineKeyboardButton("🛒 Buyurtma berish", callback_data="buy_stars")]]
        await query.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    
    # Premium narxlari
    elif query.data == "premium":
        text = (
            "*💎 Telegram Premium*\n\n"
            "1 oy — *39,990 so'm*\n"
            "3 oy — *109,990 so'm*\n"
            "6 oy — *199,990 so'm*\n"
            "12 oy — *349,990 so'm*"
        )
        kb = [[InlineKeyboardButton("🛒 Buyurtma berish", callback_data="buy_premium")]]
        await query.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    
    # Reklama narxlari
    elif query.data == "ads":
        text = (
            "*📢 Reklama xizmati*\n\n"
            "12 soat — *14,990 so'm*\n"
            "24 soat — *29,990 so'm*\n"
            "1 hafta — *99,990 so'm*\n"
            "1 oy — *339,990 so'm*\n\n"
            f"*Batafsil ma’lumot:* {ADMIN_USERNAME}"
        )
        kb = [[InlineKeyboardButton("🛒 Buyurtma qilish", callback_data="buy_ads")]]
        await query.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    
    # Bog'lanish
    elif query.data == "contact":
        text = f"*📞 Bog'lanish*\n\nAdmin: {ADMIN_USERNAME}\nQo'llab quvvatlash: +998XXXXXXXXX"
        await query.message.reply_text(text, parse_mode="Markdown")
    
    # Savdolar
    elif query.data == "sales":
        kb = [[InlineKeyboardButton("📢 Kanalga o'tish", url=SALES_CHANNEL)]]
        await query.message.reply_text("*🧾 Qilingan savdolar va isbotlar shu kanalda!*",
                                     parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    
    # Buyurtma berish uchun step 1
    elif query.data == "buy_stars":
        user_orders[query.from_user.id] = "stars"
        await query.message.reply_text("*Nechta Stars sotib olasiz?*\nMasalan: 100", parse_mode="Markdown")
    
    elif query.data == "buy_premium":
        user_orders[query.from_user.id] = "premium"
        await query.message.reply_text("*Necha oylik Premium kerak?*\nMasalan: 3", parse_mode="Markdown")
    
    elif query.data == "buy_ads":
        kb = [
            [InlineKeyboardButton("12 soat", callback_data="ads_12")],
            [InlineKeyboardButton("24 soat", callback_data="ads_24")],
            [InlineKeyboardButton("1 hafta", callback_data="ads_week")],
            [InlineKeyboardButton("1 oy", callback_data="ads_month")]
        ]
        await query.message.reply_text("*Reklama paketini tanlang:*", parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    
    # Reklama paket tanlanganda
    elif query.data in ["ads_12", "ads_24", "ads_week", "ads_month"]:
        package_prices = {"ads_12":"14,990 so'm","ads_24":"29,990 so'm","ads_week":"99,990 so'm","ads_month":"339,990 so'm"}
        package_names = {"ads_12":"12 soat","ads_24":"24 soat","ads_week":"1 hafta","ads_month":"1 oy"}
        user_orders[query.from_user.id] = ("ads", query.data)
        
        kb = [
            [InlineKeyboardButton("💳 Karta orqali", callback_data="pay_card")],
            [InlineKeyboardButton("📩 Admin orqali", callback_data="pay_admin")]
        ]
        await query.message.reply_text(
            f"*{package_names[query.data]} paketi narxi:* {package_prices[query.data]}\n\n"
            f"Karta: `{CARD}`\nEga: *{CARD_NAME}*",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(kb)
        )
    
    # To'lov tugmalari
    elif query.data in ["pay_card","pay_admin"]:
        await query.message.reply_text("*To'lov qilgach pastdagi tugmani bosing*", parse_mode="Markdown",
                                     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✅ To'lov qildim", callback_data="paid")]]))
    
    # To'lov chek yuborilganda adminga xabar
    elif query.data == "paid":
        user = query.from_user
        await context.bot.send_message(
            ADMIN_ID,
            f"*Yangi buyurtma*\n\nUser: @{user.username}\nID: {user.id}\nXizmat: {user_orders.get(user)}",
            parse_mode="Markdown"
        )
        await query.message.reply_text("*To'lov qabul qilindi, sizga 1-6 soat ichida javob beramiz*", parse_mode="Markdown")

# TEXT HANDLER: Stars va Premium miqdor kiritilganda
async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user.id
    text = update.message.text
    
    if user_orders.get(user) == "stars":
        price = f"{int(text)*259.9} so'm"
        pay_text = f"*To'lov ma'lumotlari*\n\nKarta: {CARD}\nEga: *{CARD_NAME}*\nSumma: {price}"
        kb = [[InlineKeyboardButton("✅ To'lov qildim", callback_data="paid")]]
        await update.message.reply_text(pay_text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    
    elif user_orders.get(user) == "premium":
        months = int(text)
        prices = {1:39990,3:109990,6:199990,12:349990}
        price = f"{prices.get(months, 0)} so'm"
        pay_text = f"*To'lov ma'lumotlari*\n\nKarta: {CARD}\nEga: *{CARD_NAME}*\nSumma: {price}"
        kb = [[InlineKeyboardButton("✅ To'lov qildim", callback_data="paid")]]
        await update.message.reply_text(pay_text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

# PHOTO CHECK HANDLER
async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    await context.bot.send_photo(
        ADMIN_ID,
        update.message.photo[-1].file_id,
        caption=(f"*Yangi buyurtma*\nUser: @{user.username}\nID: {user.id}"),
        parse_mode="Markdown"
    )
    await update.message.reply_text("*To'lov qabul qilindi, sizga 1-6 soat ichida javob beramiz*", parse_mode="Markdown")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))
    app.add_handler(MessageHandler(filters.PHOTO, photo_handler))
    app.run_polling()

if __name__ == "__main__":
    main()
