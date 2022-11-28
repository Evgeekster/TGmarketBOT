import telebot
import config
from telebot import types
from DBReader import ReadDB, get_url, get_rairty
bot = telebot.TeleBot(config.TOKEN)
from weapons import GetKeyboarsForPistols, GetWeapType, GetKeyboardFowWeapon, GUN_TYPES, GUNS, GetReplyMarkupForSkins
from AllSkinStuff import allskins

# from weapons import weapons
def main():

    bot = telebot.TeleBot(config.TOKEN)




    @bot.message_handler(content_types=['text'], commands=['start'])
    def Msg(message):
        bot.send_message(message.chat.id, f'Привет! Я - бот, дающий тебе возможность купить скины\nпо выгодной цене'.format(message.from_user, bot.get_me()))
        inl = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton('CSGO')
        inl.add(item)
        # inl = types.InlineKeyboardMarkup(row_width=1).add(types.InlineKeyboardButton(text='CSGO', callback_data='xxxx'))
        bot.send_message(message.chat.id, 'выбери доступную мне игру'.format(message.from_user, bot.get_me()), reply_markup=inl)
    # #
    # #
    # #

    @bot.message_handler(content_types=['text'])
    def GetTheGun(message):
        global c_g

        if message.text == 'CSGO':
            bot.send_message(message.chat.id, 'выбери категорию оружия'.format(message.from_user, bot.get_me()), reply_markup=GetWeapType())

        if message.text in GUN_TYPES:

            bot.send_message(message.chat.id, 'выбери оружие'.format(message.from_user, bot.get_me()), reply_markup=GetKeyboardFowWeapon(message.text))



        for key, value in GUNS.items():
            if message.text in value:
                c_g = message.text
                print(c_g)
                bot.send_message(message.chat.id, 'выбери скин'.format(message.from_user, bot.get_me()), reply_markup=GetReplyMarkupForSkins(message.text))

        for sett in allskins:
            for key, value in sett.items():
                if key == 'name' and message.text == value:
                    guns = ReadDB(c_g, message.text)
                    print(c_g)
                    for items in guns:
                        bot.send_message(message.chat.id,
                                         f'{items.format(message.from_user, bot.get_me())}' + '\n' + f'{get_url(items).format(message.from_user, bot.get_me())}' + '\n' + get_rairty(
                                             items).format(message.from_user, bot.get_me()))
                    c_g = ''
                    guns = []






        #     buy_inl = types.InlineKeyboardMarkup(row_width=1).add(types.InlineKeyboardButton(text='купить'))
        #     if message.text in value:
        #         aks = ReadDB(message.text)
        #         links = get_url(message.text)
        #         for items in aks:
        #             buy_inl.add(types.InlineKeyboardButton(text='Купить', callback_data='xxx'))
        #             bot.send_message(message.chat.id, f'{items.format(message.from_user, bot.get_me())}' +  '\n' + f'{get_url(items).format(message.from_user, bot.get_me())}' + '\n' + get_rairty(items).format(message.from_user, bot.get_me()))
        #







    bot.polling(none_stop=True)
#
if __name__ == '__main__':
    main()
