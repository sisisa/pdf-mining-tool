# PDFテキストマイニングツール

## 概要
PDFファイルからテキストを抽出し、テキストマイニング（頻出語解析・TF-IDF分析）を自動実行するPythonツールです。

新聞・論文・議事録・レポート・契約書など、あらゆるPDFに対応した **汎用テキスト解析エンジン** として設計しています。

OSに依存せず、Google Colab上でも実行可能です。

---

## 主な機能

- PDF → テキスト抽出
- 日本語形態素解析（Janome）
- 頻出単語カウント
- TF-IDF分析
- CSV出力
- Excel出力
- Google Colab対応（環境構築不要）

---

## ディレクトリ構成

```text
pdf-mining-tool/
│
├─ input_pdf/ # 解析対象PDFを格納
├─ output/ # 出力結果
│
├─ src/
│ ├─ extractor.py # PDF → text抽出
│ ├─ preprocess.py # 前処理
│ ├─ tokenizer.py # 形態素解析
│ ├─ mining.py # テキストマイニング処理
│ ├─ exporter.py # CSV/Excel出力
│ └─ main.py # 実行エントリーポイント
│
├─ requirements.txt
├─ README.md
```

---

## 使用技術

- Python 3
- pdfplumber（PDF抽出）
- Janome（日本語形態素解析）
- pandas（データ処理）
- scikit-learn（TF-IDF）
- openpyxl（Excel出力）

---

# 実行方法

### ① ライブラリインストール
```text
pip install -r requirements.txt
```
---

### ②PDFを配置
```text
input_pdf/
```

フォルダに解析したいPDFを入れる

---

### ③ 実行
```text
python src/main.py
```

---

### ④ 出力結果
```text
output/result_freq.csv
output/result_freq.xlsx
output/result_tfidf.csv
output/result_tfidf.xlsx
```
---
# Google Colabで実行（推奨）

環境構築不要。GoogleアカウントのみでOK。

## 手順

### ① Colabを開く
https://colab.research.google.com/

### ② GitHubから読み込み
「GitHub」タブ → このリポジトリURLを入力

または以下セルを順番に実行

---

### セル① ライブラリインストール
```python
!pip install pdfplumber pandas openpyxl scikit-learn janome
```

### セル② GitHubクローン
```python
!git clone https://github.com/sisisa/pdf-mining-tool.git
%cd pdf-mining-tool
```

### セル③ PDFアップロード
```python
from google.colab import files
files.upload()
```

アップロード後、input_pdf/ に移動

### セル④ 実行
```python
!python src/main.py
```

### セル⑤ ダウンロード
```python
files.download("output/result_freq.xlsx")
```
