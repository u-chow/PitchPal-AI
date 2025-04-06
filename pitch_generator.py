
from transformers import pipeline

generator = pipeline("text2text-generation", model="t5-base")

def generate_pitch(product_description):
    prompt = f"Generate a startup pitch based on this product: {product_description}"
    result = generator(prompt, max_length=256, clean_up_tokenization_spaces=True)[0]['generated_text']
    return result
