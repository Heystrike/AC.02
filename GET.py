from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/books', methods=["GET"])
def consultar():
    return 'primeira chamada de api!'

if __name__ == '__main__':
    app.run()