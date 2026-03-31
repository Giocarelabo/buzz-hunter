export default function handler(req, res) {
  const trends = [
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
  ];

  const results = trends.map(t => {
    const m_price = Math.floor(Math.random() * 4000) + 1000;
    const a_price = m_price + Math.floor(Math.random() * 4000) + 1000;

    return {
      trend: t,
      m_price,
      a_price,
      profit: a_price - m_price
    };
  });

  res.status(200).json(results);
}