### Py-Little-projects | Python小项目
Py = Please Try （雾很大
如果你觉着对你有用，请点个小星星吧qwq

    

### 项目① 用Python实现噪点图像的生成 
生成一张320*240的随机黑白噪点图，并且在程序里显示FPS性能，FPS（frame per second）
参考如下：
>
需要调的包：
* time
* random
* Tkinter
* Image

![image](http://github.com/mororolan/Py-Little-projects/raw/master/test.jpg)

### 项目② baidu音乐爬虫的学习与实战  #Spider

> 学习内容 <br>
1 爬虫本质<br>
网络爬虫 （本质：模拟浏览器行为）<br>
模拟浏览器，访问互联网资源，根据我们制定的规则，批量的下载我们所需要的数据的程序。<br>
2 利用谷歌浏览器分析http请求<br>
网络资源（可访问到的）<br>
url 全球统一资源定位符<br>
f12 打开<br>
network选项监控http请求<br>
3 分析百度音乐的请求流程<br>
下载MP3<br>

> 倒推法<br>
1	先找到MP3下载请求<br>
2	歌曲的下载地址也是从服务器请求回来的，<br>
找到下载地址的那个请求（有顺序哒）<br>
3 找到歌曲ID<br>
4 通过python去实现请求<br>

### 项目③ 简单的豆瓣短评爬取代码 #Spider #正则表达式
> 不到20行代码的小爬虫<br>
正则表达式的运用
