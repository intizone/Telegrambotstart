from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import states


# async def startup_answer(bot: Bot):
#     await bot.send_message(chat_id=638615136, text="Bot ishlamoqda ✔️")

# async def shutdown_answer(bot: Bot):
#     await bot.send_message(chat_id=638615136, text="Bot to'xtadi ❌")


async def get_info(message: Message, bot: Bot):
    user = await bot.get_chat(message.from_user.id)
    user_photos = await message.from_user.get_profile_photos()

    matn = (f"{message.from_user.mention_html('USER')} info:\n\n"
            f"full name: {message.from_user.full_name}\n"
            f"user's ID: <code>{message.from_user.id}</code>\n")
    if user.bio:
        matn += f"Bio: {user.bio}\n"
    if user.username:
        matn += f"Username: @{user.username}\n"
    if user_photos.photos:
        photo_file_id = user_photos.photos[0][-1].file_id
        await message.answer_photo(photo_file_id, caption=matn, parse_mode='HTML')
    else:
        await message.answer(matn, parse_mode='HTML')

async def echo(message: Message, bot: Bot):
    # print(type(message))
    # print(message)
    # print(message.chat.first_name)
    print(message.from_user)
    a = message.chat
    for i in range(10):
        await message.copy_to(chat_id=message.chat.id)
    await bot.send_message(chat_id=message.chat.id, text=f"Bot ishlamoqda {a.first_name},\nsizning ma'lumotlaringiz:\nid:{a.id},\nusername:{a.username},\nname = {a.first_name} {a.last_name}\nbio:{a.bio}")
    # await message.copy_to(chat_id=6401654016)

async def start_answer(message: Message, bot: Bot, state: FSMContext):
    # await bot.send_message(message.from_user.id, text=f"Salom, {message.from_user.mention_html(message.from_user.first_name)}", parse_mode="HTML")
    # await message.answer("Salom, ismingizni kiriting:")
    # await state.set_state(states.sign_up.name)
    await bot.send_message(message.from_user.id, text=f"Salom, {message.from_user.mention_html(message.from_user.first_name)}! \nBotdan foydalanish haqida /help buyrug'i orqali qisqacha bilib olishingiz mumkin.", parse_mode="HTML")

async def help_answer(message: Message, bot: Bot):
    matn = f"""
    <b>Bot buyruqlari:</b>

    /application - <i>Arizani yo'llash</i>
    /cancel - <i>Joriy arizani bekor qilish</i>
    /start - <i>Botni ishga tushirish</i>
    /help - <i>Yordam!</i>
    """
    await bot.send_message(message.from_user.id, text=matn, parse_mode='HTML')


# async def sign_up_name(message: Message, bot: Bot, state: FSMContext):
#     await state.update_data(name=message.text)
#     await message.answer(f"Ismingiz qabul qilindi: {message.text}")
#     await message.answer("Yoshingizni kiriting:")
#     await state.set_state(states.sign_up.age)

# async def sign_up_age(message: Message, bot: Bot, state: FSMContext):
#     await state.update_data(age=message.text)
#     data = await state.get_data()
#     await message.answer(f"yoshingiz qabul qilindi {data.get('name')} - {message.text} yosh")
#     await state.clear()


async def application(message: Message, bot: Bot):
    await message.answer("Assalomu aleykum, botdan foydalanish haqida /help buyrug'i orqali bilib olishingiz mumkin")

async def application_name(message: Message, bot:Bot, state:FSMContext):
    await message.answer("Ism-sharfingizni kiriting:")
    await state.set_state(states.Application.name)

# async def application_name(message: Message, bot:Bot, state:FSMContext):