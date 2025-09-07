from aiogram import types
from reminders import remind_client
import asyncio

clients = []
client_id = 0

# /start komandasi uchun
async def start_handler(message: types.Message):
    text = (
        "👋 Assalomu alaykum!\n\n"
        "📌 Klient ma’lumotlarini quyidagi tartibda yuboring:\n\n"
        "1️⃣ Ism Familiya\n"
        "2️⃣ Telefon raqami (+99890xxxxxxx)\n"
        "3️⃣ Xizmat turi (Soch / Soqol)\n"
        "4️⃣ Sana (YYYY-MM-DD)\n"
        "5️⃣ Necha soniyadan keyin eslatma yuborilsin\n\n"
        "✍️ Namuna:\n"
        "`Ali Valiyev, +998901234567, Soch, 2025-09-07, 30`\n\n"
        "✅ Shu formatda yozsangiz, ma’lumotlar saqlanadi!"
    )
    await message.answer(text, parse_mode="Markdown")

# Klient ma’lumotlarini qabul qilish
async def client_handler(message: types.Message, bot, admin_id: int):
    global client_id
    try:
        data = message.text.split(",")
        name = data[0].strip()
        phone = data[1].strip()
        service = data[2].strip()
        date = data[3].strip()
        remind_after = int(data[4].strip())  # foydalanuvchi yozgan soniya

        client_id += 1

        client_info = {
            "id": client_id,
            "name": name,
            "phone": phone,
            "service": service,
            "date": date,
            "remind_after": remind_after
        }
        clients.append(client_info)

        # Foydalanuvchiga javob
        await message.answer("✅ Ma’lumotlar saqlandi!")

        # Belgilangan vaqtdan keyin ADMINga eslatma
        asyncio.create_task(wait_and_remind(bot, message.chat.id, client_info, admin_id))

    except Exception:
        await message.answer(
            "⚠️ Format xato!\n\n"
            "To‘g‘ri yozing:\n"
            "`Ism Familiya, Telefon, Xizmat, Sana, Vaqt(soniya)`",
            parse_mode="Markdown"
        )

# Kutib turib, admin’ga eslatma yuborish
async def wait_and_remind(bot, chat_id, client_info, admin_id):
    await asyncio.sleep(client_info["remind_after"])
    await remind_client(bot, chat_id, client_info, admin_id)
