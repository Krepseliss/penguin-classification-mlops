# Penguin Classification - MLOps Assignment

## Project Overview
This project builds a machine learning pipeline to classify penguin species based on physical measurements. The project also includes an automated system that fetches new penguin data daily from an API, makes predictions, and updates the results.

## Technologies Used
- Python 3.11
- Pandas
- Scikit-learn
- Seaborn
- SQLite (via SQLAlchemy)
- Joblib
- GitHub Actions for automation

## Workflow Description
- **Data Preparation:** 
  - Load penguin dataset
  - Normalize the database into `ISLANDS` and `PENGUINS` tables
- **Model Training:** 
  - Train a Random Forest Classifier to predict species
  - Save the trained model
- **Prediction Script:** 
  - Fetch new penguin data from the API
  - Predict the species
  - Save the result into `predictions/latest_prediction.md`
- **Automation:** 
  - A GitHub Action runs daily
  - It fetches new data, predicts, and updates the prediction file

## Automated Prediction
- The GitHub Action runs daily at 7:30 AM CET
- It fetches new penguin data, predicts, and updates `latest_prediction.md`

## Output
The latest prediction can be found in:
"predictions/latest_prediction.md"

It includes:
- Timestamp when the penguin was spotted
- Prediction timestamp
- Predicted species
- Penguin features used for prediction
