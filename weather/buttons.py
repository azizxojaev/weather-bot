from aiogram import types


async def start_btn():
    btn = types.ReplyKeyboardRemove()
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row('🌞 Погода сейчас', '🌅 На завтра')
    btn.row('🔮 На 5 дней', '🔮 На 10 дней')
    btn.row('🔔 Уведомления')
    btn.row('⚙️ Настройки')
    return btn
async def settings_btn():
    btn = types.ReplyKeyboardRemove()
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row('🌎 Изменить город')
    btn.row('📏 Единицы измерения', '🇷🇺/🇬🇧 Язык')
    btn.row('👥 Добавить бота в канал/группу')
    btn.row('↩️ Назад')
    return btn
async def location_btn():
    btn = types.ReplyKeyboardRemove()
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row('📍 Отправить геолокацию')
    btn.row('📝 Выбрать из 5-ти последних')
    btn.row('↩️ Назад')
    return btn
async def add_btn():
    btn = types.ReplyKeyboardRemove()
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row('👥 Добавить бота в группу')
    btn.row('📢 Добавить бота в канал')
    btn.row('↩️ Назад')
    return btn


async def weather_now():
    btn = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.add(
        types.InlineKeyboardButton('Подробный прогноз', callback_data='more'),
        types.InlineKeyboardButton('Пожертвование боту', callback_data='0')
    )
    return btn
async def weather_back_now():
    btn = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.add(
        types.InlineKeyboardButton('Вернуться к сводке', callback_data='back'),
        types.InlineKeyboardButton('Пожертвование боту', callback_data='00')
    )
    return btn
async def weather_tomorrow():
    btn = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.add(
        types.InlineKeyboardButton('Пожертвование боту', callback_data='00')
    )
    return btn

async def notifications():
    btn = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.add(
        types.InlineKeyboardButton('🌞 Прогноз на сегодня', callback_data='notifications:1'),
        types.InlineKeyboardButton('🌅 Прогноз на завтра', callback_data='notifications:2'),
        types.InlineKeyboardButton('🔮 На 5 дней', callback_data='notifications:3'),
        types.InlineKeyboardButton('🔮 На 10 дней', callback_data='notifications:4')
    )
    return btn
async def notifications_choice():
    btn = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.add(
        types.InlineKeyboardButton('🔔 Ежедневное уведомление', callback_data='notifications:everyday'),
        types.InlineKeyboardButton('📆 По дням недели', callback_data='notifications:week'),
        types.InlineKeyboardButton('↩️ Назад', callback_data='notifications:menu')
    )
    return btn
async def notifications_time():
    btn = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=4)
    btn.add(
        types.InlineKeyboardButton('⛔️ 00:00', callback_data='t1'),
        types.InlineKeyboardButton('⛔️ 01:00', callback_data='t2'),
        types.InlineKeyboardButton('⛔️ 02:00', callback_data='t3'),
        types.InlineKeyboardButton('⛔️ 03:00', callback_data='t4'),
        types.InlineKeyboardButton('⛔️ 04:00', callback_data='t5'),
        types.InlineKeyboardButton('⛔️ 05:00', callback_data='t6'),
        types.InlineKeyboardButton('⛔️ 06:00', callback_data='t7'),
        types.InlineKeyboardButton('⛔️ 07:00', callback_data='t8'),
        types.InlineKeyboardButton('⛔️ 08:00', callback_data='t9'),
        types.InlineKeyboardButton('⛔️ 09:00', callback_data='t10'),
        types.InlineKeyboardButton('⛔️ 10:00', callback_data='t11'),
        types.InlineKeyboardButton('⛔️ 11:00', callback_data='t12'),
        types.InlineKeyboardButton('⛔️ 12:00', callback_data='t13'),
        types.InlineKeyboardButton('⛔️ 13:00', callback_data='t14'),
        types.InlineKeyboardButton('⛔️ 14:00', callback_data='t15'),
        types.InlineKeyboardButton('⛔️ 15:00', callback_data='t16'),
        types.InlineKeyboardButton('⛔️ 16:00', callback_data='t17'),
        types.InlineKeyboardButton('⛔️ 17:00', callback_data='t18'),
        types.InlineKeyboardButton('⛔️ 18:00', callback_data='t19'),
        types.InlineKeyboardButton('⛔️ 19:00', callback_data='t20'),
        types.InlineKeyboardButton('⛔️ 20:00', callback_data='t21'),
        types.InlineKeyboardButton('⛔️ 21:00', callback_data='t22'),
        types.InlineKeyboardButton('⛔️ 22:00', callback_data='t23'),
        types.InlineKeyboardButton('⛔️ 23:00', callback_data='t24')
    )
    btn.add(
        types.InlineKeyboardButton('↩️ Назад', callback_data='notifications2:menu2')
    )
    return btn
