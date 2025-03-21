# House-price-prediction
🏡 House Price Prediction API
📢 A Machine Learning model to predict house prices based on key features.
🚀 Built using: FastAPI, Scikit-Learn, Random Forest, and Docker.


📌 Project Overview
This project uses Machine Learning to predict house prices based on various features such as square footage, number of rooms, and quality scores.
It includes:
✅ Data Preprocessing & Feature Engineering
✅ Multiple Model Training & Optimization
✅ FastAPI Deployment for real-time predictions
✅ Containerization with Docker (optional)
✅ Deployment on Render/AWS/GCP (optional)

🚀 Getting Started
1️⃣ Clone the Repository

git clone https://github.com/nchaudhary12/house-price-prediction.git
cd house-price-prediction
2️⃣ Create a Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
3️⃣ Run FastAPI Locally

uvicorn app:app --host 127.0.0.1 --port 8000 --reload
4️⃣ Test API Using Postman or Swagger UI
Open Swagger UI: http://127.0.0.1:8000/docs
Or use Postman to send a POST request to:
http://127.0.0.1:8000/predict

📌 Example JSON Input:
json
Copy
Edit
{
  "OverallQual": 7,
  "GrLivArea": 2000,
  "ExterQual": 3,
  "KitchenQual": 3,
  "GarageCars": 2,
  "GarageArea": 400,
  "TotalBsmtSF": 1000,
  "1stFlrSF": 1200,
  "BsmtQual": 3
}
✅ Example Response:
{
  "predicted_price": 312239.69
}

📊 Model Training & Evaluation
1️⃣ Data Cleaning & Preprocessing
2️⃣ Feature Engineering (Scaling, Encoding, Feature Selection)
3️⃣ Trained models:

✅ Linear Regression
✅ Decision Tree
✅ Random Forest (Best Model)
✅ XGBoost 4️⃣ Hyperparameter Tuning with GridSearchCV 5️⃣ Model Evaluation (RMSE, MAE, R² Score)
🔹 Final Model: RandomForestRegressor
🔹 Best Hyperparameters: n_estimators=300, max_depth=15
🔹 Evaluation Metrics:

MAE = 18,826
MSE = 880,962,731
RMSE = 29,681
R² Score = 0.8851
🎯 Future Enhancements
✅ Deploy API on AWS/GCP/Render
✅ Implement Model Versioning (MLflow/DVC)
✅ Add Frontend UI for user interaction
✅ Improve Model Performance with Feature Engineering

🤝 Contributing
🔹 Fork the repository
🔹 Create a new branch: git checkout -b feature-branch
🔹 Commit changes: git commit -m "Your message"
🔹 Push to GitHub: git push origin feature-branch
🔹 Create a Pull Request

📜 License
This project is open-source and available under the MIT License.

📞 Contact
👩‍💻 Developer: Nishi Chaudhary
📧 Email: nchaudhary@example.com
🌐 GitHub: nchaudhary12
