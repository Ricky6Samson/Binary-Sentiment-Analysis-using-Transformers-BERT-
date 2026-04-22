# 📌 Sentiment Analysis using BERT (Multi-Domain)

## 🚀 Live Demo

👉 Hugging Face Space: https://huggingface.co/spaces/ricky-samson/binary-sentiment-classifier

---

## 📌 Overview

This project implements a **Transformer-based sentiment analysis system using BERT**, designed to classify text as **Positive or Negative**.

The model was initially trained on a single dataset (IMDB) and later improved using a **multi-domain training strategy (IMDB + Amazon + Yelp)** to enhance real-world robustness and generalization.

---

## 🧠 Key Improvement: Single-Domain → Multi-Domain Learning

### ❌ Initial Model (IMDB Only)

* Strong performance on movie reviews
* Weak generalization on product and service reviews
* Struggled with real-world diverse text inputs

### ✅ Final Model (Multi-Domain)

Trained on:

* IMDB (movie reviews)
* Amazon (product reviews)
* Yelp (service reviews)

**Outcome:**

* Improved robustness across different domains
* More stable predictions on real-world text
* Better generalization beyond movie reviews

---

## 📊 Key Insight

This project demonstrates that **domain diversity in training data significantly improves NLP model generalization**.

Single-domain training leads to overfitting on specific linguistic patterns, while multi-domain training creates a more adaptable sentiment classifier for real-world use cases.

---

## 🛠️ Tech Stack

* Python
* PyTorch
* Hugging Face Transformers (BERT)
* Gradio

---

## 📂 Project Structure

```
sentiment-transformer/
│
├── app.py              # Gradio inference app
├── requirements.txt    # Dependencies
├── model/              # Trained BERT model + tokenizer
└── notebooks/          # Training pipeline
```

---

## ▶️ Run Locally

```bash
conda activate bert_env
cd sentiment-transformer
python app.py
```

Then open:

```
http://127.0.0.1:7860
```

---

## 🌐 Deployment

Deployed using **Hugging Face Spaces (Gradio)** for real-time inference and public access.

---

## ⚠️ Limitations

* Binary classification only (Positive / Negative)
* Limited sarcasm understanding
* Performance depends on domain similarity to training data

---

## 🔮 Future Improvements

* Add confidence score visualization
* Introduce neutral sentiment class
* Improve sarcasm and irony detection
* Expand dataset diversity further
* Experiment with larger transformer architectures (RoBERTa, DeBERTa)

---

## 👤 Author

Ricky Samson
