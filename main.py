# Created by X-Corporation


import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import sqlite3


def main():
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
                elif 199 >= check >= 191:
                    rider = cur.execute("""SELECT Henshin FROM Build WHERE key LIKE ? AND FullComm LIKE ?""",
                                        (b[1], a)).fetchall()[0][0]
                    henshin = cur.execute("""SELECT Pose FROM Build WHERE key LIKE ? AND FullComm LIKE ?""",
                                          (b[1], a)).fetchall()[0][0]
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=rider,
                                 random_id=random.randint(0, 2 ** 64),
                                 attachment=f"doc-204132804_{henshin}")
            elif 'Кари' in a:
                if 'Привет' in a or 'привет' in a or 'Хай' in a or 'Охайо' in a:
                    c = random.choice(['Хай-хай!~', 'Привет!', 'Ohayo!', 'Хелло!'])
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f'{c}',
                                     random_id=random.randint(0, 2 ** 64))
            else:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Gomennasai, но я тебя не понял :(\nСкажи что-нибудь другое.",
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()