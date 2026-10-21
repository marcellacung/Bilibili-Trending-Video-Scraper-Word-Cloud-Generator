# Bilibili Trending Video Scraper & Word Cloud Generator

A Python-based web scraping project designed to collect trending video information from Bilibili (a popular Chinese video sharing platform). The scraped data (video titles and uploaders) is saved into a JSON file and analyzed using Natural Language Processing (NLP) to generate a visual Word Cloud representing the most frequent keywords.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Tools & Libraries](#-tools--libraries)
- [How to Run](#-how-to-run)
- [Results & Output](#-results--output)
- [Challenges & Limitations](#-challenges--limitations)
- [Author](#-author)

---

## 📖 Overview

With the rapid growth of User-Generated Content (UGC), analyzing trending topics provides valuable insights. This project automates the extraction of trending video data from the Bilibili API. It processes the video titles using Chinese word segmentation (`jieba`), filters out stop words, and visualizes the most prominent themes using a Word Cloud (`wordcloud`).

---

## ✨ Features

- ✅ **Automated Data Scraping**: Fetches trending videos from multiple pages (up to 20 pages) via the Bilibili API.
- ✅ **Robust Request Handling**: Uses custom HTTP headers (Cookies, User-Agent, Referer) to simulate browser behavior and bypass basic anti-scraping mechanisms.
- ✅ **Data Structuring**: Extracts Video ID, Title, and Owner (Uploader) and saves them neatly into a `.json` file.
- ✅ **Chinese Text Processing**: Utilizes `jieba` for accurate Chinese word segmentation.
- ✅ **Stop Words Filtering**: Removes common, meaningless words to improve analysis quality.
- ✅ **Data Visualization**: Generates a colorful Word Cloud highlighting the most popular topics.

---

## 🗂 Project Structure

```text
Bilibili-Trending-Video-Scraper-Word-Cloud-Generator/
│
├── README.md
├── .gitignore
├── Bilibili_spider.py          # Main Python script
│
└── result/                     # Output folder
    ├── B站热门视频.json        # Output JSON file (Scraped data)
    └── 词云.png                # Generated word cloud image
```

---

## 🛠 Tools & Libraries

This project is built using **Python** and the following essential libraries:

| Library | Purpose |
|---------|---------|
| `requests` | Sends HTTP GET requests to the Bilibili API. |
| `json` | Parses API responses and saves the extracted data. |
| `time` | Adds delays between requests to prevent getting blocked by rate limits. |
| `jieba` | Performs Chinese word segmentation on video titles. |
| `wordcloud` | Generates the word cloud visualization. |
| `matplotlib` | Displays the generated word cloud image. |

---

## 🚀 How to Run

### Prerequisites

- **Python 3.8** or higher.
- Install the required dependencies:
  ```bash
  pip install requests wordcloud matplotlib jieba
  ```

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/marCellacung/Bilibili-Trending-Video-Scraper-Word-Cloud-Generator.git
   cd Bilibili-Trending-Video-Scraper-Word-Cloud-Generator
   ```

2. **Run the script**
   ```bash
   python Bilibili_spider.py
   ```

3. **Input the number of pages** you want to scrape when prompted (e.g., `2`).

4. **Wait for the process** to finish. The script will print the scraped data in the console, save it to `result/B站热门视频.json`, and display the Word Cloud.

---

## 📸 Results & Output

### 1. JSON Data Structure
The scraped data is saved in a structured JSON format inside the `result` folder:
```json
[
    {
        "video id": 113582339922396,
        "title": "【左右声道】《cry for me》和《反方向的钟》",
        "owner": "风见杰克逊"
    },
    {
        "video id": 113607002036389,
        "title": "⚡️ 猫 咪 摇 摆 舞⚡️",
        "owner": "伢伢gagako"
    }
]
```

### 2. Word Cloud Visualization
The generated word cloud highlights the most frequent and popular keywords found in the video titles.

![Word Cloud](result/词云.png)

---

## ⚠️ Challenges & Limitations

### Challenges
1. **API Restrictions**: The Bilibili API limits scraping to a maximum of 20 pages per session.
2. **Cookie Dependency**: Requires valid authentication cookies in the headers. These cookies expire periodically, requiring manual updates.
3. **Text Preprocessing**: Creating a perfect stop words list is difficult; some irrelevant words might still slip through.

### Limitations & Future Improvements
- **Scope**: Currently only analyzes video titles. Future updates could include descriptions and top comments.
- **Dynamic Stop Words**: Implement a feature allowing users to input their own stop words via a text file.
- **Advanced NLP**: Incorporate Topic Modeling (LDA) or Sentiment Analysis for deeper insights into user preferences.

---

## 👤 Author

**MARCELLA**
- Institution: Shantou University
- Major: Data Science and Big Data Technology
- Email: 23marcella@stu.edu.cn

---

## 📄 License

This project is created for educational purposes as part of a Data Acquisition and Web Scraping assignment.
