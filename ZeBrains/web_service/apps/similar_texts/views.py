import numpy as np
from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import render
from transformers import AutoTokenizer
import numpy as np


def get_distance(request):
    if request.method == "POST":
        text1 = request.POST.get("textField1",None)
        text2 = request.POST.get("textField2",None)

        if len(text1)==0 or len(text2)==0:
            return render(request, "texts_distance.html", {"score": "Incorrect input! Both textfields must contain text!"})

        else:
            tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
            token = tokenizer([text1, text2], padding=True, truncation=True, return_tensors="np")

            token1 = token['input_ids'][0]
            token2 = token['input_ids'][1]
            score = (token1@token2)/(np.linalg.norm(token1)*np.linalg.norm(token2))

            return render(request, "texts_distance.html", {"score": (score+1)/2, "text1": text1, "text2": text2,})

    else:
        return render(request, "texts_distance.html")
