# 人口無脳 Unmo　discord bot ver.

`Unmo`はPythonで書かれたチャットボットです。形態素解析・マルコフ連鎖などに基づいたアルゴリズムにより、ユーザーの入力を学習・成長していきます。人口無脳とも呼ばれます。

もともとはRuby向けの書籍「[恋するプログラム][book]」で解説されているチャットボットであり、このリポジトリは勉強を兼ねてPythonに移植したものをdiscordで使えるようにしました。

## 必要なもの

[Python3][python3]が必要です。Python2系では動作しません。依存パッケージはインストール時に自動的にインストールされます。

## インストール

`git`による`clone`か、またはパッケージを[ダウンロード][releases]して展開してください。その後`setup.py`を実行します。

    git clone https://github.com/lovetwice1012/unmo2.git
    cd unmo2/
    python setup.py install
    export DISCORD_BOT_TOKEN=<discordのbotのトークン>

## 起動

`python -m unmo`とタイプすることで、ディスコードのボットがオンラインになります。まずは「こんにちは」など話しかけてみてください。

はじめはユーザーの発言を繰り返すだけですが、学習して辞書が充実してくると自分で文章を考え始めます。辛抱強く話しかけてあげてください。

## 謝辞

- [恋するプログラム][book]の著者、秋山 智俊さん

## 変更履歴
- 0.2.3
  - 辞書ファイルの保存先を固定しました。これに伴い、これまでの辞書は読み込めなくなります。
    - Mac, Unix系では`$HOME/.unmo/dics/`ディレクトリ
    - Windowsでは`C:\Users\username\.unmo\dics\`フォルダ
- 0.2.2
  - 辞書が保存できない場合があるバグを修正しました。
  - テストコードをリファクタリングしました。

[releases]: https://github.com/lovetwice1012/unmo2/releases
[book]: http://amzn.to/2kYltNz
[python3]: https://www.python.org/downloads/
