# Title

Temperature Prediction with XGBoost

## Description
This project uses machine learning, specifically XGBoost, to predict temperatures based on planetary degrees and historical temperature data. The model is trained on historical data and can make predictions for future dates. The project also includes a simple frontend for user interaction and a pickle file containing the trained model.

## Installation

Clone this repository:

```
git clone https://github.com/anket16/forecasting-model.git
cd ./forecasting-model/
```

Install scikit-learn==1.3.2 and other dependencies
```bash
pip install scikit-learn==1.3.2
pip install -r requirements.txt

```

## Usage

Run the app.py file:
```python
python app.py
```
Open your browser with localhost.
select the specific date and planets degree corresponding to it. Click on predict to get Temp(max)

## Data

The dataset contains day-wise planetary degrees and temperature information.
Historical data is used to train the XGBoost model, and future dates can be predicted.

## Files

app.py: Main file for running the Flask web application.
requirements.txt: List of Python packages required for the project.
model.pkl: Pickle file containing the trained XGBoost model.
templates/index.html:Html file for frontend of application
