from flask import Flask, render_template, request
import os
import func
import traceback

app = Flask(__name__)



# メイン関数
@app.route('/', methods=['GET'])
def index():
    try:
        # パラメータ変数格納
        word = request.args.get('word') # アクセストークン

        # スクレイピング実行
        return func.get_ad_url(word)

    # エラー時
    except:
        return traceback.format_exc()



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))