# Auto Clicker for Idle Tasks

このツールは、さまざまなゲームでの放置作業をさらに**つまらなく**、**暇にする**シンプルで簡単なGUIツールです。PyAutoGUIとTkinterを使用して、マウスやキーボードの操作をシミュレートし、特定のキーやボタンの設定や押下間隔の調整が可能です。

## 特徴

- **シンプルな操作**: 直感的なGUIで簡単に設定可能。
- **多用途**: 様々なゲームでの放置作業に対応。
- **カスタマイズ可能**: 押下・離脱間隔やキー、ボタンを自由に設定。
- **緊急停止機能**: Ctrl + Shift + Sで自動クリックを瞬時に停止。

## 使用方法

### 仮想環境の設定とパッケージのインストール

1. 仮想環境の作成、アクティベート、および必要なパッケージのインストールを行うスクリプトがあります。
    - Windows:
        ```bash
        install.bat
        ```
    - macOS/Linux:
        ```bash
        ./install.sh
        ```

### ツールの実行

1. `AutoClicker.py`を実行するためのスクリプトがあります。
    - Windows:
        ```bash
        start.bat
        ```
    - macOS/Linux:
        ```bash
        ./start.sh
        ```

2. GUIで設定を行い、「Start」ボタンをクリックして自動クリックを開始。
3. 自動クリックを停止するには、Ctrl + Shift + Sを押すか、GUI上の「Stop」ボタンをクリック。

## 必要なパッケージ

以下のパッケージが必要です。プロジェクトディレクトリ内で`pipreqs`を使用して`requirements.txt`を生成しました。

- PyAutoGUI
- Tkinter
- Keyboard

## 注意事項

このツールは自己責任で使用してください。ゲームの利用規約を遵守し、適切に使用してください。

---

作成者: [あなたの名前]
