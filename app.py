import pickle
import warnings
warnings.filterwarnings("ignore")

from flask import Flask, jsonify, request
from tokenizer import tokenize

app = Flask(__name__)
clf = None
vct = None

@app.route('/')
def load_model():
    global clf, vct

    clf = pickle.load(open('classifier.pkl', 'rb'))
    vct = pickle.load(open('vectoriser.pkl', 'rb'))

    return jsonify(status='model is loaded')


@app.route('/predict', methods=['POST'])
def predict():
    global clf, vct

    text = request.get_json()['text']
    text_preprocessed = tokenize(text)

    answer = clf.predict(vct.transform([text_preprocessed]))
    return jsonify(answer=str(answer))

if __name__ == '__main__':
    app.run(debug=True)