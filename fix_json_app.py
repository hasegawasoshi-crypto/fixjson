#uv run python fix_json_app.py

from flask import Flask, render_template, request
import json
import re

app = Flask(__name__)


def fix_bad_escapes_in_json(json_str: str) -> str:
    """JSON文字列内の不正なエスケープを修正する"""
    def escape_match(m):
        s = m.group(0)
        fixed = re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', s)
        return fixed

    return re.sub(r'\"(\\.|[^"\\])*\"', escape_match, json_str)


def remove_cite_start(json_str: str) -> str:
    """[cite_start]削除"""
    return json_str.replace("[cite_start]", "")


def fix_json_text(text: str) -> str:
    """入力テキストに処理をかけて整形済みJSONテキストを返す"""
    fixed = remove_cite_start(text)
    fixed = fix_bad_escapes_in_json(fixed)

    # JSONチェック
    try:
        parsed = json.loads(fixed)
        # 整形して返す
        return json.dumps(parsed, ensure_ascii=False, indent=2)
    except json.JSONDecodeError as e:
        return f"JSONエラー: {e}"


@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        input_text = request.form.get("input_text", "")
        result = fix_json_text(input_text)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
