import vk
import time
import datetime
print('VKBot')
session = vk.Session('9f47aaceb6d8e648190009703fed8cbb360f6feba81b97d2dc5f1aae9bd9717f5fdbf7c6890b0e8f6d759')
api = vk.API(session)
messages = api.messages.get()
commands = ['Версия приложения', 'Что твариться в мире?', 'привет', 'какой фильм посмотреть?']
while (True):
    messages = [(m['uid'], m['mid'], m['body'])
               for m in messages[1:] if m['body'] in commands and m['read_state'] == 0]

    for m in messages:
        user_id = m[0]
        message_id = m[1]
        comand = m[2]

        date_time_string = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')

        if comand == 'Версия приложения':
           api.messages.send(user_id=user_id,
                             message=date_time_string + '\n>VKBot v0.1\n>Разработал: Овчаров Роман')

        if comand == 'Что твариться  в мире?':
           api.messages.send(user_id=user_id,
                             message=date_time_string + '\n>Всё как обычно, доллар 60+. ')

        if comand == 'привет':
            api.messages.send(user_id=user_id,
                              message=date_time_string + '\n>Привет,как ты?!')
        if comand == 'какой фильм посмотреть?':
            api.messages.send(user_id=user_id,
                              message=date_time_string + '\n>Я что? википедия? для кого придумывали GOOGLE?!')

    ids = ', '.join([str(m[1]) for m in messages])

    if ids:
        api.messages.markAsRead(message_ids=ids)


    time.sleep(2)


