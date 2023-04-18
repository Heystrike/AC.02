from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'A Guerra dos Tronos',
        'author': 'George R. R. Martin'
    },
    {
        'id': 2,
        'title': 'O Senhor dos Anéis',
        'author': 'J. R. R. Tolkien'
    }
]

booksJSON = jsonify(books)

@app.route('/')
def home():
    return "API Funcionando!"

@app.route('/api/books', methods=['GET'])
def books():
    return booksJSON


if __name__ == '__main__':
    app.run()

