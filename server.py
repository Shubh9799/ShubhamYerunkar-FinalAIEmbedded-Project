from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    # Extract statement from the request
    data = request.get_json()
    text = data.get("statement", "")

    # Call the emotion detector function
    result = emotion_detector(text)

    # Handle cases where dominant_emotion is None
    if result["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    # Prepare the response
    response = {
        "anger": result["anger"],
        "disgust": result["disgust"],
        "fear": result["fear"],
        "joy": result["joy"],
        "sadness": result["sadness"],
        "dominant_emotion": result["dominant_emotion"]
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
    app.run(port=5001)
