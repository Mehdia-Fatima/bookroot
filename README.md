# 📚 BookRoot 🌱  
**An intelligent Android lifestyle app for book insights, recommendations, and reader profiling** <br><br>
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://bookroot-prototype.streamlit.app/)

BookRoot is a **machine learning–driven Android application** that uses book metadata and reader reviews to deliver **personalized recommendations, intelligent summaries, and reader behavior insights**.

The project focuses on **building robust ML/NLP models** and integrating them into a **native Android app built with Kotlin**, with the goal of publishing on the **Google Play Store**.

---

## 🌿 The Core Concept: The World-Tree
In this ecosystem, progress is organic. Every book started, journal entry written, or habit completed acts as nutrients for your **Personal Tree**. 



* **Sprout:** Begin a new book or habit.
* **Leaves:** Maintain a reading or journaling streak.
* **Blossom:** Complete a book or reach a significant milestone.
* **Arbor:** Reflect on a forest of past achievements and intellectual growth.

---

## 🎯 Project Goals

- Build real-world **machine learning models** on book and review data  
- Apply **NLP** to understand reader sentiment and themes  
- Create a **recommendation system** for personalized book discovery  
- Design a **production-ready Android app**  
- Deploy and publish the app on the **Google Play Store**

---

## 🧠 Core Features (Planned)

### 📊 Book Analytics
- Book metadata analysis (author, genre, publication year, editions)  
- Genre and author trend analysis  
- Popularity indicators based on ratings and reviews  

### 🧾 Natural Language Processing (NLP)
- Sentiment analysis on book reviews  
- Topic modeling to extract major themes  
- AI-generated review summaries for quick understanding  

### 🤝 Recommendation System
- Content-based recommendations using embeddings  
- Collaborative filtering using ratings  
- Hybrid recommendation engine  
- “Books similar to what you like” suggestions  

### 👤 Reader Profiling & Clustering
- Cluster users based on reading preferences  
- Predict reader personas (e.g., Explorer, Comfort Reader, Literary Enthusiast)  
- Input: user’s favorite books or genres  

### 📈 Predictive Modeling
- Book popularity prediction using regression models  
- Explainable ML (feature importance)  

---

## 🚀 Working Prototype (Streamlit)
A functional web-based prototype has been developed to serve as a "Logic Testing Ground." This allows for rapid iteration of growth algorithms and API data parsing before final mobile deployment.

* **Live Discovery:** Real-time search using the **Open Library API**.
* **XP Engine:** Logic that converts reading progress into "Biological Nutrients" (XP).
* **NLP Sandbox:** Testing sentiment analysis on journal entries to determine "weather" effects (Sun/Rain) for the tree.

**To run the prototype:**
```bash
cd prototypes/streamlit_app
pip install -r requirements.txt
streamlit run app.py
```

---

## 📱 Android Application

- **Platform:** Android  
- **Language:** Kotlin  
- **IDE:** Android Studio  
- **Architecture:** MVVM (planned)  
- **UI Focus:** Clean, simple, lifestyle-oriented experience  
- **Backend:** ML models served via APIs (planned)  

The Android app will:
- Allow users to discover books  
- Provide AI-generated insights  
- Offer personalized recommendations  
- Deliver an engaging, consumer-facing experience  

---

## 🛠️ Tech Stack

### Machine Learning & Data
- Python  
- Pandas, NumPy  
- Scikit-learn  
- NLP: Transformers, Topic Modeling  
- Recommendation systems  
- Regression & clustering models  

### Data Sources
- Open Library API  
- Public book review datasets  
- Google Books API (optional / later)  

### Mobile Development
- Kotlin  
- Android Studio  
- REST APIs for ML integration  

---

## 📂 Project Structure

- **BookRoot/**
  - **data/**
    - raw/
    - processed/
  - **notebooks/**
    - eda.ipynb
    - sentiment_analysis.ipynb
    - topic_modeling.ipynb
    - recommendation_system.ipynb
  - **models/**
    - sentiment_model.pkl
    - recommender_model.pkl
  - **backend/**
    - api/ *(ML model serving – planned)*
  - **prototypes/**
    - streamlit_app/
      - app.py
      - requirements.txt
  - **android/**
    - BookRootApp/ *(Kotlin Android app)*
  - requirements.txt
  - README.md

---

## 🚧 Development Status

- [x] Project planning & architecture  
- [ ] Data collection & cleaning  
- [ ] NLP model development  
- [ ] Recommendation system  
- [ ] Backend API setup
- [ ] Web Prototype: Streamlit MVP functional for logic validation.
- [ ] Android app MVP: Porting UI to Kotlin/Jetpack Compose.
- [ ] Play Store deployment  

---

## 🔮 Future Enhancements

- Knowledge graphs for books and authors  
- Mood-based reading recommendations  
- Book-to-movie adaptation analysis  
- Social and cultural insights from literature  

---

## 👩‍💻 Author

**Mehdia Fatima**  
Data Scientist | Machine Learning | Analytics  

Building end-to-end ML products with real-world impact.
