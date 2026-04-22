# Sentiment Analysis using BERT (Multi-Domain)

## 📌 Overview

This project implements a **Transformer-based sentiment analysis system** using BERT for binary classification (**Positive / Negative**).

The project evolved from an initial single-domain model to a more robust **multi-domain model**, improving performance on real-world, diverse text inputs.

---

## 🚀 Features

* BERT-based sentiment classification
* Binary output: Positive / Negative
* Gradio web interface for real-time predictions
* Improved generalization using multi-domain training
* Ready for deployment on Hugging Face Spaces

---

## 🧠 Model Development Journey

### 1. Initial Approach — IMDB-Only Model

* Trained exclusively on IMDB movie reviews
* Performed well on movie-related text
* Showed **inconsistent predictions on general reviews** (e.g., products, services)

### 2. Improved Approach — Multi-Domain Model

* Trained on a combination of:

  * IMDB (movie reviews)
  * Amazon (product reviews)
  * Yelp (service reviews)
* Result:

  * More **stable and consistent predictions**
  * Better handling of **diverse real-world inputs**

---

## 📊 Key Insight

This project highlights the impact of domain diversity in training data.

* Single-domain models may struggle when applied to different types of text
* Multi-domain training improves robustness and generalization
* Real-world NLP systems benefit from **diverse data sources**

---

## 🛠️ Tech Stack

* Python
* PyTorch
* Hugging Face Transformers
* Gradio

---

## 📂 Project Structure

```
sentiment-transformer/
│
├── app.py              # Gradio app for inference
├── requirements.txt   # Dependencies
├── model/             # Trained model + tokenizer
└── notebooks/         # Training notebook (optional)
```

---

## ▶️ Run Locally

```bash
conda activate bert_env
cd sentiment-transformer
python app.py
```

Then open in browser:
http://127.0.0.1:7860

---

## 🌐 Deployment

This project is designed to be deployed using **Gradio on Hugging Face Spaces** for public access.

---

## ⚠️ Limitations

* Binary classification only (no neutral class)
* May struggle with sarcasm or highly ambiguous text
* Not optimized for extremely domain-specific language

---

## 🔮 Future Improvements

* Add neutral sentiment class
* Improve sarcasm detection
* Train on larger and more diverse datasets
* Add confidence scores to predictions

---

## 📌 Author

Ricky Samson
