# Auto Clicker for Idle Tasks

このツールは、さまざまなゲームでの放置作業をさらに**つまらなく**、**暇にする**シンプルで簡単なGUIツールです。PyAutoGUIとTkinterを使用して、マウスやキーボードの操作をシミュレートし、特定のキーやボタンの設定や押下間隔の調整が可能です。

## 特徴

- **シンプルな操作**: 直感的なGUIで簡単に設定可能。
- **多用途**: 様々なゲームでの放置作業に対応。
- **カスタマイズ可能**: 押下・離脱間隔やキー、ボタンを自由に設定。
- **緊急停止機能**: Alt + ピリオド（.）+ Enterで自動クリックを瞬時に停止。

## 使用方法

### 仮想環境の設定

1. 仮想環境の作成
    ```bash
    python -m venv myenv
    ```

2. 仮想環境のアクティベート
    - Windows:
        ```bash
        .\myenv\Scripts\activate
        ```
    - macOS/Linux:
        ```bash
        source myenv/bin/activate
        ```

3. 必要なパッケージのインストール
    ```bash
    pip install -r requirements.txt
    ```

### ツールの実行

1. `AutoClicker.py`を実行
    ```bash
    python AutoClicker.py
    ```

2. GUIで設定を行い、「Start」ボタンをクリックして自動クリックを開始。
3. 自動クリックを停止するには、Alt + ピリオド（.）+ Enterを押すか、GUI上の「Stop」ボタンをクリック。

## 必要なパッケージ

以下のパッケージが必要です。プロジェクトディレクトリ内で`pipreqs`を使用して`requirements.txt`を生成しました。

- PyAutoGUI
- Tkinter

## 注意事項

このツールは自己責任で使用してください。ゲームの利用規約を遵守し、適切に使用してください。

---

作成者: [あなたの名前]
