from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "secret_key_123"

USER_ID = "admin"
PASSWORD = "1234"

@app.route("/", methods=["GET", "POST"])
def home():

    if "logged_in" not in session and session.get("used"):
        return redirect(url_for("login"))

    ideas = []

    if request.method == "POST":

        if "logged_in" not in session:
            session["used"] = True

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


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["user"]
        pw = request.form["pw"]

        if user == USER_ID and pw == PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("home"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)