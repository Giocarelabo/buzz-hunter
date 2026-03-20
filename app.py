from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)
app.secret_key = "secret_key_123"

# 擬似トレンド生成（売れる系）
def get_trends():

    base = [
        "WBC", "地震", "花粉", "新生活", "入学", "卒業",
        "ダイエット", "筋トレ", "美容", "節約",
        "防災", "キャンプ", "旅行", "桜"
    ]

    sub = [
        "グッズ", "アイテム", "おすすめ", "人気",
        "便利", "最新", "2026", "ランキング"
    ]

    trends = []

    for _ in range(5):
        trend = random.choice(base) + " " + random.choice(sub)
        trends.append(trend)

    return trends

@app.route("/", methods=["GET", "POST"])
def home():

    ideas = []

    if request.method == "POST":

        trends = get_trends()

        for trend in trends:

            idea = "関連グッズ"
            mercari_kw = trend
            amazon_kw = trend
            m_price = random.randint(1500, 3000)
            a_price = m_price + random.randint(800, 2000)
            profit = a_price - m_price

            post = f"""今トレンドの「{trend}」🔥

実はこれ、物販チャンスです。

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)