from telethon import TelegramClient, sync
from telethon.tl.types import InputMessagesFilterPhotos
import os

proxy = None
# =============需要被替换的值=================
'''
api_id 你的api id
api_hash 你的api hash
channel_link 要下载图片的频道链接
proxy 将localhost改成代理地址,12345改成代理端口
picture_storage_path 图片下载到的路径
'''
api_id = 123456
api_hash = "23jhbfj23kbf3wkfbwk3j8w3fbesiug"
channel_link = "https://t.me/xxxx" #你要下载的频道链接
proxy = ("socks5", "localhost", 12345)  # 不需要代理的话删掉该行
picture_storage_path = "picture_storage_path" #下载目录

# 获取已经下载文件ID
dir_name = './picture_storage_path/' #如果报错请在脚本存放里新建'picture_storage_path'文件夹
file_list = os.listdir(dir_name)
file_list_id = [int(i.replace('.jpg', '')) for i in file_list ]
print(f'已下载的图片id{file_list_id}')

# TG参数
client = TelegramClient('my_session', api_id=api_id, api_hash=api_hash, proxy=proxy).start()
photos = client.get_messages(channel_link, None, filter=InputMessagesFilterPhotos)

#获取频道图片id
photo_id = [i.id for i in photos]
print(f'频道所有图片id{photo_id}')

#去重
photo_id_OK = set(photo_id) - set(file_list_id)
print(f'未下载的图片id{photo_id_OK}')

#下载图片
total = len(photo_id_OK)
index = 0
for photo in photos:
    if photo.id in photo_id_OK :
        filename = picture_storage_path + "/" + str(photo.id) + ".jpg"
        index = index + 1
        print("downloading:", index, "/", total, " : ", filename)
        client.download_media(photo, filename)

client.disconnect()
print("Done.")
