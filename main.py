# Created by X-Corporation


TODO = [111, 112, 113, 114, 115, 116, 117, 118, 119, 121, 122, 123, 124, 125, 126, 127, 128, 129, 131, 132, 133,
        134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 146, 147, 148, 149, 151, 152, 153, 154, 155, 156,
        157, 158, 159, 161, 162, 163, 164, 165, 166, 167, 168, 169, 171, 172, 173, 174, 175, 176, 177, 178, 179]

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import sqlite3


def main():
    global TODO
    print('KRB Power On')
    krdb = sqlite3.connect('data/KamenRiderDataBase.sqlite')
    cur = krdb.cursor()
    vk_session = vk_api.VkApi(
        token='0f6a4cbc6fd03a40fa122165a1061c881c49bb78a1a7b479a4c6a87f1b4b40a5b46c2fcd5b5651212df84',
    api_version='5.130')
    vk = vk_session.get_api()
    longpoll = VkBotLongPoll(vk_session, '204132804')
    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])
            a = event.obj.message['text']
            if '<' in a and '-' in a:
                b = a.split('-')
                try:
                    check = cur.execute("""SELECT id FROM Riders WHERE Command LIKE ?""", (b[1],)).fetchall()[0][0]
                except Exception:
                    check = 0
                if check == 0:
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f'Ой, похоже ты ввёл неверную команду. :('
                                             f'\nМожет быть, ты попробуешь ещё раз?',
                                     random_id=random.randint(0, 2 ** 64))
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f'Напоминаю, что список всех комманд можно вызвать,'
                                             f'введя команду /help.',
                                     random_id=random.randint(0, 2 ** 64))
                elif 179 >= check >= 111:
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f'Извиняй, но такого Райдера у меня пока нет :(\n'
                                             f'Не расстраивайся, уверен, в следующем обновлении'
                                             f' он обязательно появится!',
                                     random_id=random.randint(0, 2 ** 64))
                elif check == 11:
                    rider = cur.execute("""SELECT Henshin FROM Kuuga WHERE key LIKE ? AND FullComm LIKE ?""",
                                        (b[1], a)).fetchall()[0][0]
                    try:
                        henshin = cur.execute("""SELECT Pose FROM Kuuga WHERE key LIKE ? AND FullComm LIKE ?""",
                                              (b[1], a)).fetchall()[0][0]
                    except Exception:
                        henshin = 0
                elif 29 >= check >= 21:
                    rider = cur.execute("""SELECT Henshin FROM Agito WHERE key LIKE ? AND FullComm LIKE ?""",
                                        (b[1], a)).fetchall()[0][0]
                    try:
                        henshin = cur.execute("""SELECT Pose FROM Agito WHERE key LIKE ? AND FullComm LIKE ?""",
                                              (b[1], a)).fetchall()[0][0]
                    except Exception:
                        henshin = 0
                elif 39 >= check >= 31:
                    rider = cur.execute("""SELECT Henshin FROM Ryuki WHERE key LIKE ? AND FullComm LIKE ?""",
                                        (b[1], a)).fetchall()[0][0]
                    try:
                        henshin = cur.execute("""SELECT Pose FROM Ryuki WHERE key LIKE ? AND FullComm LIKE ?""",
                                              (b[1], a)).fetchall()[0][0]
                    except Exception:
                        henshin = 0
                elif 49 >= check >= 41:
                    rider = cur.execute("""SELECT Henshin FROM Faiz WHERE key LIKE ? AND FullComm LIKE ?""",
                                        (b[1], a)).fetchall()[0][0]
                    try:
                        henshin = cur.execute("""SELECT Pose FROM Faiz WHERE key LIKE ? AND FullComm LIKE ?""",
                                              (b[1], a)).fetchall()[0][0]
                    except Exception:
                        henshin = 0
                elif 59 >= check >= 51:
                    rider = cur.execute("""SELECT Henshin FROM Blade WHERE key LIKE ? AND FullComm LIKE ?""",
                                        (b[1], a)).fetchall()[0][0]
                    try:
                        henshin = cur.execute("""SELECT Pose FROM Blade WHERE key LIKE ? AND FullComm LIKE ?""",
                                              (b[1], a)).fetchall()[0][0]
                    except Exception:
                        henshin = 0
                elif 69 >= check >= 61:
                    rider = cur.execute("""SELECT Henshin FROM Hibiki WHERE key LIKE ? AND FullComm LIKE ?""",
                                        (b[1], a)).fetchall()[0][0]
                    try:
                        henshin = cur.execute("""SELECT Pose FROM Hibiki WHERE key LIKE ? AND FullComm LIKE ?""",
                                              (b[1], a)).fetchall()[0][0]
                    except Exception:
                        henshin = 0
                elif 79 >= check >= 71:
                    rider = cur.execute("""SELECT Henshin FROM Kabuto WHERE key LIKE ? AND FullComm LIKE ?""",
                                        (b[1], a)).fetchall()[0][0]
                    try:
                        henshin = cur.execute("""SELECT Pose FROM Kabuto WHERE key LIKE ? AND FullComm LIKE ?""",
                                              (b[1], a)).fetchall()[0][0]
                    except Exception:
                        henshin = 0
                elif 89 >= check >= 81:
                    rider = cur.execute("""SELECT Henshin FROM Den-O WHERE key LIKE ? AND FullComm LIKE ?""",
                                        (b[1], a)).fetchall()[0][0]
                    try:
                        henshin = cur.execute("""SELECT Pose FROM Den-O WHERE key LIKE ? AND FullComm LIKE ?""",
                                              (b[1], a)).fetchall()[0][0]
                    except Exception:
                        henshin = 0
                elif 99 >= check >= 91:
                    rider = cur.execute("""SELECT Henshin FROM Kiva WHERE key LIKE ? AND FullComm LIKE ?""",
                                        (b[1], a)).fetchall()[0][0]
                    try:
                        henshin = cur.execute("""SELECT Pose FROM Kiva WHERE key LIKE ? AND FullComm LIKE ?""",
                                              (b[1], a)).fetchall()[0][0]
                    except Exception:
                        henshin = 0
                elif 109 >= check >= 101:
                    rider = cur.execute("""SELECT Henshin FROM Decade WHERE key LIKE ? AND FullComm LIKE ?""",
                                        (b[1], a)).fetchall()[0][0]
                    try:
                        henshin = cur.execute("""SELECT Pose FROM Decade WHERE key LIKE ? AND FullComm LIKE ?""",
                                              (b[1], a)).fetchall()[0][0]
                    except Exception:
                        henshin = 0
                elif 189 >= check >= 181:
                    rider = cur.execute("""SELECT Henshin FROM Ex-Aid WHERE key LIKE ? AND FullComm LIKE ?""",
                                        (b[1], a)).fetchall()[0][0]
                    try:
                        henshin = cur.execute("""SELECT Pose FROM Ex-Aid WHERE key LIKE ? AND FullComm LIKE ?""",
                                              (b[1], a)).fetchall()[0][0]
                    except Exception:
                        henshin = 0
                elif 199 >= check >= 191:
                    rider = cur.execute("""SELECT Henshin FROM Build WHERE key LIKE ? AND FullComm LIKE ?""",
                                        (b[1], a)).fetchall()[0][0]
                    try:
                        henshin = cur.execute("""SELECT Pose FROM Build WHERE key LIKE ? AND FullComm LIKE ?""",
                                              (b[1], a)).fetchall()[0][0]
                    except Exception:
                        henshin = 0
                elif 209 >= check >= 201:
                    rider = cur.execute("""SELECT Henshin FROM Zi-O WHERE key LIKE ? AND FullComm LIKE ?""",
                                        (b[1], a)).fetchall()[0][0]
                    try:
                        henshin = cur.execute("""SELECT Pose FROM Zi-O WHERE key LIKE ? AND FullComm LIKE ?""",
                                              (b[1], a)).fetchall()[0][0]
                    except Exception:
                        henshin = 0
                if int(henshin) != 0:
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=rider,
                                     random_id=random.randint(0, 2 ** 64),
                                     attachment=f"doc-204132804_{henshin}")
                else:
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=rider,
                                     random_id=random.randint(0, 2 ** 64))
            elif 'Кари' in a:
                if 'Привет' in a or 'привет' in a or 'Хай' in a or 'Охайо' in a:
                    c = random.choice(['Хай-хай!~', 'Привет!', 'Ohayo!', 'Хелло!'])
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f'{c}',
                                     random_id=random.randint(0, 2 ** 64))
                elif ('Какой' in a or 'какой' in a) and ('Любимый' in a or 'любимый' in a) and '?' in a:
                    if 'цвет' in a or 'Цвет' in a:
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=f'Мой любимый цвет - Маджента.',
                                         random_id=random.randint(0, 2 ** 64))
                    elif 'Райдер' in a or 'Rider' in a or '' in a or '' in a:
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=f'Мой любимый Райдер - Дикейд, потому что он умеет '
                                                 f'превращаться в других райдеров, и потому что он моего '
                                                 f'любимого цвета.',
                                         random_id=random.randint(0, 2 ** 64))
            elif '/help' in a:
                b = a.split('-')
                if len(b) == 1:
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f'Для получения базовой формы райдера введи "<kr-Ключ райдера".'
                                             f'Для получения финальной формы - "<final-Ключ райдера".'
                                             f'Для любой другой формы нужно написать '
                                             f'"<form-Ключ райдера-Ключ формы."',
                                     random_id=random.randint(0, 2 ** 64))
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f'Имена рабочих райдеров (на данный момент):',
                                     random_id=random.randint(0, 2 ** 64))
                    krlist = cur.execute("""SELECT Name FROM Riders WHERE id NOT BETWEEN ? AND ?""",
                                         (TODO[0], TODO[-1])).fetchall()
                    line = ''
                    for elem in krlist:
                        if line == '':
                            line = line + elem[0]
                        else:
                            line = line + ', ' + elem[0]
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=line,
                                     random_id=random.randint(0, 2 ** 64))
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f'Для справки по каждому Райдеру введи "/help-Имя райдера":',
                                     random_id=random.randint(0, 2 ** 64))
                else:
                    try:
                        check = cur.execute("""SELECT id FROM Riders WHERE Name LIKE ?""", (b[1],)).fetchall()[0][0]
                        key = cur.execute("""SELECT Command FROM Riders WHERE Name LIKE ?""", (b[1],)).fetchall()[0][0]
                    except Exception:
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=f'Ой, похоже ты ввёл неверную команду. :('
                                                 f'\nМожет быть, ты попробуешь ещё раз?',
                                         random_id=random.randint(0, 2 ** 64))
                    if check == 11:
                        rider = cur.execute("""SELECT FormName, FullComm FROM Kuuga WHERE key LIKE ?""",
                                            (key,)).fetchall()
                    elif 29 >= check >= 21:
                        rider = cur.execute("""SELECT FormName, FullComm FROM Agito WHERE key LIKE ?""",
                                            (key,)).fetchall()
                    elif 39 >= check >= 31:
                        rider = cur.execute("""SELECT FormName, FullComm FROM Ryuki WHERE key LIKE ?""",
                                            (key,)).fetchall()
                    elif 49 >= check >= 41:
                        rider = cur.execute("""SELECT FormName, FullComm FROM Faiz WHERE key LIKE ?""",
                                            (key,)).fetchall()
                    elif 59 >= check >= 51:
                        rider = cur.execute("""SELECT FormName, FullComm FROM Blade WHERE key LIKE ?""",
                                            (key,)).fetchall()
                    elif 69 >= check >= 61:
                        rider = cur.execute("""SELECT FormName, FullComm FROM Hibiki WHERE key LIKE ?""",
                                            (key,)).fetchall()
                    elif 79 >= check >= 71:
                        rider = cur.execute("""SELECT FormName, FullComm FROM Kabuto WHERE key LIKE ?""",
                                            (key,)).fetchall()
                    elif 89 >= check >= 81:
                        rider = cur.execute("""SELECT FormName, FullComm FROM Den-O WHERE key LIKE ?""",
                                            (key,)).fetchall()
                    elif 99 >= check >= 91:
                        rider = cur.execute("""SELECT FormName, FullComm FROM Kiva WHERE key LIKE ?""",
                                            (key,)).fetchall()
                    elif 109 >= check >= 101:
                        rider = cur.execute("""SELECT FormName, FullComm FROM Decade WHERE key LIKE ?""",
                                            (key,)).fetchall()
                    elif 189 >= check >= 181:
                        rider = cur.execute("""SELECT FormName, FullComm FROM Ex-Aid WHERE key LIKE ?""",
                                            (key,)).fetchall()
                    elif 199 >= check >= 191:
                        rider = cur.execute("""SELECT FormName, FullComm FROM Build WHERE key LIKE ?""",
                                            (key,)).fetchall()
                    elif 209 >= check >= 201:
                        rider = cur.execute("""SELECT FormName, FullComm FROM Zi-O WHERE key LIKE ?""",
                                            (key,)).fetchall()
                    line = ''
                    for elem in rider:
                        line = line + elem[0] + ': ' + elem[1] + '\n'
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=line,
                                     random_id=random.randint(0, 2 ** 64))
            else:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Gomennasai, но я тебя не понял :(\nСкажи что-нибудь другое.",
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()