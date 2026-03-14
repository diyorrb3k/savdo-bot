import logging
from telegram import *
from telegram.ext import *

BOT_TOKEN = "8655830918:AAGoSVFsZdZokmYOBImr-ctOeTBsZeDWkdc"
ADMIN_ID = 8398525143
ADMIN_USERNAME = "@diyor_wa"
SALES_CHANNEL = "https://t.me/savdolarkanali"

CARD = "8600454566778804"
CARD_NAME = "Abdurashidov Shahzod"

logging.basicConfig(level=logging.INFO)
user_orders = {}

# 🔹 Asosiy persistent menu (doim ekranda)
MAIN_MENU = InlineKeyboardMarkup([
    [InlineKeyboardButton("⭐️ Stars olish", callback_data="stars"),
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
            "*⭐️ Telegram Stars narxlari*\n\n"
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
        await query.message.reply_text("*Reklama paketini tanlang:*", parse_mode="Markdown",
