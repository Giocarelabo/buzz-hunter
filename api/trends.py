import json
import random

def handler(request):
    try:
        trends = [
            "大谷翔平 グッズ",
            "ポケモンカード 151",
            "PS5 コントローラー",
            "無印良品 収納ケース",
            "ナイキ エアフォース1",
            "スターバックス タンブラー",
            "ユニクロ エアリズム",
            "iPhone15 ケース",
            "ワンピース フィギュア",
            "任天堂スイッチ 本体"
        ]

        results = []

        for t in trends:
            m_price = random.randint(1000, 5000)
            a_price = m_price + random.randint(1000, 4000)

            results.append({
                "trend": t,
                "m_price": m_price,
                "a_price": a_price,
                "profit": a_price - m_price
            })

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(results)  # ←これ超重要
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }