from flask import Flask, request, abort
from simplenote import Simplenote
import json

username = ''
password = ''

with open('config.json') as data_file:
    data = json.load(data_file)
    username = data['username']
    password = data['password']


app = Flask(__name__)


@app.route('/', methods=['POST'])
def post():
    s = Simplenote(username, password)
    (notes, result) = s.get_note_list(tags=['bookmarks'])
    if result == 0:  # sucess
        bookmarknote = notes[0]

        (note, result) = s.get_note(bookmarknote['key'])
        content = note['content']

        content = '%s\n\n%s' % (content, request.data)
        bookmarknote['content'] = content
        bookmarknote['tags'] = ['bookmarks']

        s.update_note(bookmarknote)
        return 'OK'
    abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
