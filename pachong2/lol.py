import requests

import re
import json

def getLOLImages():
    url_js ="http://lol.qq.com/biz/hero/champion.js"
    html_js = requests.get(url_js).text


    req = '"keys":(.*?),"data"'
    list_js = re.findall(req,html_js)


    dict_js = json.loads(list_js[0])


    pic_list = []
    for hero_id in dict_js:


        for i in range(20):
            num = str(i)
            if len(num) == 1:
                hero_num = "00" +num
            elif len(num) == 2:
                hero_num = "0" + num
            # print(hero_num)

            numstr = hero_id + hero_num
            url = 'http://ossweb-img.qq.com/images/lol/web201310/skin/big'+numstr+'.jpg'
            pic_list.append(url)
        # print(pic_list)

    list_filepath = []
    path = "/home/wang/test/pachong2/lolpic\\"
    for name in dict_js.values():
        # print(name)
        for i in range(20):
            file_path = path + name + str(i) +".jpg"
            list_filepath.append(file_path)

    #下载图片
    n = 0
    for picurl in pic_list:
        res = requests.get(picurl)
        n +=1
        if res.status_code == 200:
            print("正在下载%s:"%list_filepath[n])
            f = open(list_filepath[n],"wb")
            f.write(res.content)
            f.close()

            # with open(list_filepath[n],"wb") as f:
            #     f.write(res.content)




getLOLImages()

