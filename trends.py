from http.server import BaseHTTPRequestHandler
import json
import random

def get_trends():
    trends = [
        "鬼滅の刃 グッズ",
        "呪術廻戦 フィギュア",
        "ポケモンカード レア",
        "大谷翔平 グッズ",
        "無印良品 収納",
        "ユニクロ 新作",
        "スタバ 新作",
        "PS5 本体",
        "防災グッズ",
        "キャンプ用品"
    ]
    return random.sample(trends, 5)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        trends = get_trends()

        results = []
        for trend in trends:
            m_price = random.randint(1500, 3000)
            a_price = m_price + random.randint(1000, 2500)
            profit = a_price - m_price

            results.append({
                "trend": trend,
                "m_price": m_price,
                "a_price": a_price,
                "profit": profit
            })

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(results).encode())