
from DBReader import ReadDB, get_url, get_rairty
bot = telebot.TeleBot(config.TOKEN)
from weapons import GetKeyboarsForPistols, GetWeapType, GetKeyboardFowWeapon, GUN_TYPES


# from weapons import weapons
def main():

    bot = telebot.TeleBot(config.TOKEN)




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
            bot.send_message(message.chat.id, 'выбери категорию оружия'.format(message.from_user, bot.get_me()), reply_markup=GetWeapType())

        if message.text in GUN_TYPES:
            print(message.text)
            bot.send_message(message.chat.id, 'выбери оружие'.format(message.from_user, bot.get_me()), reply_markup=GetKeyboardFowWeapon(message.text))


        #ЭТА ХУЕТА ТРЕБУЕТ ФИКСА!!!!!!!!!!!!!!. ВЫВОДИТ МУЗЫКУ ПО НАЧАЛУ. ОСНОВНАЯ ЛОГИКА РАБОТАЕТ
        if message.text != '':
            aks = ReadDB(message.text)
            links = get_url(message.text)
            for items in aks:
                bot.send_message(message.chat.id, f'{items.format(message.from_user, bot.get_me())}' +  '\n' + f'{get_url(items).format(message.from_user, bot.get_me())}' + '\n' + get_rairty(items).format(message.from_user, bot.get_me()))









    bot.polling(none_stop=True)
#
if __name__ == '__main__':
    main()
