from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)
app.secret_key = "secret_key_123"

# --- トレンド生成（売れる＋具体ワード） ---
def get_trends():

    base = [
        "大谷翔平", "鬼滅の刃", "呪術廻戦", "ワンピース",
        "ポケモンカード", "ちいかわ", "PS5",
        "ニンテンドースイッチ", "スタバ新作",
        "ユニクロ新作", "無印良品",
        "地震 防災", "花粉症", "キャンプ", "旅行"
    ]

    sub = [
        "グッズ", "限定", "コラボ", "最新",
        "人気", "レア", "再販"
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
            a_price = m_price + random.randint(1000, 2500)
            profit = a_price - m_price

            post = f"""【これ狙い目です】

今トレンドの「{trend}」🔥

・仕入れ：約{m_price}円
・販売：約{a_price}円
・利益：+{profit}円

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