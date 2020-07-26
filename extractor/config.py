# -*- coding: utf-8 -*-
"""
Created on 2017-12-07 15:57
---------
@summary: 正文提取的配置
---------
@author: Boris
"""
## 提取正文的阈值配置
MIN_PARAGRAPH_LENGHT = 5  # 最小段落长度
MAX_PARAGRAPH_DISTANCE = 5  # 正文段落与段落之间的最大距离 段落之间可能有空白行
MIN_PARAGRAPH_AND_CONTENT_PROPORTION = 0.5  # p标签内的文字长度/正文长度 最小占比
MIN_COUNTENT_WORDS = 500  # 最小文章内容长度
RELEASE_TIME_OFFSET = (
    10
)  # 发布时间偏离正文区域的距离， 如正文在 10~28 行 ，发布时间在 (10-RELEASE_TIME_OFFSET) ~ (28 + RELEASE_TIME_OFFSET) 行之内

USEFUL_TAG = [  # html 中需要保留的标签
    r"<img(.|\n)+?>",
    r"<p(.|\n)*?>",
    r"</p>",
    r"<span(.|\n)+?>",
    r"</span>",
    r"<strong.*?>",
    r"</strong>",
    r"<br.*?/>",
]

# 时间正则
# 日期
DAY_REGEXS = [
    "(\d{4}[-|/|.]\d{1,2}[-|/|.]\d{1,2})",
    "(\d{2}[-|/|.]\d{1,2}[-|/|.]\d{1,2})",
    "(\d{4}年\s*?\d{1,2}\s*?月\s*?\d{1,2}\s*?日)",
    "(\d{2}年\s*?\d{1,2}\s*?月\s*?\d{1,2}\s*?日)",
    # '(\d{1,2}月\d{1,2}日)',
    # '(\d{1,2}日)'
]

# 时间
TIME_REGEXS = [
    "([0-1]?[0-9]:[0-5]?[0-9]:[0-5]?[0-9])",
    "([2][0-3]:[0-5]?[0-9]:[0-5]?[0-9])",
    "([0-1]?[0-9]:[0-5]?[0-9])",
    "([2][0-3]:[0-5]?[0-9])",
    "([1-24]\d时[0-60]\d分)" "([1-24]\d时)",
]


# 将时间和日期的正则组合在一起
DAY_TIME_REGEXS = []
for day_regex in DAY_REGEXS:
    for time_regex in TIME_REGEXS:
        DAY_TIME_REGEXS.append(day_regex[:-1] + "\s*?" + time_regex[1:])

DAY_TIME_REGEXS.extend(DAY_REGEXS)

# 作者
AUTHOR_REGEXS = [
    r"责编[：|:| |丨|/]",
    r"作者[：|:| |丨|/]",
    r"编辑[：|:| |丨|/]",
    r"文[：|:| |丨|/]",
    r"撰文[：|:| |丨|/]",
]

NAME = "([\u4E00-\u9FA5]{2,5})[^\u4e00-\u9fa5|:|：]"
AUTHOR_REGEXS_TEXT = [
    AUTHOR_REGEX + "\s*" + NAME for AUTHOR_REGEX in AUTHOR_REGEXS
]  # 基于文字
AUTHOR_REGEX_TAG = ['(?i)<meta.*?author.*?content="(.*?)"']  # 基于标签

# 特殊网站，标题提取自定义
SPECIAL_TITLE = {
    "qz001.gov.cn": "<h4>(.*?)</h4>",
    "payh.gov.cn": '<font color="#000000">(.*?)</font>',
}
