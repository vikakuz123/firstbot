from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

TOKEN_API='7162242931:AAEZk_c_RcE3ppOTgHUgQP8xJd57u1Qmhps'
bot = Bot(token= TOKEN_API)
dp = Dispatcher(bot)


keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton('сайты')
button1 = KeyboardButton('комиксы')
keyboard.add(button,button1)



async def set_commands(bot: Bot):
    commands =[
        types.BotCommand(command="/start", description='Привет, я mimi.\nЯ создаю комфорт и уют!'),
        types.BotCommand(command="/help", description='Возникли вопросы? \nя всегда рад тебе помочь!'),
        types.BotCommand(command="/about",description='Я помогаю с подбором удобной платформы для просмотра дорам и чтения комиксов!'),
        types.BotCommand(command="/revievs", description='Если вам удобен бот и все нравится можете оставить отзыв')
    ]
    await bot.set_my_commands(commands)

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('Привет, я mimi.\nЯ создаю комфорт и уют!', reply_markup=keyboard)

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.answer('Возникли вопросы? \nя всегда рад тебе помочь!')

@dp.message_handler(commands='about')
async def about(message: types.Message):
   await message.answer('Я помогаю с подбором удобной платформы для просмотра дорам и чтения комиксов!')

@dp.message_handler(commands= 'revievs')
async def revievs(message: types.Message):
    await message.answer('Если вам удобен бот и все нравится можете оставить отзыв!')



keyboard_inline = InlineKeyboardMarkup(row_width= 1)
button_inline = InlineKeyboardButton('softbox',url='https://ru.softboxtv.tv/')
button1_inline = InlineKeyboardButton('doramafox',url='https://doramafox.club/')
button2_inline = InlineKeyboardButton('doramaland',url='https://rus.doramaland.cc/')
keyboard_inline.add(button_inline, button1_inline, button2_inline)


keyboard_inline2 = InlineKeyboardMarkup(row_width= 1)
button3_inline = InlineKeyboardButton('mangalib',url='https://mangalib.me/?section=home-updates-3308155')
button4_inline = InlineKeyboardButton('mangabuff',url='https://mangabuff.ru/')
button5_inline = InlineKeyboardButton('readmanga',url='https://readmanga.live/')
keyboard_inline2.add(button3_inline, button4_inline, button5_inline)


@dp.message_handler(lambda message: message.text == 'сайты')
async def button_sites(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://sun9-38.userapi.com/impg/SwK58_P2CxnmbWhPsHnYNEZeF0IncAfppJ_TIA/YAF-vRCMMFA.jpg?size=1080x1080&quality=95&sign=58886081b987992994004819ab4e7050&c_uniq_tag=vkuTHJhn9tAbFJgKtiJHEmaVY4xtMj-I3DFL0PDBbC4&type=album', reply_markup= keyboard_inline)


@dp.message_handler(lambda message: message.text == 'комиксы')
async def button1_click(message: types.Message):
        await bot.send_photo(message.chat.id, photo='https://i0.wp.com/www.comicsbeat.com/wp-content/uploads/2020/01/Sweet-Home.png',reply_markup= keyboard_inline2)


async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)


if __name__ == 'main':
    executor.start_polling(dp, skip_updates= True, on_startup=on_startup)