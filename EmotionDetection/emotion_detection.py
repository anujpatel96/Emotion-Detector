# Import the requests library to handle HTTP requests
import requests  
import json
# Define a function named emotion_detector that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyse):  
    # URL of the emotion_detector service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse }} 
    # Set the headers required for the API request 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)
    # If the response status code is 200, extract the the information
    if response.status_code == 200:  
        # Format the response 
        formatted_response = json.loads(response.text)
        emotion_dict = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotion_dict['anger']
        disgust_score = emotion_dict['disgust']
        fear_score = emotion_dict['fear']
        joy_score = emotion_dict['joy']
        sadness_score = emotion_dict['sadness']
        # Find the key with the maximum value
        max_key = max(emotion_dict, key=emotion_dict.get)
        # Add a new key, to the dictionary as dominant_emotion
        emotion_dict['dominant_emotion'] = max_key

    # If the response status code is 500, set label and score to None
    elif response.status_code == 400:
        emotion_dict = {
        "anger": None, 
        "disgust": None, 
        "fear": None, 
        "joy": None, 
        "sadness": None, 
        "dominant_emotion": None
        }
        
    # Return the response text from the API
    return emotion_dict