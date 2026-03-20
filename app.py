from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)
app.secret_key = "secret_key_123"

def get_trends():

    trends_pool = [
        "大谷翔平", "WBC 日本代表", "鬼滅の刃",
        "呪術廻戦", "ワンピース", "ポケモンカード",
        "ちいかわ", "スターバックス 新作",
        "ユニクロ 新作", "無印良品 人気商品",
        "ニンテンドースイッチ", "PS5",
        "東京ディズニーランド", "USJ",
        "地震 防災グッズ", "花粉症対策グッズ",
        "キャンプ用品", "車中泊グッズ"
    ]

    return random.sample(trends_pool, 5)

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)