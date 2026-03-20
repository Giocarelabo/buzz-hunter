from flask import Flask, render_template, request
from pytrends.request import TrendReq
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)
app.secret_key = "secret_key_123"

# --- Googleトレンド ---
def get_google_trends():
    try:
        pytrends = TrendReq(hl='ja-JP', tz=540)
        df = pytrends.trending_searches(pn='japan')

        if df.empty:
            return []

        return list(df[0][:5])

    except:
        return []

# --- Yahooリアルタイム（Xトレンド代替） ---
def get_yahoo_trends():
    try:
        url = "https://search.yahoo.co.jp/realtime"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        res = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")

        trends = []
        for item in soup.select("span.sw-Card__titleInner")[:5]:
            trends.append(item.text.strip())

        return trends

    except:
        return []

# --- トレンド統合（安定版） ---
def get_trends():

    trends = []

    # Google
    trends += get_google_trends()

    # Yahoo
    trends += get_yahoo_trends()

    # 重複削除
    trends = list(set(trends))

    # それでも空なら保険
    if not trends:
        trends = ["人気商品", "話題グッズ", "注目アイテム"]

    return trends[:5]

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