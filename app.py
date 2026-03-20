from flask import Flask, render_template, request, session, redirect, url_for, send_from_directory
import os

app = Flask(__name__)
app.secret_key = "secret_key_123"

# --- PWA用 ---
@app.route('/manifest.json')
def manifest():
    return send_from_directory('.', 'manifest.json')

@app.route('/service-worker.js')
def sw():
    return send_from_directory('.', 'service-worker.js')

# --- メイン ---
@app.route("/", methods=["GET", "POST"])
def home():

    ideas = []

    if request.method == "POST":

        trends = ["暗殺教室", "WBC", "地震"]

        for trend in trends:

            if "地震" in trend:
                idea = "防災グッズ"
                mercari_kw = "防災グッズ"
                amazon_kw = "防災グッズ"
                m_price = 2500
                a_price = 3800

            elif "WBC" in trend:
                idea = "野球グッズ"
                mercari_kw = "野球 グッズ"
                amazon_kw = "野球 グッズ"
                m_price = 3000
                a_price = 4500

            else:
                idea = "アニメグッズ"
                mercari_kw = trend + " グッズ"
                amazon_kw = trend + " グッズ"
                m_price = 2800
                a_price = 4200

            profit = a_price - m_price

            post = f"""今トレンドの「{trend}」🔥

実はこれ、物販チャンスです。

狙い目👇
・関連グッズ
・限定商品
・トレンド便乗

今のうちにチェックで利益につながる可能性あり💰

あなたなら何を仕入れますか？🤔

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

# --- 起動設定（Render対応） ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)