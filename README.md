# 📩 Spam Message Detection using NLP
Website : https://spam-message-detection-ty37.onrender.com

> A Machine Learning and Natural Language Processing project that classifies SMS messages as **Spam** or **Ham** using **TF-IDF Vectorization** and **Multinomial Naive Bayes**, deployed with Flask.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-green?style=for-the-badge)

---

## 📌 Project Overview

Spam messages are a common issue in emails and SMS services. This project uses **Natural Language Processing (NLP)** techniques to automatically classify incoming messages into:

- ✅ HAM (Legitimate Message)
- 🚫 SPAM (Unwanted/Promotional Message)

The application provides an easy-to-use web interface where users can enter text and instantly receive the prediction.

---

## 🚀 Features

- Spam/Ham message classification
- NLP preprocessing using TF-IDF Vectorizer
- Machine Learning model using Multinomial Naive Bayes
- Flask-based web application
- Fast prediction using saved model (.pkl)
- Simple and responsive interface

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Flask | Backend Web Framework |
| Scikit-learn | Machine Learning |
| TF-IDF Vectorizer | Text Feature Extraction |
| Multinomial Naive Bayes | Classification Algorithm |
| HTML/CSS | Frontend |

---

## 📂 Project Structure

```
Spam-Detection/
│
├── app.py
├── nlp_model.pkl
├── tfidf.pkl
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── css/
│   └── images/
│
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/spam-message-detection.git
```

```bash
cd spam-message-detection
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 🧠 Machine Learning Workflow

```
Input Message
       │
       ▼
Text Preprocessing
       │
       ▼
TF-IDF Vectorization
       │
       ▼
Multinomial Naive Bayes Model
       │
       ▼
Prediction
       │
 ┌──────────────┐
 │ Spam / Ham   │
 └──────────────┘
```

---

## 📷 Screenshots

<img width="1915" height="976" alt="Screenshot 2026-07-27 144634" src="https://github.com/user-attachments/assets/5aff21f7-fcf8-4847-a729-427107197f6e" />
<img width="1917" height="967" alt="Screenshot 2026-07-27 144707" src="https://github.com/user-attachments/assets/96e5afe9-3174-4cc3-96ee-dd9026184344" />



## 📊 Model Used

- **Algorithm:** Multinomial Naive Bayes
- **Vectorizer:** TF-IDF
- **Task:** Binary Text Classification
- **Output Classes:**
  - HAM
  - SPAM

---

## 🎯 Future Improvements

- Add text preprocessing pipeline
- Support multiple languages
- Improve UI/UX
- Deploy on Render or Railway
- Integrate Deep Learning (LSTM/BERT)
- Add probability/confidence score
- Store prediction history

---

## 💻 Requirements

Install all required packages using:

```bash
pip install -r requirements.txt
```

Main libraries:

- Flask
- Scikit-learn
- NumPy
- SciPy
- Joblib
- Gunicorn

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Create a Pull Request

---

## 👨‍💻 Author

**Darshan Patil**

- LinkedIn: https://linkedin.com/in/darshanpatil1
- GitHub: https://github.com/darshan1845

---

## ⭐ Support

If you found this project useful, don't forget to **Star ⭐ the repository**.

It motivates me to build more Machine Learning and AI projects!

---

## 📜 License

This project is licensed under the MIT License.
