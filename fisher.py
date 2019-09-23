from flask import Flask, make_response
from helper import is_isbn_or_key
from yushu_book import YuShuBook
import json

app = Flask(__name__)
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    print(result)
    return json.dumps(result), 200, {'content-type': 'application/json'}


if __name__ == "__main__":
    app.run(
        debug=app.config['DEBUG']
    )
