🏥 Health Insurance Plan Predictor
Use this interactive tool to estimate your health insurance premium based on your personal, lifestyle, and financial details. This ML-powered app helps users make informed decisions about their insurance needs.

🔗 Live Demo Try the app live: 
👉 https://my-health-insurance-cost-predictor.streamlit.app/

📌 Project Highlights


🎯 Goal: Predict suitable insurance premium based on user profile

🧠 Model Type: Regression using LinearRegression

🧪 Toolkit: Python, Scikit-Learn, Pandas, Streamlit, Joblib

🌐 Frontend: Streamlit-based intuitive UI

📊 Key Features:

Personal details (age, gender, region, marital status)

Lifestyle choices (BMI, smoking, employment, diseases)

Financial data (income, dependents, insurance plan level)

Genetic risk factor slider

💡 Dual-Model Strategy for Age Segmentation
I noticed that health insurance dynamics significantly differ between younger individuals and adults. To improve accuracy, I trained and deployed two separate models:

🔹 model_young → For users aged 25 or below

🔸 model_Rest → For users aged above 25

This segmentation allowed me to capture distinct patterns and tailor predictions more effectively for each age group. The Streamlit app auto-selects the appropriate model based on user input.


## 🧰 Tech Stack

| Component       | Tool/Library        |
|----------------|---------------------|
| ML Model       | scikit-learn        |
| App Framework  | Streamlit           |
| Serialization  | Joblib              |
| Data Handling  | Pandas, NumPy       |
| UI Styling     | Streamlit widgets   |

---


## 💡 Usage

### 🖥️ Run the App Locally

1. **Clone the repository**
   ```bash
      https://github.com/Krushang010/ML_health-insurance-cost-predictor.git

   
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt


3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py


📦 Model Development Summary
Cleaned and preprocessed user data

Created BMI categories and income brackets

Removed multicollinearity using VIF analysis

Trained separate models and scalers for two age segments

Saved artifacts using joblib under artifacts
