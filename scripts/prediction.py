import requests
import pandas as pd
import joblib
from pathlib import Path
from datetime import datetime


#load the dumped model
model_path = Path("models/rf_classifier.pkl").resolve()
model = joblib.load(model_path)

#fetch penguin data from API
api_url = "http://130.225.39.127:8000/new_penguin/"
penguin_data = requests.get(api_url).json()

#extract timestamp
spotted_time = penguin_data.pop('datetime', 'N/A')

#DataFrame preparation for prediction
features = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
df_new = pd.DataFrame([{k: penguin_data[k] for k in features}])

prediction = model.predict(df_new)[0]

#prediction markdown
prediction_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
prediction_text = f"""
###Penguin Spotted Prediction:

- **Penguin Spotted At:** {spotted_time}
- **Time of Prediction:** {prediction_time}
- **Predicted Species:** {prediction}
- **Penguin Features Used:** {penguin_data}
"""

#save the prediction
output=Path("predictions/latest_prediction.md").resolve()
with open(output, "w", encoding='utf-8') as f:
    f.write(prediction_text)

print(f"\nPrediction saved to {output}")
