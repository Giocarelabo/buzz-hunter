export default async function handler(req, res) {

  const items = [
    "ワイヤレスイヤホン",
    "ゲーミングマウス",
    "モバイルバッテリー",
    "スマートウォッチ",
    "ネッククーラー",
    "電動歯ブラシ",
    "小型プロジェクター",
    "Bluetoothスピーカー",
    "タブレットスタンド",
    "LEDリングライト",
    "ノイズキャンセリングイヤホン",
    "充電式ハンディファン"
  ];

  // シャッフル
  const shuffled = items.sort(() => 0.5 - Math.random()).slice(0,5);

  const data = shuffled.map(name => {

    const m = Math.floor(Math.random() * 3000) + 1500; // 1500〜4500
    const a = m + Math.floor(Math.random() * 5000) + 2000; // 上乗せ
    const profit = a - m;

    return {
      trend: name,
      m_price: m,
      a_price: a,
      profit: profit
    };
  });

  res.status(200).json(data);
}