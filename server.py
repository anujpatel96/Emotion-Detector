'''
This is the server.py file degined to host the server
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")
@app.route("/emotionDetector")
def sent_detection():
    '''
    This function is designed to invoke emotion_detector function
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        msg = "Invalid input! Try again."
    else:
        # Return a formatted string with the sentiment label and score
        msg = (
            f"For the given statement, the system response is 'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
            f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}."
        )
    return msg

@app.route("/")
def render_index_page():
    '''
    This function is set to redirect to main page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
    