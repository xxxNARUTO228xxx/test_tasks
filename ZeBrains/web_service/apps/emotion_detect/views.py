import numpy as np
from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import render
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline


def text2emo(request):
    if request.method == "POST":
        text = request.POST.get("textField",None)

        if len(text) != 0:
            tokenizer = AutoTokenizer.from_pretrained("lordtt13/emo-mobilebert")
            model = AutoModelForSequenceClassification.from_pretrained("lordtt13/emo-mobilebert")
            nlp_sentence_classif = pipeline('sentiment-analysis', model = model, tokenizer = tokenizer)
            output = nlp_sentence_classif(text)

            return render(request, "emo_detect.html", {"label": output[0]['label'], "score": output[0]['score'], "text": text})
        else:
            return render(request, "emo_detect.html", {"label": "Incorrect input!", "score": "Text area is empty!"})

    else:
        return render(request, "emo_detect.html")
