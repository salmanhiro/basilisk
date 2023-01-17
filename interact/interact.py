import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from transformers import AutoTokenizer

# Load the model and tokenizer
model = tf.keras.models.load_model("models/124M") # My model
tokenizer = AutoTokenizer.from_pretrained("text-davinci-002")

def generate_text(prompt):
    # Preprocess the prompt
    prompt_encoded = tokenizer.texts_to_sequences([prompt])
    prompt_encoded = tf.keras.preprocessing.sequence.pad_sequences(prompt_encoded, maxlen=1024)

    # Use the model to generate text
    generated_text = model.predict(prompt_encoded)

    # Decode the generated text
    generated_text = tokenizer.sequences_to_texts(generated_text)
    return generated_text

prompt = input("Enter a prompt to generate text: ")
generated_text = generate_text(prompt)
print(generated_text)
