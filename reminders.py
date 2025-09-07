from aiogram import Bot
import json

async def remind_client(bot: Bot, chat_id: int, client_info: dict, admin_id: int):
    # Eslatma ADMINga boradi
    text = (
        "⏰ *Eslatma!*\n\n"
        "Bugun xizmatdan foydalangan klient ma’lumoti:\n\n"
        f"👤 Ism Familiya: *{client_info['name']}*\n"
        f"📞 Telefon: `{client_info['phone']}`\n"
        f"💈 Xizmat: {client_info['service']}\n"
        f"📅 Sana: {client_info['date']}\n"
        f"🔔 Eslatma muddati: {client_info['remind_after']} soniya\n\n"
        f"➡️ Iltimos, ushbu klient bilan bog‘laning."
    )

    await bot.send_message(admin_id, text, parse_mode="Markdown")

    # Tarixga yozib qo‘yish (database.json)
    try:
        with open("database.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []  # agar fayl bo‘lmasa yangisini yaratamiz

    data.append(client_info)

    with open("database.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
