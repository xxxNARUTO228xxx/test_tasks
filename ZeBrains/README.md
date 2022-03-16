# ZeBrains-WebService
This repo contains test task to ZeBrains company - more detailed description in task.md

## Task 1. Emotion-detection with multilabel classification with BERT
link/emotion_detect/
1. I took pretrained for emotions AutoTokenizer and AutoModelForSequenceClassification from transformers library.
2. Added them to pipeline and called "go_brrr" function

![image](https://user-images.githubusercontent.com/44481414/145414420-8b24c394-c8a2-4a8e-be98-9fdf11f48995.png)


## Task 2. Image-text-recognition using any OCR framework
link/img_to_text/

1. import easyocr and go_brrr

Image for recognition:

![img](https://user-images.githubusercontent.com/44481414/145414965-79121e1e-fc46-4d34-be84-50f1c3240e62.jpg)


Results:

![image](https://user-images.githubusercontent.com/44481414/145415107-4739c712-e326-4279-a9af-df42300868ca.png)


## Task 3. Similar-texts-recognition using any algorithm
link/similar_texts/
1. from transformers import AutoTokenizer
2. Tokenized two texts with padding
3. Computed cos-distance between these vectors (rescaled from 0 to 1 as well)

![image](https://user-images.githubusercontent.com/44481414/145415994-29079485-3ae5-4570-82e7-23903f9abcad.png)

