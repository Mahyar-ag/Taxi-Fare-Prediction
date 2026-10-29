# NYC Taxi Fare Prediction 🚕

This project predicts taxi fares in New York City based on trip distance, passenger count, and location. It demonstrates a complete Data Science and Machine Learning pipeline, focusing heavily on cleaning dirty data and preventing data leakage.

## Key Skills & Techniques Demonstrated
- **Data Imputation:** Handled missing values (Nulls) using mode and constant replacement.
- **Categorical Encoding:** Converted text data (e.g., payment methods, boroughs) into numerical format using One-Hot Encoding.
- **Feature Scaling:** Applied `StandardScaler` to normalize continuous variables (distance, passengers) for better model performance.
- **Data Leakage Prevention:** Removed post-trip features (like tips and total amount) before training to simulate real-world prediction.
- **Exploratory Data Analysis (EDA):** Generated full correlation heatmaps using Seaborn.

## Model Performance
- **Algorithm:** Random Forest Regressor
- **R-squared (R2) Score:** 0.90 (Explains 90% of the variance in fares)
- **Mean Absolute Error (MAE):** $1.84
