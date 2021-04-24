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
            a = vk.docs.save(file="251102317|204132804|-1|536132|4c843b3731|gif|22610769|Mighty Lvl 2.gif|67696808d638acdee6c4d14498b20217|f668aadde2a051a99f6c79d1dacd11ef|m_4c843b3731|247|m:130x74,s:100x57,x:604x342,y:807x456,o:640x362|eyJkaXNrIjoiMiJ9")
            print(a['doc']['owner_id'], a['doc']['id'])
            a = event.obj.message['text']
            if a == 'Kamen Rider':
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Henshin!",
                                 random_id=random.randint(0, 2 ** 64))
            elif '<' in a and '-' in a:
                b = a.split('-')
                check = cur.execute("""SELECT id FROM Riders WHERE Command LIKE ?""", (b[1],)).fetchall()[0][0]
                if check >= 21 or check <= 24:
                    rider = cur.execute("""SELECT Henshin FROM Build WHERE key LIKE ? AND FullComm LIKE ?""",
                                       (b[1], a)).fetchall()[0][0]
                    henshin = cur.execute("""SELECT Pose FROM Build WHERE key LIKE ? AND FullComm LIKE ?""",
                                          (b[1], a)).fetchall()[0][0]
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=rider,
                                 random_id=random.randint(0, 2 **64),
                                 attachment=f"doc-204132804_{henshin}")
            elif 'Привет' in a or 'привет' in a or 'Хай' in a or 'Охайо' in a:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message='Хай-хай~!',
                                 random_id=random.randint(0, 2 ** 64))
            else:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Gomennasai, но я тебя не понял :(\nСкажи что-нибудь другое.",
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()