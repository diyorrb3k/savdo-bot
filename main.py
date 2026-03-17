from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# ✅ TOKENNI SHU YERGA QO'YASAN (BotFather token)
import os
TOKEN = os.getenv("BOT_TOKEN")  # BotFather tokenini shu Environment Variable orqali o‘qiydi

ADMIN_ID = 8398525143   # admin telegram id

# Admin kontakt
ADMIN_USERNAME = "@diyor_WA"
ADMIN_PHONE = "+998881077333"

# buyurtma va admin-contact holatini saqlash
order_mode = {}
contact_mode = {}

# ✅ 5 ta knopka (o'zgarmaydi)
keyboard = [
    ["👨 Erkaklar atirlari", "👩 Ayollar atirlari"],
    ["🔥 Chegirmalar", "📦 Buyurtma berish"],
    ["📞 Admin bilan bog‘lanish"]
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# ====== RASMLAR ======
IMG_DIOR_SAUVAGE = "https://elcos.uz/static/siteApp/media/f3bfe6a4-0d7a-4142-8795-025eeec8267b.jpg"
IMG_LV_IMAGINATION = "https://olcha.uz/image/700x700/products/2022-03-10/louis-vuitton-imagination-edp-u-100ml-original-39821-0.jpeg"
IMG_BLEU_DE_CHANEL = "https://olcha.uz/image/700x700/products/2022-02-07/chanel-bleu-de-chanel-edp-100ml-original-35443-0.jpeg"

IMG_GUCCI_FLORA = "https://dutyfree.uz/thumb/2/IRc9N72JVJ25TfdcZZ5qbg/r/d/2_438.jpg"
IMG_BACCARAT = "https://www.prom.uz/_ipx/f_webp/https://devel.prom.uz/upload/product_logos/77/bd/77bd370d9652e9d406d11823b98c564a.jpg"
IMG_CHANEL_CHANCE = "https://elisium.uz/thumb/2/NvF66IHxlQmn-lqMwhWOcw/r/d/chance-eau-de-toilette-spray-3-4fl-oz_packshot-default-126460-8841593683998-scale-2_00x.jpg"


# MarkdownV2 xatolarini oldini olish uchun escape (o'zgarmaydi)
def esc(text: str) -> str:
    if text is None:
        return ""
    for ch in r"\_*[]()~`>#+-=|{}.!":
        text = text.replace(ch, f"\\{ch}")
    return text


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "Assalomu alaykum\\! 👋\n\n"
        "✨ *Atirlar Dunyosi* botiga xush kelibsiz 🧴\n\n"
        "Quyidagi bo‘limlardan birini tanlang 👇"
    )
    await update.message.reply_text(
        msg,
        reply_markup=reply_markup,
        parse_mode="MarkdownV2"
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text or ""
    user = update.message.from_user
    user_id = user.id
    chat_id = update.effective_chat.id

    # ===== ERKAKLAR ATIRLARI =====
    if text == "👨 Erkaklar atirlari":

        caption1 = (
            "🧴 *Dior Sauvage* 🌿\n"
            "━━━━━━━━━━━━━━\n"
            "🔥 Erkaklar orasida *TOP hit*\n"
            "🌪 Kuchli, jozibali va universal hid\n\n"
            "💰 *Narxi:* *420,000 so‘m*\n"
            "⏳ *Stoyka:* 8–12 soat\n"
            "🎁 *Bonus:* bepul upakovka\n\n"
            "📦 Buyurtma uchun: *Buyurtma berish* tugmasini bosing 👇"
        )
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=IMG_DIOR_SAUVAGE,
            caption=esc(caption1),
            parse_mode="MarkdownV2"
        )

        caption2 = (
            "🧴 *Louis Vuitton Imagination* 🍋\n"
            "━━━━━━━━━━━━━━\n"
            "✨ *Fresh & luxury* segment\n"
            "🌟 Trenddagi eng yoqimli hidlardan biri\n\n"
            "💰 *Narxi:* *470,000 so‘m*\n"
            "⏳ *Stoyka:* 10–12 soat\n"
            "🚚 *Yetkazib berish:* bor\n\n"
            "📦 Buyurtma uchun: *Buyurtma berish* tugmasini bosing 👇"
        )
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=IMG_LV_IMAGINATION,
            caption=esc(caption2),
            parse_mode="MarkdownV2"
        )

        caption3 = (
            "🧴 *Bleu de Chanel* 🌊\n"
            "━━━━━━━━━━━━━━\n"
            "🎩 Elegant & classic — *premium tanlov*\n"
            "💎 Ofis, uchrashuv, har kuni uchun mos\n\n"
            "💰 *Narxi:* *450,000 so‘m*\n"
            "⏳ *Stoyka:* 8–10 soat\n"
            "✅ *Sovg‘aga ham ideal*\n\n"
            "📦 Buyurtma uchun: *Buyurtma berish* tugmasini bosing 👇"
        )
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=IMG_BLEU_DE_CHANEL,
            caption=esc(caption3),
            parse_mode="MarkdownV2"
        )

    # ===== AYOLLAR ATIRLARI =====
    elif text == "👩 Ayollar atirlari":

        caption1 = (
            "🌸 *Chanel Chance* 💎\n"
            "━━━━━━━━━━━━━━\n"
            "✨ Nafis va klassik ayollar atiri\n"
            "💃 Kundalik va bayram uchun mos\n\n"
            "💰 *Narxi:* *430,000 so‘m*\n"
            "⏳ *Stoyka:* 7–10 soat\n"
            "🎁 *Bonus:* bepul upakovka\n\n"
            "📦 Buyurtma uchun: *Buyurtma berish* tugmasini bosing 👇"
        )
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=IMG_CHANEL_CHANCE,
            caption=esc(caption1),
            parse_mode="MarkdownV2"
        )

        caption2 = (
            "🌺 *Gucci Flora* 🌷\n"
            "━━━━━━━━━━━━━━\n"
            "💕 Gulli va yumshoq aroma\n"
            "🌸 Juda yoqimli, ayollarga mos\n\n"
            "💰 *Narxi:* *390,000 so‘m*\n"
            "⏳ *Stoyka:* 6–9 soat\n"
            "🚚 *Yetkazib berish:* bor\n\n"
            "📦 Buyurtma uchun: *Buyurtma berish* tugmasini bosing 👇"
        )
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=IMG_GUCCI_FLORA,
            caption=esc(caption2),
            parse_mode="MarkdownV2"
        )

        caption3 = (
            "🔥 *Baccarat Rouge 540* 💎\n"
            "━━━━━━━━━━━━━━\n"
            "👑 Premium segment — *status hidi*\n"
            "✨ Juda kuchli va esda qoladigan aroma\n\n"
            "💰 *Narxi:* *490,000 so‘m*\n"
            "⏳ *Stoyka:* 10–14 soat\n"
            "✅ *Sovg‘aga TOP*\n\n"
            "📦 Buyurtma uchun: *Buyurtma berish* tugmasini bosing 👇"
        )
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=IMG_BACCARAT,
            caption=esc(caption3),
            parse_mode="MarkdownV2"
        )

    # ===== CHEGIRMALAR =====
    elif "Chegirmalar" in text:
        msg = (
            "🔥 *Bugungi chegirmalar* 💸\n"
            "━━━━━━━━━━━━━━\n\n"
            "✅ *Louis Vuitton Imagination* — *-20%*\n"
            "✅ *Dior Sauvage* — *-15%*\n\n"
            "⏳ Aksiya bugun amal qiladi\\!\n"
            "📦 Buyurtma: *Buyurtma berish* 👇"
        )
        await update.message.reply_text(
            msg,
        )

    # ===== BUYURTMA BOSHLASH =====
    elif text == "📦 Buyurtma berish":
        order_mode[user_id] = True

        msg = (
            "📦 *Buyurtma berish* 🛒\n"
            "━━━━━━━━━━━━━━\n\n"
            "Iltimos, quyidagilarni *bitta xabarda* yuboring:\n\n"
            "👤 Ism:\n"
            "📞 Telefon:\n"
            "🧴 Qaysi atir:\n"
            "📏 Hajmi \\(50ml / 100ml\\):\n"
            "📍 Manzil:\n\n"
            "✅ Yuborganingizdan so‘ng buyurtma adminga ketadi\\."
        )
        await update.message.reply_text(
            msg,
            parse_mode="MarkdownV2"
        )

    # ===== ADMIN BILAN BOG'LANISH =====
    elif text == "📞 Admin bilan bog‘lanish":
        contact_mode[user_id] = True

        msg = (
            "📞 *Admin bilan bog‘lanish*\n"
            "━━━━━━━━━━━━━━\n\n"
            f"👤 Admin: {esc(ADMIN_USERNAME)}\n"
            f"📱 Telefon: {esc(ADMIN_PHONE)}\n\n"
            "✍️ Savolingizni yozing — men adminga yuboraman\\.\n"
            "🕒 Tez orada javob beriladi\\."
        )
        await update.message.reply_text(
            msg,
            parse_mode="MarkdownV2"
        )

    # ===== BUYURTMA ADMIN GA BORADI =====
    elif user_id in order_mode:
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"🛒 Yangi buyurtma!\n\n{text}\n\n👤 User: {user.first_name} | ID: {user_id}"
        )

        msg = (
            "✅ *Buyurtmangiz qabul qilindi\\!* 🎉\n"
            "━━━━━━━━━━━━━━\n"
            "⏱️ Admin tez orada siz bilan bog‘lanadi\\.\n\n"
            "🙂 Menyudan davom etishingiz mumkin 👇"
        )
        await update.message.reply_text(
            msg,
            parse_mode="MarkdownV2",
            reply_markup=reply_markup
        )

        del order_mode[user_id]

    # ===== SAVOL ADMIN GA BORADI =====
    elif user_id in contact_mode:
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"📩 Mijoz savoli:\n\n{text}\n\n👤 User: {user.first_name} | ID: {user_id}"
        )

        msg = (
            "✅ *Xabaringiz adminga yuborildi\\!* 📨\n"
            "━━━━━━━━━━━━━━\n"
            "🕒 Admin tez orada javob beradi\\.\n\n"
            "🙂 Menyudan davom eting 👇"
        )
        await update.message.reply_text(
            msg,
            parse_mode="MarkdownV2",
            reply_markup=reply_markup
        )

        del contact_mode[user_id]

    else:
        await update.message.reply_text(
            "🙂 Iltimos, pastdagi *menyu tugmalari* orqali tanlang 👇",
            reply_markup=reply_markup,
            parse_mode="MarkdownV2"
        )


if TOKEN == "PASTE_TOKEN_HERE" or not TOKEN.strip():
    raise RuntimeError("TOKEN ni qo'ymagansan. TOKEN = \"...\" ichiga BotFather tokenni joyla.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, message_handler))
app.run_polling()
