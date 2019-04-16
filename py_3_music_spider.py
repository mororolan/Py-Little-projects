#-*- coding:utf-8 -*-
import requests
import re
# 第一步获取歌曲IDs
search_api='https://music.taihe.com/search'
keyword = {'key':'Taylor Swift'} #搜索的关键字，传递参数，通过字典构造
#发送请求
#get请求 params 是 传递的get的参数
response = requests.get(search_api,params=keyword)
#取出html的源码
response.encoding = 'utf-8'
html = response.text #文本信息用text 图片用content
# 通过正则表达式获取ID
ids = re.findall(r'{&quot;id&quot;:&quot;(\d+)&quot;',html)
#print(ids)
# 第二步获取歌曲信息
MP3_info_api = 'https://play.taihe.com/data/music/songlink'
data ={
        'songIds': ','.join(ids),  #拼接参数 例如
        'hq': 0, 'type': 'm4a,mp3', 'rate': '', 'pt': 0, 'flag': -1,
        's2p': -1, 'prerate': -1,'bwt': -1, 'dur': -1, 'bat': -1,
        'bp': -1, 'pos': -1, 'auto': -1
}
#data 就是 post的参数
res = requests.post(MP3_info_api, data=data)
# 返回的数据是json格式，直接调用json方法，转成字典
info = res.json() #拿到的就是preview里面的东西
#
# 第三步下载歌曲
# 根据数据的结构 获取歌曲的信息
song_info=info['data']['songList']
#循环
for song in song_info:
    #根据数据结构获取信息
    #歌名
    song_name= song['songName']
    #mp3 地址
    song_link = song['songLink']
    # 歌曲格式
    song_format=song['format']
    if song_link: #有可能没有地址 就是非空
         song_res=requests.get(song_link) #下载
         #写文件
         with open('%s.%s' %(song_name,song_format),'wb') as f:
             f.write(song_res.content) #歌曲是二进制