import nltk
from unidecode import unidecode
import re
from nltk.util import ngrams
from collections import Counter
import string
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fastapi import FastAPI
from pydantic import BaseModel


def cosseno(formated,endereco):
    # Vetoriza os endereços
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(formated + [endereco])

    # Calcula a similaridade de cosseno entre o endereço fornecido e os endereços no dataset
    similarities = cosine_similarity(X[-1], X[:-1])

    # Encontra o índice do endereço mais similar
    index = similarities.argmax()

    if similarities[0][index] > 0:
        return formated[index]
    else:
        return "Endereço não encontrado"

# ===================== TESTE POR N-GRAM (VIGENTE) ================
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def calculate_similarity(text1, text2, n):
    text1 = preprocess_text(text1)
    text2 = preprocess_text(text2)

    ngrams_text1 = list(ngrams(text1.split(), n))
    ngrams_text2 = list(ngrams(text2.split(), n))

    ngrams_text1_counter = Counter(ngrams_text1)
    ngrams_text2_counter = Counter(ngrams_text2)

    intersection_count = sum((ngrams_text1_counter & ngrams_text2_counter).values())

    union_count = len(ngrams_text1) + len(ngrams_text2) - intersection_count
    similarity = intersection_count / union_count

    return similarity

class Item(BaseModel):
    name: str


features = {
    "cosseno":cosseno
}

with open("./datassets/enderecos/vetor-de-enderecos.txt","r") as file:
    formated = file.readlines()

unliked_items = [",",".",":","/","-","?","'"]

app = FastAPI()

@app.post("/address/")
async def create_item(item: Item):
    similaritys = [calculate_similarity(item.name,i,1) for i in formated]
    return formated[similaritys.index(max(similaritys))]