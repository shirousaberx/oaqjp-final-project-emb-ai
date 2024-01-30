import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=payload, headers=header)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }   

    elif response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
        
        dominant_emotion = ''
        minimum_score = 0

        for key, value in emotion_scores.items():
            if value > minimum_score:
                minimum_score = value
                dominant_emotion = key
        
        emotion_scores['dominant_emotion'] = dominant_emotion

        return emotion_scores

    ''' Returned emotion_scores
    {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': '<name of the dominant emotion>'
    }
    '''