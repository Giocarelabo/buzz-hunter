from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)
app.secret_key = "secret_key_123"

def get_trends():

    trends = []

    anime = [
        "鬼滅の刃 グッズ", "呪術廻戦 フィギュア",
        "ワンピース カード", "ちいかわ グッズ"
    ]

    sports = [
        "大谷翔平 グッズ", "WBC ユニフォーム",
        "プロ野球 グッズ"
    ]

    brand = [
        "無印良品 収納", "ユニクロ 新作",
        "スタバ 新作"
    ]

    hobby = [
        "ポケモンカード レア", "PS5 本体",
        "ニンテンドースイッチ ソフト"
    ]

    life = [
        "防災グッズ", "花粉症対策グッズ",
        "キャンプ用品", "旅行グッズ"
    ]

    all_trends = anime + sports + brand + hobby + life

    return random.sample(all_trends, 5)


@app.route("/", methods=["GET", "POST"])
def home():

    ideas = []

    if request.method == "POST":

        trends = get_trends()

        for trend in trends:

            m_price = random.randint(1500, 3000)
            a_price = m_price + random.randint(1000, 2500)
            profit = a_price - m_price

            post = f"""【これ狙い目です】

{trend} 🔥

・仕入れ：約{m_price}円
・販売：約{a_price}円
・利益：+{profit}円

今のうちにチェックで利益につながる可能性あり💰

#副業 #せどり #物販"""

            ideas.append({
                "trend": trend,
                "post": post,
                "mercari_url": f"https://www.mercari.com/jp/search/?keyword={trend}",
                "amazon_url": f"https://www.amazon.co.jp/s?k={trend}",
                "m_price": m_price,
                "a_price": a_price,
                "profit": profit
            })

    return render_template("index.html", ideas=ideas)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)