from flask import Flask, render_template, request
from sklearn.naive_bayes import MultinomialNB
import pickle

app = Flask(__name__)

model = pickle.load(open('nlp_model.pkl', 'rb'))

vectorizer = pickle.load(open('tfidf.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        v1 = request.form.get('inp1')
        v2 = request.form.get('inp2')

        vector = vectorizer.transform([v1, v2])

        result = model.predict(vector)[0]
        res = ''
        if result == 0:
            res = 'HAM'
        elif result == 1:
            res = 'SPAM'
        else:
            res = 'UNKNOWN'
    return render_template('result.html', res=res, msg = v2, name = v1)

# if __name__ == '__main__':
#     app.run(debug=True)