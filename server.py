'''This is the routing for our flask app'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def send_emotion_detection():
    '''get text from ajax request and return emotion of text'''
    text = request.args['textToAnalyze']
    emotion = emotion_detector(text)

    if emotion['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    return f'''
    For the given statement, the system response is 'anger': {emotion['anger']},
    'disgust': {emotion['disgust']}, 'fear': {emotion['fear']}, 'joy': {emotion['joy']}
    and 'sadness': {emotion['sadness']}. The dominant emotion is {emotion['dominant_emotion']}
    '''

@app.route('/')
def index():
    '''render index.html'''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
