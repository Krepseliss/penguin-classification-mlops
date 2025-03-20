import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

#Connect to the database
db_path=Path(r"C:\Users\alex\Data Engineering\penguin-classification-mlops\data\penguins_db.sqlite").resolve()
engine=create_engine(r'sqlite:///C:\Users\alex\Data Engineering\penguin-classification-mlops\data\penguins_db.sqlite')

#SQL JOIN to merge PENGUINS and ISLANDS / extracting island names
query="""
SELECT PENGUINS.*, ISLANDS.name AS island_name
FROM PENGUINS
JOIN ISLANDS ON PENGUINS.island_id = ISLANDS.island_id
"""
df=pd.read_sql(query, con=engine)

features = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
target = 'species'

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#train RandomForest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

#Predict and evaluate
y_pred = model.predict(X_test)
print("✅ Model Evaluation:")
print(classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save the trained model
model_path = Path(r"C:\Users\alex\Data Engineering\penguin-classification-mlops\models\rf_classifier.pkl").resolve()
joblib.dump(model, model_path)

print("\nSuccess!")
