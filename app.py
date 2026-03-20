from flask import Flask, render_template, request
import requests
import xml.etree.ElementTree as ET
import os

app = Flask(__name__)
app.secret_key = "secret_key_123"

# --- GoogleトレンドRSS ---
def get_trends():
    try:
        url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=JP"
        res = requests.get(url, timeout=5)

        root = ET.fromstring(res.content)

        trends = []
        for item in root.findall(".//item")[:5]:
            title = item.find("title").text
            trends.append(title)

        return trends

    except:
        return ["人気商品", "話題グッズ", "注目アイテム"]

# --- メイン ---
@app.route("/", methods=["GET", "POST"])
def home():

    ideas = []

    if request.method == "POST":

        trends = get_trends()

        for trend in trends:

            idea = "関連グッズ"
            mercari_kw = trend + " グッズ"
            amazon_kw = trend + " グッズ"
            m_price = 2500
            a_price = 3800
            profit = a_price - m_price

            post = f"""今トレンドの「{trend}」🔥

実はこれ、物販チャンスです。

狙い目👇
・関連グッズ
・限定商品
・トレンド便乗

今のうちにチェックで利益につながる可能性あり💰

#副業 #せどり #物販"""

            ideas.append({
                "trend": trend,
                "idea": idea,
                "post": post,
                "mercari_url": f"https://www.mercari.com/jp/search/?keyword={mercari_kw}",
                "amazon_url": f"https://www.amazon.co.jp/s?k={amazon_kw}",
                "m_price": m_price,
                "a_price": a_price,
                "profit": profit
            })

    return render_template("index.html", ideas=ideas)

# --- Render対応 ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)