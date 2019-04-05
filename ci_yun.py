import jieba
import wordcloud
import csv
import json
import re
from PIL import Image
import numpy as np
import codecs


def read_csv():
    word_str = ''
    with codecs.open('info.csv', encoding='utf-8') as f:
         for line in f.readlines():
             try:
                 line = line.replace('"[','').replace(']"','')
                 data = eval(line)
                 word_str += data['announcementTitle']
             except:
                 continue
         return re.sub(r'(关于|进展|公告|公司|股东|股份|部分|使用|情况|提示性|年度|进行)','',word_str)
    
def gen_img(word_str):
    result = jieba.lcut(word_str)
    # img = Image.open('123.jpeg')
    # mask = np.array(img)
    wcObj = wordcloud.WordCloud(
        # mask=mask,
        background_color="black",
        font_path="simkai.ttf",
        min_font_size=50,
        max_font_size=300,
        width=1500,
        height=1200,
        max_words=800,
        collocations=False,
    )
    wcObj.generate(",".join(result))
    wcObj.to_file('公告词云.jpg')
   
    
if __name__ == '__main__':
    s = read_csv()
    gen_img(s)

