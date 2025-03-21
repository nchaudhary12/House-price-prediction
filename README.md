# House-price-prediction      <br>
🏡 House Price Prediction API    <br>
📢 A Machine Learning model to predict house prices based on key features. <br>
🚀 Built using: FastAPI, Scikit-Learn, Random Forest, and Docker. <br>


📌 Project Overview <br>
This project uses Machine Learning to predict house prices based on various features such as square footage, number of rooms, and quality scores. <br>
It includes: <br>
✅ Data Preprocessing & Feature Engineering <br>
✅ Multiple Model Training & Optimization <br>
✅ FastAPI Deployment for real-time predictions <br>
✅ Containerization with Docker (optional) <br>
✅ Deployment on Render/AWS/GCP (optional) <br>

🚀 Getting Started <br>
1️⃣ Clone the Repository <br>

git clone https://github.com/nchaudhary12/house-price-prediction.git <br>
cd house-price-prediction <br>
2️⃣ Create a Virtual Environment & Install Dependencies <br>

python -m venv venv <br>
venv\Scripts\activate     # For Windows<br>

pip install -r requirements.txt<br>

3️⃣ Run FastAPI Locally<br>
uvicorn app:app --host 127.0.0.1 --port 8000 --reload<br>

4️⃣ Test API Using Postman or Swagger UI<br>
Open Swagger UI: http://127.0.0.1:8000/docs<br>
Or use Postman to send a POST request to:<br>
http://127.0.0.1:8000/predict<br>

📌 Example JSON Input:<br>

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
<br>
✅ Example Response:<br>
{
  "predicted_price": 312239.69
}<br>

📊 Model Training & Evaluation<br>
1️⃣ Data Cleaning & Preprocessing<br>
2️⃣ Feature Engineering (Scaling, Encoding, Feature Selection)<br>
3️⃣ Trained models:<br>

✅ Linear Regression<br>
✅ Decision Tree<br>
✅ Random Forest (Best Model)<br>
✅ XGBoost 4️⃣ Hyperparameter Tuning with GridSearchCV 5️⃣ Model Evaluation (RMSE, MAE, R² Score)<br>
🔹 Final Model: RandomForestRegressor<br>
🔹 Best Hyperparameters: n_estimators=300, max_depth=15<br>
🔹 Evaluation Metrics:<br>

MAE = 18,826<br>
MSE = 880,962,731<br>
RMSE = 29,681<br>
R² Score = 0.8851<br>
🎯 Future Enhancements<br>
✅ Deploy API on AWS/GCP/Render<br>
✅ Implement Model Versioning (MLflow/DVC)<br>
✅ Add Frontend UI for user interaction<br>
✅ Improve Model Performance with Feature Engineering<br>

🤝 Contributing<br>
🔹 Fork the repository<br>
🔹 Create a new branch: git checkout -b feature-branch<br>
🔹 Commit changes: git commit -m "Your message"<br>
🔹 Push to GitHub: git push origin feature-branch<br>
🔹 Create a Pull Request<br>

📜 License<br>
This project is open-source and available under the MIT License.<br>

📞 Contact<br>
👩‍💻 Developer: Nishi Chaudhary<br>
📧 Email: nishichaudhary2001@gmail.com<br>
🌐 GitHub: nchaudhary12<br>
