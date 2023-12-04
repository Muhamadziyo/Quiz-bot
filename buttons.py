from telebot.types import KeyboardButton,ReplyKeyboardMarkup


def start_game():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    
    button = KeyboardButton('Share contact',request_contact=True)
    
    kb.add(button)
    return kb
    
def contact():
    kr = ReplyKeyboardMarkup(resize_keyboard=True)
    
    button = KeyboardButton('Play game🎰')
    
    kr.add(button)
    return kr




 
