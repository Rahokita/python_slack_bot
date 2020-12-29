from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import slackbot_settings


# メンションあり応答
@respond_to('こんにちは')
def greeting01(message):
    # メンションして応答
    message.reply('こんにちは!!')

@respond_to('役立たず')
def greeting02(message):
    # メンションして応答
    message.send('...')

# メンションなし応答
@listen_to('今日は何曜日？')
def greeting03(message):

    # メンションなしで応答
    message.reply('自分で調べましょう')

@listen_to('もうかりまっか')
def greeting04(message):

    # メンションなしで応答
    message.send('ぼちぼちでんな')


@default_reply
def my_default_handler(message):
    # デフォルトリプライをsendに変更する
    message.send(slackbot_settings.DEFAULT_REPLY)
