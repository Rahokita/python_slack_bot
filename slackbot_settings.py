# ライブラリのインポート
import os

# 環境変数に定義しておく
API_TOKEN = os.environ['HUBOT_SLACK_TOKEN']

# デフォルトの応答
DEFAULT_REPLY = "すみません。よくわかりません"

PLUGINS = [
            'slackbot.plugins',
            'botmodules.conversation',
            # ここにカンマ区切りでプラグインを追加していくことで拡張できます。
]
