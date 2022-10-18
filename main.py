import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'], commands=['start'])
def Msg(message):
    bot.send_message(message.chat.id, f'Привет! Я - бот, дающий тебе возможность купить скины\nпо выгодной цене'.format(message.from_user, bot.get_me()))


    inl = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton('DOTA2', callback_data='ok')
    inl.add(item)
    bot.send_message(message.chat.id, 'выбери доступную мне игру'.format(message.from_user, bot.get_me()), reply_markup=inl)

@bot.callback_query_handler(func=lambda call:True)
def call_back(call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="No", reply_markup=None)

bot.polling(none_stop=True)