async def notifications_week():
    btn = types.InlineKeyboardMarkup(resize_keyboard=True)
    btn.add(
        types.InlineKeyboardButton('🔔 Ежедневное уведомление', callback_data='notifications:everyday')
    )
    btn.add(
        types.InlineKeyboardButton('📆 Выберите день недели', callback_data='notifications:week2')
    )
    btn.add(
        types.InlineKeyboardButton('⛔️ Понедельник', callback_data='w1'),
        types.InlineKeyboardButton('⛔️ Вторник', callback_data='w2')
    )
    btn.add(
        types.InlineKeyboardButton('⛔️ Среда', callback_data='w3'),
        types.InlineKeyboardButton('⛔️ Четверг', callback_data='w4'),
        types.InlineKeyboardButton('⛔️ Пятница', callback_data='w5')
    )
    btn.add(
        types.InlineKeyboardButton('⛔️ Суббота', callback_data='w6'),
        types.InlineKeyboardButton('⛔️ Воскресенье', callback_data='w7')
    )
    btn.add(
        types.InlineKeyboardButton('↩️ Назад', callback_data='notifications:menu')
    )
    return btn

async def izmereniye():
    btn = types.InlineKeyboardMarkup(resize_keyboard=True)
    btn.add(
        types.InlineKeyboardButton('🕖 Формат времени', callback_data='i1')
    )
    btn.add(
        types.InlineKeyboardButton('⚪️ 12-часовой', callback_data='i2'),
        types.InlineKeyboardButton('🔘 24-часовой', callback_data='i3')
    )
    btn.add(
        types.InlineKeyboardButton('🌡 Температура', callback_data='i1')
    )
    btn.add(
        types.InlineKeyboardButton('🔘 °С', callback_data='i2'),
        types.InlineKeyboardButton('⚪️ °F', callback_data='i3')
    )
    btn.add(
        types.InlineKeyboardButton('💨 Скорость ветра', callback_data='i1')
    )
    btn.add(
        types.InlineKeyboardButton('🔘 м/с', callback_data='i2'),
        types.InlineKeyboardButton('⚪️ мили/ч', callback_data='i3')
    )
    btn.add(
        types.InlineKeyboardButton('💦 Осадки', callback_data='i1')
    )
    btn.add(
        types.InlineKeyboardButton('🔘 мм', callback_data='i2'),
        types.InlineKeyboardButton('⚪️ дюймы', callback_data='i3')
    )
    btn.add(
        types.InlineKeyboardButton('⏱ Давление', callback_data='i1')
    )
    btn.add(
        types.InlineKeyboardButton('🔘 мм рт. ст.', callback_data='i2'),
        types.InlineKeyboardButton('⚪️ дюймы рт. ст.', callback_data='i3')
    )
    return btn

async def text_btn():
    btn = types.InlineKeyboardMarkup(resize_keyboard=True)
    btn.add(
        types.InlineKeyboardButton('Текстовая версия', callback_data='textv')
    )
    return btn