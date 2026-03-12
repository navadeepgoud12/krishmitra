# 🌾 KrishMitra – AI Powered Smart Crop Yield & Disease Prediction System

KrishMitra is an AI-based smart agriculture system designed to assist farmers by predicting crop yield and detecting crop diseases using Artificial Intelligence.

The system integrates **Machine Learning, Deep Learning, Cloud Databases, Weather APIs, and ETL pipelines** to provide intelligent insights for modern agriculture.

This project was developed as a **B.Tech Minor Project** to demonstrate the use of AI and data engineering in agriculture.

---

# 🚀 Key Features

🌾 Crop Yield Prediction using Machine Learning
🍃 Crop Disease Detection using Deep Learning
🌦 Real-time Weather Data Integration
☁️ Cloud Database using MongoDB Atlas
🔄 ETL Pipeline for dataset processing
📷 Image-based crop disease analysis
💡 Treatment recommendations for detected diseases

---

# 🧠 AI Modules

KrishMitra includes two Artificial Intelligence modules.

## 1️⃣ Crop Yield Prediction (Machine Learning)

The yield prediction module estimates the expected crop yield using agricultural and environmental factors.

### Input Features

* Crop type
* Season
* Area cultivated
* Rainfall
* Temperature
* Humidity

### Model

Machine Learning algorithms are used to train the yield prediction system.

Possible algorithms:

* Linear Regression
* Random Forest
* Gradient Boosting

The trained model predicts the **expected crop yield** for given inputs.

---

## 2️⃣ Crop Disease Detection (Deep Learning)

The disease detection module analyzes plant leaf images to identify diseases.

### Input

* Crop leaf image

### Model

A **Deep Learning Convolutional Neural Network (CNN)** model is used for disease classification.

### Supported Crops and Diseases

**Pepper**

* Pepper Bell Bacterial Spot
* Pepper Bell Healthy

**Potato**

* Potato Early Blight
* Potato Healthy

**Tomato**

* Tomato Early Blight
* Tomato Late Blight
* Tomato Healthy

The system provides **treatment recommendations** after detecting the disease.

---

# 🔄 System Workflow

```
User Input
   │
   ├── Crop Data → ML Model → Yield Prediction
   │
   └── Leaf Image → DL Model → Disease Detection
                            │
                            └→ Treatment Recommendation
```

---

# 🌦 Weather Module

KrishMitra integrates a **Weather API** to fetch real-time weather data.

Weather information includes:

* Temperature
* Humidity
* Wind speed
* Weather conditions

The API key is stored securely inside the `.env` file.

Example:

```
WEATHER_API_KEY=your_api_key
```

Weather data helps farmers understand environmental conditions affecting crops.

---

# 🗄 Database (MongoDB Atlas)

KrishMitra uses **MongoDB Atlas**, a cloud-based NoSQL database.

MongoDB stores:

* Agricultural dataset
* Crop information
* Processed data from ETL pipeline

---

# 🔄 ETL Pipeline

The project includes an **ETL pipeline implemented in `push_data.py`**.

### Extract

Agricultural dataset was collected locally.

### Transform

Dataset was cleaned and prepared for storage.

### Load

Processed dataset is uploaded to **MongoDB Atlas**.

Run the ETL script:

```
python push_data.py
```

This uploads the dataset to the cloud database.

---

# 📁 Project Structure

```
KRISHMITRA/
│
├── Backend/                 # Backend logic and ML pipeline
│
├── data/                    # Dataset used for training
│
├── final_model/             # Trained ML/DL models
│
├── Frontend/
│   ├── static/              # CSS, JavaScript, images
│   └── templates/           # HTML templates
│
├── logs/                    # Application logs
│
├── notebook/                # Jupyter notebooks for experiments
│
├── venv/                    # Virtual environment
│
├── .env                     # Environment variables
├── .gitignore
├── app.py                   # Main Flask application
├── push_data.py             # ETL script for MongoDB
├── requirements.txt         # Dependencies
├── setup.py                 # Project setup
├── QUICK_REFERENCE.md
└── README.md
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone the Repository

```
git clone https://github.com/navadeepgoud12/krishmitra.git
cd KRISHMITRA
```

---

## 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate environment.

### Windows

```
venv\Scripts\activate
```

### Linux / Mac

```
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create `.env` file.

```
MONGO_URI=your_mongodb_atlas_connection_string
WEATHER_API_KEY=your_weather_api_key
```

---

## 5️⃣ Load Dataset into MongoDB

Run the ETL script.

```
python push_data.py
```

This uploads the dataset to **MongoDB Atlas**.

---

## 6️⃣ Run the Application

```
python app.py
```

---

## 7️⃣ Open the Web Application

Open your browser.

```
http://127.0.0.1:5000
```

Upload a crop leaf image to detect diseases or enter crop details to predict yield.

---

# 🛠 Technologies Used

Python
Flask
Machine Learning
Deep Learning (CNN)
MongoDB Atlas
Weather API
HTML
CSS
JavaScript

---

# 🎯 Future Improvements

* Mobile application for farmers
* Pest detection system
* Multilingual farmer support
* IoT sensor integration
* Real-time farm monitoring

---

# 👨‍💻 Author

**Navadeep Goud**

B.Tech Student
Minor Project

AI Powered Smart Crop Yield & Disease Prediction System

---

# 📜 License

This project is developed for **academic and educational purposes only**.

