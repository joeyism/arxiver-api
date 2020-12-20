from flask import Flask, jsonify
from flask_cors import CORS
import arxiv

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Arxiver API"

@app.route('/<arxiv_num>')
def arxiv_num(arxiv_num):
    results = arxiv.query(id_list=[arxiv_num])[0]
    return jsonify(results)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)
