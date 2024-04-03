from aiogram import Bot, Dispatcher, types
from asyncio import run
import funcs
dp = Dispatcher()
from aiogram.filters import Command
import states




async def start():

    # dp.message.register(funcs.startup_answer)
    # dp.message.register(echo)
    dp.message.register(funcs.start_answer, Command("start"))
    dp.message.register(funcs.help_answer, Command("help"))
    dp.message.register(funcs.application, Command("application", prefix="/!"))
    # dp.message.register

    # dp.message.register(funcs.sign_up_name, states.sign_up.name)
    # dp.message.register(funcs.sign_up_age, states.sign_up.age)

    dp.message.register(funcs.get_info)
    # dp.message.register(funcs.shutdown_answer)
    bot = Bot("7092332737:AAGexe6193cIvZ-YVKLZIHyxbliL2tTDwsM")
    await bot.set_my_commands([
        types.BotCommand(command="/start", description="Botni ishga tushirish"),
        types.BotCommand(command="/help", description="Foydalanish yo'riqnomasi"),
        types.BotCommand(command="/application", description="Ariza yo'llash"),
        types.BotCommand(command="/cancel", description="Arizani bekor qilish"),
    ])
    await dp.start_polling(bot)


run(start())

# message_id=273 date=datetime.datetime(2024, 3, 26, 0, 49, 43, tzinfo=TzInfo(UTC)) 
# chat=Chat(id=6401654016, type='private', title=None, username='ZoirbekTukhtasinov', first_name='Zoirbek', last_name="To'xtasinov", 
#         is_forum=None, photo=None, active_usernames=None, available_reactions=None, accent_color_id=None, background_custom_emoji_id=None, 
#         profile_accent_color_id=None, profile_background_custom_emoji_id=None,
#         emoji_status_custom_emoji_id=None, emoji_status_expiration_date=None, bio=None, has_private_forwards=None, 
#         has_restricted_voice_and_video_messages=None, join_to_send_messages=None, join_by_request=None, description=None, 
#         invite_link=None, pinned_message=None, permissions=None, slow_mode_delay=None, unrestrict_boost_count=None,
#         message_auto_delete_time=None, has_aggressive_anti_spam_enabled=None, has_hidden_members=None, has_protected_content=None, 
#         has_visible_history=None, sticker_set_name=None, can_set_sticker_set=None, custom_emoji_sticker_set_name=None,
#         linked_chat_id=None, location=None) 
# message_thread_id=None 
# from_user=User(id=6401654016, is_bot=False, first_name='Zoirbek', last_name="To'xtasinov", 
#                    username='ZoirbekTukhtasinov', language_code='uz', is_premium=None, added_to_attachment_menu=None,
#                 can_join_groups=None, can_read_all_group_messages=None, supports_inline_queries=None)

