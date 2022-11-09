from telebot import types

PISTOLS = ['GLOCK-17', 'USP-S','Dual Berettas', 'P250', 'Tec-9', 'CZ75-Auto', 'Desert Eagle', 'R8 Revolver', 'P2000', 'Five-Seven']
PPS = ['MAC-10', 'MP7', 'UMP-45', 'P90', 'PP-Bizon', 'MP9']
SHOTGUNS = []
HEAVY = []
ARS = []
def GetKeyboarsForPistols(PISTOLS):
    inl = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for weapon in PISTOLS:
        inl.add(types.KeyboardButton(text=weapon))
    return inl
# MAC-10 = give weapon_mac10
# MP7 = give weapon_mp7
# UMP-45 = give weapon_ump45
# P90 = give weapon_p90
# PP-Bizon = give weapon_bizon
# Контр-террористы
#
# MP9 = give weapon_mp9
# MP7 = give weapon_mp7
# UMP-45 = give weapon_ump45
# P90 = give weapon_p90
# PP-Bizon = give weapon_bizon