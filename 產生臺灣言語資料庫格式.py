# -*- coding: utf-8 -*-
from os.path import dirname, abspath, join
import re

import yaml


_專案目錄 = dirname(abspath(__file__))


class 處理資料:

    def 資料抓出來(self):
        歌詞檔 = join(_專案目錄, 'minkalaok_970501.txt')
        全部資料 = set()
        with open(歌詞檔) as 檔案:
            for 一逝 in 檔案:
                資料 = 一逝.split()
                if len(資料) >= 3 and 資料[-1] != '曲名':
                    新, 舊 = 資料[-3:-1]
                    全部資料.add((新, 舊))
        提掉華語 = re.compile('\*.*\*')
        for 新, 舊 in 全部資料:
            yield 提掉華語.sub('', 新).replace('', '䆀'), 提掉華語.sub('', 舊)


if __name__ == '__main__':
    資料內容 = {
        '來源': '閩南語卡拉OK正字小組',
        '版權': '無版權',
        '種類': '語句',
        '語言腔口': '閩南語',
        '著作所在地': '臺灣',
        '著作年': '2008',
        '下層': []
    }
    到資料庫 = 處理資料()
    for 新, 舊 in 到資料庫.資料抓出來():
        print(新, 舊)
        資料內容['下層'].append({'相關資料組': [舊, 新]})
    with open(join(_專案目錄, '閩南語卡拉OK正字字表.yaml'), 'w') as 檔案:
        yaml.dump(資料內容, 檔案, default_flow_style=False, allow_unicode=True)
