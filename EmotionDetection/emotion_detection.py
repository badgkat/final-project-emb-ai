import requests  # Import the requests library to handle HTTP requests
import json  # Import the json library to handle JSON data

def emotion_detector(text_to_analyse):  
    """Define a function named emotion_detector that takes a string input (text_to_analyse)"""
    
    # URL of the Emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
   
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }  
   
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)
    
    # Parsing the JSON response from the API
    formatted_response = response.json()
    
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Navigate the response to get to the emotion scores
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        # Find dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
    
    # If the response is not OK, set emotions to None
    else:
        emotions = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None
        }
        dominant_emotion = None

    return {
        "anger": emotions['anger'],
        "disgust": emotions['disgust'],
        "fear": emotions['fear'],
        "joy": emotions['joy'],
        "sadness": emotions['sadness'],
        "dominant_emotion": dominant_emotion
    }