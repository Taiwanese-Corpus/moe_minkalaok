# 臺灣閩南語卡拉OK正字字表

## 內容說明 
有鑑於目前坊間閩南語伴唱帶，歌詞字幕之閩南語用字，常借用華語用詞或採用華語借音，造成閩南語漢字使用的混淆。為改善這種混亂情形，教育部特成立「閩南語卡拉OK正字小組」，就國內KTV閩南語歌曲中選出50首較具代表性之歌曲，並以「臺灣閩南語卡拉OK正字字表」方式，呈現教育部建議用字與歌詞原文用字之差異。

在「臺灣閩南語卡拉OK正字字表」中的「歌詞建議用字」欄位，是以教育部公告的「臺灣閩南語推薦用字（第1、2批）」為依據。至於歌詞原文之用字，另於「原文用字」欄位呈現，以方便對照。


## 呈現說明

1.「歌詞建議用字」欄位中，較大字體為「臺灣閩南語推薦用字（第1、2批）」，其餘部分為華語同形字。
2.兩個「*」之間的歌詞為華語。
3.歌曲原文用字符合推薦用字者，亦呈現於「歌詞建議用字」欄位中。

## 資料處理

### 文字格式
轉成`minkalaok_970501.txt`
```
pdftotext -layout minkalaok_970501.pdf 
```

### 臺灣言語資料庫
#### 產生yaml格式
```bash
sudo apt-get install -y python3 python-virtualenv
virtualenv --python=python3 venv
. venv/bin/activate
pip install pyyaml
python 產生臺灣言語資料庫格式.py
```

#### 匯入資料
在`臺灣言語資料庫`專案目錄下
```bash
python manage.py 匯入資料 https://Taiwanese-Corpus.github.io/moe_minkalaok/閩南語卡拉OK正字字表.yaml
```