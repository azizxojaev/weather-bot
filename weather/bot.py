import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import *
from buttons import *


logging.basicConfig(level=logging.INFO)

BOT_TOKEN = '5689047693:AAEY4yEZocaDOlzoXicCtCko_F2PD3mc8cs'

bot = Bot(token=BOT_TOKEN, parse_mode='Markdown')
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    btn = await start_btn()
    await message.answer('Вот список того, что я умею:', reply_markup=btn)

channel = None

@dp.message_handler()
async def messages(message: types.Message):
    global channel
    text = message.text
    if text == '🌞 Погода сейчас':
        btn = await weather_now()
        await message.answer_photo(types.InputFile('black.jpg'), reply_markup=btn)
    elif text == '🌅 На завтра':
        btn = await weather_tomorrow()
        await message.answer_photo(types.InputFile('black.jpg'), reply_markup=btn)
    elif text == '🔮 На 5 дней':
        btn = await weather_tomorrow()
        await message.answer_photo(types.InputFile('black.jpg'), reply_markup=btn)
    elif text == '🔮 На 10 дней':
        btn = await weather_tomorrow()
        await message.answer_photo(types.InputFile('black.jpg'), reply_markup=btn)
    elif text == '🔔 Уведомления':
        btn = await notifications()
        await message.answer('Выберите тип отправляемых уведомлений:', reply_markup=btn)
    elif text == '⚙️ Настройки':
        btn = await settings_btn()
        await message.answer('Настройки', reply_markup=btn)
    elif text == '↩️ Назад':
        btn = await start_btn()
        await message.answer('Вот список того, что я умею:', reply_markup=btn)
    elif text == '🌎 Изменить город':
        btn = await location_btn()
        await message.answer('Напишите название населенного пункта или отправь свою геолокацию, чтобы я показал тебе погоду:', reply_markup=btn)
    elif text == '📏 Единицы измерения':
        btn = await izmereniye()
        await message.answer('Единицы измерения', reply_markup=btn)
    elif text == '👥 Добавить бота в канал/группу':
        btn = await add_btn()
        await message.answer('Выберите действие:', reply_markup=btn)
    elif text == '👥 Добавить бота в группу':
        channel = 'group'
        btn = await text_btn()
        await message.answer_video(types.InputFile('groups.mp4'), caption='Посмотрите видео о том, как добавлять бота в группы', reply_markup=btn)
    elif text == '📢 Добавить бота в канал':
        channel = 'channel'
        btn = await text_btn()
        await message.answer_video(types.InputFile('channels.mp4'), caption='Посмотрите видео о том, как добавлять бота в каналы', reply_markup=btn)

@dp.callback_query_handler(text_contains='more')
async def more(call: types.CallbackQuery):
    btn = await weather_back_now()
    await call.message.edit_reply_markup(btn)
@dp.callback_query_handler(text_contains='back')
async def more_back(call: types.CallbackQuery):
    btn = await weather_now()
    await call.message.edit_reply_markup(btn)

name = None

@dp.callback_query_handler(text_contains='notifications:')
async def more_back(call: types.CallbackQuery):
    global name
    choice = call.data.split(':')[1]
    if choice == '1':
        name = 'Прогноз на сегодня'
        btn = await notifications_choice()
        await call.message.edit_text('Выберите время отправки уведомлений "_Прогноз на сегодня_"', reply_markup=btn)
    elif choice == '2':
        name = 'Прогноз на завтра'
        btn = await notifications_choice()
        await call.message.edit_text('Выберите время отправки уведомлений "_Прогноз на завтра_"', reply_markup=btn)
    elif choice == '3':
        name = 'На 5 дней'
        btn = await notifications_choice()
        await call.message.edit_text('Выберите время отправки уведомлений "_На 5 дней_"', reply_markup=btn)
    elif choice == '4':
        name = 'На 10 дней'
        btn = await notifications_choice()
        await call.message.edit_text('Выберите время отправки уведомлений "_На 10 дней_"', reply_markup=btn)
    elif choice == 'menu':
        btn = await notifications()
        await call.message.edit_text('Выберите тип отправляемых уведомлений:', reply_markup=btn)
    elif choice == 'everyday':
        btn = await notifications_time()
        await call.message.edit_text('Я буду присылать тебе актуальную погоду каждый день в выбранное время', reply_markup=btn)
    elif choice == 'week':
        btn = await notifications_week()
        await call.message.edit_text(f'Выберите время отправки уведомлений "_{name}_"', reply_markup=btn)
    elif choice == 'week2':
        btn = await notifications_choice()
        await call.message.edit_reply_markup(btn)
