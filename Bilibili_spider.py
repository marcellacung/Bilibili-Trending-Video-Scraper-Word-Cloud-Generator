import requests
import json
import time
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

# 加载停用词列表
def LoadStopWords():
    stop_words = set(["你", "我", "的", "了", "在", "是", "不", "有", "和", "就", "人", "都", "很", "也", "这", "对", "为", "上", "下", "来", "说", "要", "一个", "会", "着", "但", "能", "等", "把", "把", "如果", "那么"
    ])
    return stop_words

# 定义请求函数
def GetResponse(url):
    headers = {
        # 用户信息, 常用于检测是否有登陆账号
        'Cookie': 'buvid3=11AAC30B-A2E0-E01B-67F3-574D12C15A7618588infoc; b_nut=1721980718; _uuid=22B89FBA-8892-6659-644C-6C10677B4656218920infoc; enable_web_push=DISABLE; buvid4=74253F61-4BC9-D41D-AB33-BE1A9ED8066123590-024072607-5rqJtL5qfrQjwYfnTAyjaA==; rpdid=|(um|J|RkYRu0Ju~kum)|~Rl; DedeUserID=1356559196; DedeUserID__ckMd5=dfd3cb583802da8a; header_theme_version=CLOSE; fingerprint=3cd20d9e0f402f9037de48ba0243c15f; buvid_fp_plain=undefined; CURRENT_QUALITY=80; hit-dyn-v2=1; CURRENT_FNVAL=4048; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzAwODgzODUsImlhdCI6MTcyOTgyOTEyNSwicGx0IjotMX0.LCulQ19sdRJ2APNjFLyeCBqKqhuMTiV-yO6oiSsVGDg; bili_ticket_expires=1730088325; SESSDATA=061ebfb4,1745477840,fb432*a2CjBaHYIEZ66fYkUvhSvBtL4V7pGT-brLi9FbwaJFtxFNWm8_evtRzEDmOIuvcorTuvUSVl91Ml9LdHNlRDdzTWlPWG9JeDhnVVdPSFdwZGN3UnRaY2w4YzRJTUQ1UENyTklodzZzUG5YcEduRjczdzE4cDByZXRKUTJpNXFxWE9mb3E4c2xBZEFRIIEC; bili_jct=3e7fc43fdda56efb2b2de1a82dc32354; sid=4jtig85c; buvid_fp=3cd20d9e0f402f9037de48ba0243c15f; browser_resolution=1265-680; home_feed_column=4; share_source_origin=copy_web; bsource=share_source_copylink_web; bp_t_offset_1356559196=992953794104918016; b_lsid=CEB31492_192CE8B5E94',
        # 防盗链, 告诉服务器请求链接是从哪里跳转过来的
        'Referer': 'https://www.bilibili.com/v/popular/all/?spm_id_from=333.1007.0.0',
        # 用户代理, 表示浏览器基本身份信息
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.3.5211 SLBChan/105'
    }
    try:
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"请求失败: {e}")
        return None

# 定义多页爬取函数
def GetMultiPageInfo():
    try:
        pages = int(input("请输入要爬取的页数(最大页数20): "))
    except ValueError:
        print("请输入有效的页数（数字）。")
        return

    all_data = []  # 用于存储所有页数据
    titles = []  # 用于存储所有视频标题
    for page in range(1, pages + 1):
        print(f"正在抓取第 {page} 页数据...")
        url = f'https://api.bilibili.com/x/web-interface/popular?ps=20&pn={page}&web_location=333.934'
        response = GetResponse(url=url)
        if not response:
            print(f"第 {page} 页数据抓取失败，跳过...")
            continue
        try:
            Data = response.json()
            result = Data.get('data', {}).get('list', [])
            for index in result:
                aid = index.get('aid', '未知')
                title = index.get('title', '未知')
                owner = index['owner'].get('name', '未知') if 'owner' in index else '未知'
                print(f"视频号:{aid}; 标题：{title}; 作者:{owner}")
                all_data.append({
                    "video id": aid,
                    "title": title,
                    "owner": owner
                })
                titles.append(title)  # 收集视频标题
        except (json.JSONDecodeError, KeyError) as e:
            print(f"第 {page} 页数据解析失败: {e}")
        time.sleep(1)  # 加入延迟以避免被服务器封禁

    # 将数据保存到文件中
    with open('B站热门视频.json', 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)
    print(f"已抓取 {len(all_data)} 条数据并保存在json文件中")

    # 生成词云图
    GenerateWordcCoud(titles)

# 生成词云图函数
def GenerateWordcCoud(titles):
    # 合并所有视频标题为一个字符串
    text = ' '.join(titles)

    # 使用jieba进行分词，并过滤停用词
    stop_words = LoadStopWords()  # 加载停用词
    word_list = jieba.cut(text)
    filtered_words = [word for word in word_list if word not in stop_words and len(word) > 1]

    # 重新连接过滤后的分词结果
    processed_text = ' '.join(filtered_words)

    # 创建词云对象
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        font_path='simhei.ttf'  # 设置中文字体路径，确保正确显示中文
    ).generate(processed_text)

    # 显示词云图
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    GetMultiPageInfo()
