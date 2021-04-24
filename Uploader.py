import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import sqlite3


vk_session = vk_api.VkApi(
    token='0f6a4cbc6fd03a40fa122165a1061c881c49bb78a1a7b479a4c6a87f1b4b40a5b46c2fcd5b5651212df84',
    api_version='5.130')
vk = vk_session.get_api()
print('KRB Uploader On')
a = input()
while a != '':
    b = vk.docs.save(file=a)
    print(b['doc']['owner_id'], b['doc']['id'])
    a = input()
print('KRB Uploader Off')
