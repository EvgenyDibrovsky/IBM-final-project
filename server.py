"""Flask server for emotion detection application."""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Detect emotion from the text input.
    Returns a JSON response with emotion scores and dominant emotion.
    Returns an error message if the input text is invalid.
    """
    data = request.json
    text = data['text']
    result = emotion_detector(text)

    if result['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again!"})

    response = {
        "anger": result['anger'],
        "disgust": result['disgust'],
        "fear": result['fear'],
        "joy": result['joy'],
        "sadness": result['sadness'],
        "dominant_emotion": result['dominant_emotion']
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
