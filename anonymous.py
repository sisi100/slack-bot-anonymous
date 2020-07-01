import json
import os
import urllib.request

from setting import USER_ACCESS_TOKEN


def post_message(message: str) -> None:
    if not message:
        # Slackでファイル添付のみだと、本文なしを送信されることがあるため
        return

    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": f"Bearer {USER_ACCESS_TOKEN}",
    }
    data = {
        "channel": os.environ["SLACK_CHANNEL"],
        "username": os.environ["SLACK_USER_NAME"],
        "icon_emoji": os.environ["SLACK_ICON"],
        "attachments": [{"text": message}],
    }
    req = urllib.request.Request(
        url, data=json.dumps(data).encode("utf-8"), method="POST", headers=headers
    )
    urllib.request.urlopen(req)


def handler(event: dict, context: dict) -> dict:
    result = ""
    body = json.loads(event["body"])
    # SlackAPIからのログ。不祥事発生時のログ確認用途
    # 変数bodyから取得しないのは、event['body']のがJSON形式文字列でログが見やすいため。
    print(event["body"])

    if "event" in body:
        pyload = body["event"]
        post_message(pyload["text"],)
        if "files" in pyload:
            for file in pyload["files"]:
                # 添付ファイルがあった場合は、そのリンクを飛ばす仕様:
                # サムネイルをつけようと、多少やったがハマったので諦めた。
                post_message(file["permalink"])

    # 初回認証時の処理:
    # 初回以降不要だがエンドポイント変更時にいちいち認証のためコードを
    # 改変するのは面倒なので、記述
    if "challenge" in body:
        result = body["challenge"]

    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "https://api.slack.com"},
        "body": result,
    }
