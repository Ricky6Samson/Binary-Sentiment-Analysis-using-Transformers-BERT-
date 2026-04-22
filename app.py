from transformers import BertTokenizer, BertForSequenceClassification
import torch
import gradio as gr


# -----------------------------
# Load model
# -----------------------------
def load_model():
    model = BertForSequenceClassification.from_pretrained(r"C:\Users\CSC\Documents\New Portfolio\sentiment-transformer\model")
    tokenizer = BertTokenizer.from_pretrained(r"C:\Users\CSC\Documents\New Portfolio\sentiment-transformer\model")

    model.eval()

    return model, tokenizer

model, tokenizer = load_model()


# -----------------------------
# Prediction function
# -----------------------------
def predict(text):
    inputs=tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():
        outputs=model(**inputs)

    pred=torch.argmax(outputs.logits,dim=1).item()

    return "Positive" if pred == 1 else "Negative"


# -----------------------------
# Gradio UI
# -----------------------------
interface = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(
        lines=4,
        placeholder="Enter a review..."
    ),
    outputs=gr.Textbox(label="Sentiment"),
    title="Sentiment Analysis (BERT)",
    description="Binary sentiment classifier (Positive / Negative)"
)

interface.launch(inbrowser=True)