import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random


def main():
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
            if event.obj.message['text'] == 'Kamen Rider':
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Henshin!",
                                 random_id=random.randint(0, 2 ** 64))
            elif "<kr-bld" in event.obj.message['text']:
                a = vk.docs.save(file="251102317|204132804|-1|536132|4c75ea26fc|gif|17901096|RabbitTank.gif|"
                                      "8c7be4c26dca7bd8f1942bae80f91298|c741b81ab6ffc1f0f0dae38c4c1dcf34|m_4c75ea26fc|"
                                      "580|m:130x74,s:100x57,o:320x180|eyJkaXNrIjoiOCJ9")
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message='Build!\nHagane no Moonsaulto! RabbitTank! Yeaahh!',
                                 random_id=random.randint(0, 2 ** 64),
                                 attachment=f"doc{a['doc']['owner_id']}_{a['doc']['id']}")
            else:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="None",
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()