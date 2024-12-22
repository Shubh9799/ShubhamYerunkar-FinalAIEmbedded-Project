import requests
import json  # Import the json library to handle the response

def emotion_detector(text_to_analyze):
    # Handle blank or whitespace-only input
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    input_data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    try:
        # Send POST request to Watson NLP emotion prediction service
        response = requests.post(url, json=input_data, headers=headers)
        
        if response.status_code == 200:
            # Convert the response text into a dictionary
            response_data = response.json()

            # Debugging: print the raw response to see its structure
            # print("Raw response:", json.dumps(response_data, indent=4))
            
            # Extract emotion data from the first prediction
            emotion_data = response_data['emotionPredictions'][0]['emotion']

            anger_score = emotion_data.get('anger', 0)
            disgust_score = emotion_data.get('disgust', 0)
            fear_score = emotion_data.get('fear', 0)
            joy_score = emotion_data.get('joy', 0)
            sadness_score = emotion_data.get('sadness', 0)
            
            # Find the dominant emotion with the highest score
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)

            # Return the response in the required format
            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
        else:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
    except Exception as e:
        print(f"Error during API call: {e}")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
