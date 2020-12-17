# ライブラリの読み込み
import ssl
from slackbot.bot import Bot

def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    # https://qiita.com/shutokawabata0723/items/9733a7e640a175c23f39

    # ボットの起動
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    main()
