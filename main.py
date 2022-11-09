import telebot
from dbholder import config
from telebot import types
from DBReader import ReadDB, get_url
bot = telebot.TeleBot(config.TOKEN)
from weapons import PISTOLS, GetKeyboarsForPistols


# from weapons import weapons
def main():

    bot = telebot.TeleBot(config.TOKEN)

    #
    #
    #
    @bot.message_handler(content_types=['text'], commands=['start'])
    def Msg(message):
        bot.send_message(message.chat.id, f'Привет! Я - бот, дающий тебе возможность купить скины\nпо выгодной цене'.format(message.from_user, bot.get_me()))
        inl = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton('CSGO')
        inl.add(item)
        bot.send_message(message.chat.id, 'выбери доступную мне игру'.format(message.from_user, bot.get_me()), reply_markup=inl)
    # #
    # #
    # #
    @bot.message_handler(content_types=['text'])
    def GetTheGun(message):
        if message.text == 'CSGO':
            bot.send_message(message.chat.id, 'выбери категорию оружия'.format(message.from_user, bot.get_me()), reply_markup=GetKeyboarsForPistols(PISTOLS))

    #
    #
    #
    # @bot.message_handler(content_types=['text'])
    # def GetSkins(message):
        if message.text == 'USP-S':
            bot.send_message(message.chat.id, 'хуй'.format(message.from_user, bot.get_me()))
            aks = ReadDB('USP-S')
            links = get_url('USP-S')
            for items in aks:
                bot.send_message(message.chat.id, f'{items.format(message.from_user, bot.get_me())}' +  '\n' + f'{get_url(items).format(message.from_user, bot.get_me())}')
        # if message.text == 'SSG':
        #     aks = ReadDB('SSG')
        #     links = get_url('SSG')
        #     print(aks)
        #     print(get_url('SSG'))
            # inls = types.InlineKeyboardMarkup(row_width=1)
        # guns = ReadDB()
        # for items in guns:
        #     bot.send_message(message.chat.id, f'{items.format(message.from_user, bot.get_me())}' +  '\n' + f'{get_url(items).format(message.from_user, bot.get_me())}')
        #         # bot.send_message(message.chat.id, get_url(items).format(message.from_user, bot.get_me()))

                    # time.sleep(2)
            #     inls.add()
            #
            # bot.send_message(message.chat.id, 'y', reply_markup=inls)



    # def MarkUps(message):
    #     weapons = types.InlineKeyboardMarkup(row_width=1)
    #     weapons.add(types.InlineKeyboardButton('AK-47', callback_data='ok'))
#         weapons.add(types.InlineKeyboardButton('AWP', callback_data='ok'))
#         weapons.add(types.InlineKeyboardButton('KNIFE', callback_data='ok'))
#         weapons.add(types.InlineKeyboardButton('M4A1', callback_data='ok'))
#         weapons.add(types.InlineKeyboardButton('M4A1-S', callback_data='ok'))
#         weapons.add(types.InlineKeyboardButton('USP', callback_data='ok'))
#         weapons.add(types.InlineKeyboardButton('DESERT EAGLE', callback_data='ok'))
#         weapons.add(types.InlineKeyboardButton('GLOCK-17', callback_data='ok'))
#         weapons.add(types.InlineKeyboardButton('P250', callback_data='ok'))
#         weapons.add(types.InlineKeyboardButton('P2000', callback_data='ok'))
#         weapons.add(types.InlineKeyboardButton('DUAL-BERRETTES', callback_data='ok'))
#         # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выбери оружие", reply_markup=weapons)
#         return weapons
#
#     @bot.callback_query_handler(func=lambda call:True)
#     def call_back_first_msg(calla):
#         bot.send_message(message.chat.id, 'Выберите тип оружия', reply_markup=MarkUps(message=message))
#
#
#
    bot.polling(none_stop=True)
#
if __name__ == '__main__':
    main()

# def mainMarkup(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1 = types.KeyboardButton('Assault Rifles')
#     item2 = types.KeyboardButton('Sniper Rifles')
#     item3 = types.KeyboardButton('Knives')
#     item4 = types.KeyboardButton('Gloves')
#     item5 = types.KeyboardButton('Pistols')
#     item6 = types.KeyboardButton('SMGs')
#     item7 = types.KeyboardButton('Shotguns')
#     item8 = types.KeyboardButton('Machine guns')
#     item9 = types.KeyboardButton('Keys - in Future')
#     item10 = types.KeyboardButton('Other - in Future')
#     markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, )
#     return markup
#
#
# def mainMenu(message):
#     markup = mainMarkup(message)
#     bot.send_message(message.chat.id, 'Выберите тип оружия', reply_markup=markup)
#
#
# def assualt_rifles(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1 = types.KeyboardButton('AK')
#     item2 = types.KeyboardButton('AUG')
#     item3 = types.KeyboardButton('FAMAS')
#     item4 = types.KeyboardButton('Galil AR')
#     item5 = types.KeyboardButton('M4A4')
#     item6 = types.KeyboardButton('M4A1-S')
#     item7 = types.KeyboardButton('SG553')
#     item8 = types.KeyboardButton('Back to menu')
#     markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
#     bot.send_message(message.chat.id, 'Выберите винтовку'.format(message.from_user), reply_markup=markup)
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = mainMarkup(message)
#     bot.send_message(message.chat.id, 'Привет, {0.first_name}! Этот бот создан для подбора скинов на сайте market.csgo.com'.format(message.from_user), reply_markup=markup)
#
#
#
# @bot.message_handler(content_types=['text'])
# def getWeapon(message):
#     time.sleep(2)
#     if message.text == 'AK':
#         bot.send_message(message.chat.id, ReadDB('AK'), reply_markup=None )
#
#
#
# bot.polling(none_stop=True)