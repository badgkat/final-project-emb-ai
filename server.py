''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("EmotionDetectionApp")

@app.route("/emotionDetector")
def emote_det():
    """Analyze sentiment for the given text query parameter and return result."""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Pass the text to the emotion detector function
    result = emotion_detector(text_to_analyze)
    
    #extract the dominant emotion from the result
    dominant_emotion = result['dominant_emotion']
    
    #extract the emotion predictions
    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear'] 
    sadness = result['sadness']
    joy = result['joy']
    
    return (
        f"For the given statement, the system response is: "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is '{dominant_emotion}'."
    )

@app.route("/")
def render_index_page():
    """Render the index HTML page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)