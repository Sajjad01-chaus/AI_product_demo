from transformers import AutoTokenizer, AutoModelForSequenceClassification

# A small pre-trained model for demo 
model_name = "distilbert-base-uncased"

print("Downloading and saving model...")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

tokenizer.save_pretrained("./model")
model.save_pretrained("./model")

print("Model saved to ./model/")
