from flask import Flask, render_template, request
from pytrends.request import TrendReq
import os

app = Flask(__name__)
app.secret_key = "secret_key_123"

def get_trends():
    try:
        pytrends = TrendReq(hl='ja-JP', tz=540)
        trends = pytrends.trending_searches(pn='japan')[0:5]
        return list(trends)
    except:
        # 失敗時の保険
        return ["話題の商品", "人気アイテム", "トレンドグッズ"]

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