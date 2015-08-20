# -*- coding: utf-8 -*-
from 臺灣言語資料庫.資料模型 import 來源表
from 臺灣言語資料庫.資料模型 import 版權表
from os.path import dirname, abspath, join
import re
from 臺灣言語資料庫.資料模型 import 文本表


class 整合到資料庫:
    閩南語卡拉OK正字小組 = 來源表.objects.get_or_create(名='閩南語卡拉OK正字小組')[0]
    薛丞宏 = 來源表.objects.get_or_create(名='薛丞宏')[0]
    版權 = 版權表.objects.get_or_create(版權='無版權')[0]
    專案目錄 = join(dirname(abspath(__file__)), '..')
    公家內容 = {
        '來源': 閩南語卡拉OK正字小組,
        '版權': 版權,
        '種類': '語句',
        '語言腔口': '閩南語',
        '著作所在地': '臺灣',
        '著作年': '2008',
    }

    def 加詞目(self, 收錄者, 舊, 新):
        公家內容 = {
            '收錄者': 收錄者,
        }
        公家內容.update(self.公家內容)

        母語內容 = {
            '文本資料': 舊,
        }
        母語內容.update(公家內容)
        文本 = 文本表.加資料(母語內容)
        新母語內容 = {
            '文本資料': 新,
        }
        新母語內容.update(公家內容)
        文本.校對做(新母語內容)

    def 資料抓出來(self):
        歌詞檔 = join(self.專案目錄, 'minkalaok_970501.txt')
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


def 走(收錄者=整合到資料庫.薛丞宏):
    到資料庫 = 整合到資料庫()
    for 新, 舊 in 到資料庫.資料抓出來():
        print(新, 舊)
        到資料庫.加詞目(收錄者, 舊, 新)
    return
