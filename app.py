from flask import Flask, render_template, request, session, redirect, url_for, send_from_directory
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)
app.secret_key = "secret_key_123"

USER_ID = "buyer"
PASSWORD = "buzz123"

@app.route("/", methods=["GET", "POST"])
def home():

    if "logged_in" not in session and session.get("used"):
        return redirect(url_for("login"))

    ideas = []

    if request.method == "POST":

        if "logged_in" not in session:
            session["used"] = True

        url = "https://trends.google.com/trending/rss?geo=JP"
        response = requests.get(url)
        root = ET.fromstring(response.content)

        trends = []

        for item in root.iter("item"):
            title = item.find("title").text
            trends.append(title)
            if len(trends) >= 5:
                break

        for trend in trends:

            if "地震" in trend:
                idea = "防災グッズ"
                mercari_kw = "防災グッズ"
                amazon_kw = "防災グッズ"
                m_price = 2500
                a_price = 3800

            elif "野球" in trend or "WBC" in trend:
                idea = "野球グッズ"
                mercari_kw = "野球 グッズ"
                amazon_kw = "野球 グッズ"
                m_price = 3000
                a_price = 4500

            else:
                idea = "トレンドグッズ"
                mercari_kw = trend + " グッズ"
                amazon_kw = trend + " グッズ"
                m_price = 2800
                a_price = 4200

            profit = a_price - m_price

            post = f"""【今バズってる】{trend}🔥

これ、せどりチャンスです。

✔ メルカリ仕入れ目安：{m_price}円
✔ Amazon販売目安：{a_price}円
✔ 想定利益：+{profit}円

今はトレンドに乗るだけで売れる可能性あり。

#せどり #副業"""

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
            return redirect("/")

    return render_template("login.html")


# PWA用
@app.route('/manifest.json')
def manifest():
    return send_from_directory('.', 'manifest.json')

@app.route('/service-worker.js')
def sw():
    return send_from_directory('.', 'service-worker.js')


if __name__ == "__main__":
    app.run(debug=True)