from flask import Flask, render_template, request
import sys
import pickle
sys.path.append('/f/FOLDER-D/Anket/vasuki ai')

print(sys.path)
app = Flask(__name__)

with open('random_forest_model.pkl', 'rb') as file:
    rf_model = pickle.load(file)

def predict(input_date,planets_degree):
    user_input_array = [[331.087222	,339.494722,	43.148056	,304.988611,	328.040278]]
    predictions = rf_model.predict(planets_degree)
    predictions = round(predictions[0],2)
    print(predictions)
    prediction_result = f"Maximum temmperature on {input_date}: {predictions}"
    return prediction_result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_temp', methods=['POST'])
def predict_temp():
    date = request.form['inputDate']
    sun_degree =  float(request.form['sun_degree'])  if request.form['sun_degree'].strip().replace(".", "").isdigit() else 0
    moon_degree = float(request.form['moon_degree'])  if request.form['moon_degree'].strip().replace(".", "").isdigit() else 0
    mars_degree = float(request.form['mars_degree'])  if request.form['mars_degree'].strip().replace(".", "").isdigit() else 0
    mercury_degree = float(request.form['mercury_degree'])  if request.form['mercury_degree'].strip().replace(".", "").isdigit() else 0
    venus_degree = float(request.form['venus_degree']) if request.form['venus_degree'].strip().replace(".", "").isdigit() else 0
    
    print(type(request.form['mercury_degree']) )
    degree_list = [[sun_degree,moon_degree,mars_degree,mercury_degree,venus_degree]]
    print(degree_list)
    prediction_result = predict(date,degree_list)
    return render_template('index.html', prediction_result=prediction_result)

if __name__ == '__main__':
    app.run(debug=True)
