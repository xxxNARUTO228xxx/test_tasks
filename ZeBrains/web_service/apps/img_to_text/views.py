import numpy as np
from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import render
import easyocr


def im2text(request):
    if request.method == "POST":
        #
        # Django image API
        #
        try:
            file = request.FILES["imageFile"]
            file_name = default_storage.save(file.name, file)
            file_url = default_storage.path(file_name)

            reader = easyocr.Reader(['en','en'])
            result = reader.readtext(file_url, detail = 0)
            result = " ".join(result)
        except:
            result = "Incorrect input! Upload an image!"

        return render(request, "im_to_text.html", {"predictions": result})

    else:
        return render(request, "im_to_text.html")
