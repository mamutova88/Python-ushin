from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards import reg_menu,admin_mrnu
from data import add_user,show_user

class RegistrationState(StatesGroup):
    name = State()
    phone_num = State()


api = '7340838678:AAHWxhtcRv46DfyUdO0ByTvvBgqzuUnpO9Y'
bot = Bot(api)
storage = MemoryStorage()
dp = Dispatcher(bot,storage=storage)

admin_id=1318330948

@dp.message_handler(commands=['start'])
async def send_hi(message:types.Message):
    
    if message.from_user.id==admin_id:
        await message.answer(text='salem admin',reply=admin_mrnu)
    else:
        await message.answer(text='Здравствуйте',reply_markup=reg_menu)

@dp.callback_query_handler()
async def send_reg(call:types.CallbackQuery):
    data = call.data
    if data=='reg':
        await bot.send_message(
            chat_id=call.from_user.id,
            text='Напишите свое имя !'
        )
        await RegistrationState.name.set()


@dp.message_handler(state=RegistrationState.name)
async def send_name(message:types.Message,state:FSMContext):
    async with state.proxy() as daniy:
        daniy['имя']=message.text
    await message.answer('Введите свои номер')
    await RegistrationState.phone_num.set()
@dp.message_handler(state=RegistrationState.phone_num)
async def send_num(message:types.Message,state:FSMContext):
    async with state.proxy() as daniy:
        daniy['номер']=message.text
    await message.answer(f'''Регистрация успешно завершено!
Имя:{daniy['имя']},
Номер:{daniy['номер']},''')
    await add_user(id=message.from_user.id,name=daniy['имя'],phone_num=daniy['номер'])
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)