@dp.callback_query_handler(text_contains='notifications2:')
async def more_back(call: types.CallbackQuery):
    choice = call.data.split(':')[1]
    if choice == 'menu2':
        btn = await notifications_choice()
        await call.message.edit_text(f'Выберите время отправки уведомлений "{name}"', reply_markup=btn)

@dp.callback_query_handler(text_contains='textv')
async def more_back(call: types.CallbackQuery):
    if channel == 'group':
        await call.message.answer('*Что бы добавить бота в группу, выполните следующие действия:*\n1. Зайдите в группу, где вы являетесь администратором (вы должны быть *не анонимным* администратором)\n2. Нажмите на заголовок группы\n3. Убедитесь, что группа публичная, бот не работает в закрытых группах\n4. Нажмите на "Добавить участника"\n5. Введите "Погода" в строке поиска\n6. Нажмите на имя, появившегося в списке, бота\n7. Бот добавлен, теперь вы можете настроить уведомления\n8. Выйдите из группы и зайдите в личный диалог с ботом\n9. Нажмите на кнопку "👥 Настройки групп и каналов"\n10. Нажмите на название вашей группы\n11. Нажмите на кнопку "🔔 Уведомления"\n12. Введите название населённого пункта, для которого необходимо предоставлять погоду в группе\n13. Выберите ваш город из списка найденных городов\n14. Нажмите на кнопку "🔔 Уведомления"\n15. Выберите тип отравляемых уведомлений, например "Прогноз на сегодня"\n16. Выберите частоту отправки уведомлений, например "Ежедневно"\n17. Выберите час, а после минуты\n18. Готово! Теперь бот будет отправлять уведомление в вашу группу в указанное время!')
    elif channel == 'channel':
        await call.message.answer('*Что бы добавить бота в канал, выполните следующие действия:*\n1. Зайдите в канал, где вы являетесь администратором (вы должны быть *не анонимным* администратором)\n2. Нажмите на заголовок канала\n3. Убедитесь, что канал публичный, бот не работает в закрытых каналах\n4. Нажмите на "Администраторы"\n5. Нажмите "Добавить администратора"\n6. Нажмите на значок поиска в правом верхнем углу экрана\n7. Введите "Погода" в строке поиска\n8. Нажмите на имя, появившегося в списке, бота\n9. Нажмите на галочку в правом верхнем углу\n10. Для активации бота, необходимо что бы в канале появилась одна новая запись\n11. Добавьте любую запись в канал\n12. Бот добавлен и активирован, теперь вы можете настроить уведомления\n13. Выйдите из канала и зайдите в личный диалог с ботом\n14. Нажмите на кнопку "👥 Настройки групп и каналов"\n15. Нажмите на название вашего канала\n16. Нажмите на кнопку "🔔 Уведомления"\n17. Введите название населённого пункта, для которого необходимо предоставлять погоду в канале\n18. Выберите ваш город из списка найденных городов\n19. Нажмите на кнопку "🔔 Уведомления"\n20. Выберите тип отравляемых уведомлений, например "Прогноз на сегодня"\n21. Выберите частоту отправки уведомлений, например "Ежедневно"\n22. Выберите час, а после минуты\n23. Готово! Теперь бот будет отправлять уведомление в ваш канал в указанное время!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)