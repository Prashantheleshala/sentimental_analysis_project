from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']
        if not review:
            message = "Please enter the review."
            return render_template('home.html', message=message)
        else:
            model = joblib.load("model/naive_bayes.pkl")
            prediction = model.predict([review])[0]
            return render_template('output.html', prediction=prediction)
    else:
        return render_template('home.html')
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")