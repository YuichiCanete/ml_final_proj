from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/linear-regression')
def linear_regression():
    return render_template('linear-regression.html')

@app.route('/naive-bayes')
def naive_bayes():
    return render_template('naive-bayes.html')

@app.route('/knn')
def knn():
    return render_template('knn.html')

@app.route('/svm')
def svm():
    return render_template('svm.html')

@app.route('/decision-tree')
def decision_tree():
    return render_template('decision-tree.html')

@app.route('/neural-network')
def neural_network():
    return render_template('neural-network.html')

if __name__ == '__main__':
    app.run(debug=True)
