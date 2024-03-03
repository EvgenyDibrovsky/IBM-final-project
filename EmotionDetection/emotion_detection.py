import requests

def emotion_detector(text_to_analyze):
    # Проверка на пустой ввод
    if not text_to_analyze.strip():
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=data, headers=headers)
    if response.ok:
        # Conversion
        emotions_data = response.json()['emotionPredictions'][0]['emotion']
        
        # Search 
        dominant_emotion = max(emotions_data, key=emotions_data.get)
        
        # Return
        result = {
            'anger': emotions_data['anger'],
            'disgust': emotions_data['disgust'],
            'fear': emotions_data['fear'],
            'joy': emotions_data['joy'],
            'sadness': emotions_data['sadness'],
            'dominant_emotion': dominant_emotion
        }
        return result
    elif response.status_code == 400:
        # None,  status_code 400
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    else:
        # Error
        return "Error: " + response.text

# print(emotion_detector("I am so happy I am doing this."))
