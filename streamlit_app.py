import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove, BotCommand
from aiogram.utils.markdown import bold, italic, text

bot = Bot(token="TOKEN")
dp = Dispatcher()

MAIN_MESSAGE = text(
    bold("🍑Добро пожаловать в Хентайный Уголок/!🍑\n\n"),
    italic("Твое личное убежище для самых сладких фантазий\n\n"),
    "Здесь нет стеснения — только искусство желания\n",
    "во всей его пиксельной и чувственной красе.\n\n",
    "🔞 В нашем уголке ты найдешь:\n",
    "• Категории на любой извращённый вкус\n",
    "• Поиск по тегам и фетишам\n",
    "• Уютную сохранёнку, чтобы не потеряться в удовольствии\n",
    "• Горячие обновления — всегда есть что открыть\n\n",
    "🖤 Без цензуры. Без границ. Только ты и твои желания.\n\n",
    italic("Нажми кнопку ниже и окунись в атмосферу наслаждения"),
    "\n\nP.S. Поделись с теми, кто понимает — удовольствие любит компанию."
)

WELCOME_MESSAGE = text(
    bold("🌸 Приветствую тебя в Хентайном Уголке/! 🌸\n\n"),
    " Это место, где ты можешь снять все ограничения и отдаться сладкому наслаждению.\n\n",
    bold("Доступные команды:\n"),
    "/start - Главное меню\n",
    "/help - Помощь и информация\n",
    "/rules - Правила сообщества\n",
    "/invite - Пригласить друзей\n",
    "/chat - Инфо о чате обсуждений сообщества\n\n",
    italic("Выбери действие из меню или воспользуйся командой:")
)

DISCUSSION_CHAT_INFO = text(
    bold("💬 Сладкие Обсуждения 👉👌🏻 💬\n\n"),
    "Наш уютный чат для истинных ценителей:\n",
    "• Обсуждаем самые сочные моменты\n",
    "• Делимся находками и рекомендациями\n",
    "• Находим единомышленников по вкусам\n",
    "• Общаемся без стеснения и ограничений\n\n",
    italic("⚠️ После нажатия кнопки ты попадешь туда, где прячется всё самое 'сладкое' 🍓\n"),
    "Заходи и ощути атмосферу без стеснений и ограничений\n\n",
    bold("Ждем тебя за виртуальным столиком")
)


def get_inline_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🌴 Войти в Уголок Наслаждения 🌴", 
                    url="https://t.me/+M4j5yWy5RDc5YWEy"
                )
            ],
            [
                InlineKeyboardButton(
                    text="💬 Сладкие Обсуждения (18+)", 
                    url="https://t.me/+DgNOkpMyjolhZjIy"
                )
            ],
            [
                InlineKeyboardButton(
                    text="💌 Пригласить друзей 💌",
                    callback_data="invite_friends"
                ),
                InlineKeyboardButton(
                    text="📜 Правила",
                    callback_data="show_rules"
                )
            ]
        ]
    )

def get_invite_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📋 Копировать ссылку", 
                    callback_data="copy_link"
                ),
                InlineKeyboardButton(
                    text="↗️ Переслать приглашение", 
                    callback_data="forward_invite"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔙 Назад", 
                    callback_data="back_to_main"
                )
            ]
        ]
    )

INVITE_TEXT = text(
    bold("🌸 Дорогой друг 🌸\n\n"),
    "Ты приглашён в особенное место —",
    bold("🍑Хентайный Уголок🍑\n\n"),
    "Там, где желания не осуждают, а фантазии становятся реальностью.\n\n",
    "В нашем Уголке тебя ждёт:\n",
    "• Глубокое погружение в мир наслаждения\n",
    "• Честные и откровенные разговоры\n",
    "•  Контент, который пробуждает самые глубокие желания\n",
    "• Атмосфера, где нет места стеснению и ограничениями\n\n",
    italic("Нажми кнопку ниже и позволь себе больше, чем обычно~\n"),
    "Мы уже там. Осталось только тебе заглянуть… 🔥"
)





