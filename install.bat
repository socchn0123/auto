@echo off

:: 仮想環境の作成
python -m venv myenv

:: 仮想環境のアクティベート
call myenv\Scripts\activate

:: 必要なパッケージのインストール
pip install -r requirements.txt

echo 仮想環境の設定とパッケージのインストールが完了しました。
pause
