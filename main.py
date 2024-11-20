from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load models
lr_model = pickle.load(open('content/models/linear_regression_model.pkl', 'rb'))
nb_model = pickle.load(open('content/models/naive_bayes_model.pkl', 'rb'))
knn_model = pickle.load(open('content/models/knn_model.pkl', 'rb'))
svm_model = pickle.load(open('content/models/svm_model.pkl', 'rb'))
dt_model = pickle.load(open('content/models/decision_tree_model.pkl', 'rb'))
ann_model = pickle.load(open('content/models/ann_model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/linear_regression', methods=['GET', 'POST'])
def linear_regression():
    if request.method == 'POST':
        likes = float(request.form['likes'])
        predicted_followers = lr_model.predict([[likes]])[0]
        return render_template('algos/linear_regression.html', result=predicted_followers)
    return render_template('algos/linear_regression.html')

@app.route('/naive_bayes', methods=['GET', 'POST'])
def naive_bayes():
    if request.method == 'POST':
        caption = request.form['caption']
        sentiment = nb_model.predict([caption])
        return render_template('algos/naive_bayes.html', result=sentiment)
    return render_template('algos/naive_bayes.html')

# Add similar endpoints for KNN, SVM, Decision Tree, and ANN.

if __name__ == '__main__':
    app.run(debug=True)