RULES_TEXT = text(
    bold("📜 Правила Хентайного Уголка:\n\n"),
    "1. Уважай других участников\n",
    "2. Запрещен спам и флуд\n",
    "3. Контент 18+ только в соответствующем канале\n",
    "4. Для доступа в чат обсуждений нужно подать заявку\n",
    "5. Не нарушайте законы вашей страны\n",
    "6. Администрация вправе banить без объяснения причин\n\n",
    ("Соблюдение правил делает наше сообщество лучше для всех!")
)

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(WELCOME_MESSAGE, parse_mode="Markdown")
    await message.answer(MAIN_MESSAGE, reply_markup=get_inline_keyboard(), parse_mode="Markdown")

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        text("ℹ️ Помощь по боту:\n\n"
             "Этот бот создан для удобного доступа к Хентайному Уголку.\n"
             "Используй кнопки меню для навигации или команды:\n\n"
             "/start - Главное меню\n"
             "/rules - Правила сообщества\n"
             "/invite - Пригласить друзей\n"
             "/chat - Информация о чате обсуждений"),
        parse_mode="Markdown"
    )

@dp.message(Command("rules"))
async def cmd_rules(message: types.Message):
    await message.answer(RULES_TEXT, parse_mode="Markdown")

@dp.message(Command("invite"))
async def cmd_invite(message: types.Message):
    await message.answer("🎪 Выбери способ приглашения друзей:", reply_markup=get_invite_keyboard())

@dp.message(Command("chat"))
async def cmd_chat_info(message: types.Message):
    await message.answer(
        DISCUSSION_CHAT_INFO,
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[[
                InlineKeyboardButton(
                    text="💬 Войти в чат обсуждений",
                    url="https://t.me/+DgNOkpMyjolhZjIy"
                )
            ]]
        ),
        parse_mode="Markdown"
    )

@dp.callback_query(lambda c: c.data == 'invite_friends')
async def invite_friends(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text("🎪 Выбери способ приглашения друзей:", reply_markup=get_invite_keyboard())
    await callback_query.answer()

@dp.callback_query(lambda c: c.data == 'show_rules')
async def show_rules(callback_query: types.CallbackQuery):
    await callback_query.message.answer(RULES_TEXT, parse_mode="Markdown")
    await callback_query.answer()

@dp.callback_query(lambda c: c.data == 'copy_link')
async def copy_link(callback_query: types.CallbackQuery):
    copy_text = (
        "🔗 Вот ссылка для приглашения - выдели и скопируй её:\n"
        "https://t.me/+M4j5yWy5RDc5YWEy\n\n"
        "А это ссылка на чат обсуждений:\n"
        "https://t.me/+DgNOkpMyjolhZjIy\n\n"
        "Просто выдели нужную ссылку и нажми 'Копировать'"  
    )
    
    await callback_query.message.answer(
        text=copy_text,
        reply_markup=ReplyKeyboardRemove()
    )
    await callback_query.answer("Ссылки готовы для копирования")

@dp.callback_query(lambda c: c.data == 'forward_invite')
async def forward_invite(callback_query: types.CallbackQuery):
    await callback_query.message.answer(
        text=INVITE_TEXT,
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[[
                InlineKeyboardButton(text="🌴 Присоединиться", url="https://t.me/+M4j5yWy5RDc5YWEy"),
                InlineKeyboardButton(text="💬 Чат обсуждений", url="https://t.me/+DgNOkpMyjolhZjIy")
            ]]
        )
    )
    await callback_query.answer("Приглашение готово к пересылке!")

@dp.callback_query(lambda c: c.data == 'back_to_main')
async def back_to_main(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(
        text=MAIN_MESSAGE,
        reply_markup=get_inline_keyboard(),
        parse_mode="Markdown"
    )
    await callback_query.answer()

async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Главное меню"),
        BotCommand(command="help", description="Помощь и информация"),
        BotCommand(command="rules", description="Правила сообщества"),
        BotCommand(command="invite", description="Пригласить друзей"),
        BotCommand(command="chat", description="Инфо о чате обсуждений"),
    ]
    await bot.set_my_commands(commands)

async def main():
    await set_bot_commands(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
