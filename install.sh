#!/bin/bash

# 仮想環境の作成
python -m venv myenv

# 仮想環境のアクティベート
source myenv/bin/activate

# 必要なパッケージのインストール
pip install -r requirements.txt

echo "仮想環境の設定とパッケージのインストールが完了しました。"
