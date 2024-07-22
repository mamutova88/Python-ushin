from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton



reg_menu=InlineKeyboardMarkup()


reg_menu.add(InlineKeyboardButton(text='Registraciya',callback_data='reg'))
admin_mrnu = InlineKeyboardMarkup()
admin_mrnu.add(InlineKeyboardButton(text='admin',callback_data='ad'))