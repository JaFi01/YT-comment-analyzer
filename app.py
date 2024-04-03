from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from process_comments import main as pre_process_comments
from gpt_analysis import main as run_gpt
from models_analysis import main as run_vader

app = Flask (__name__)
CORS(app)  

@app.route('/')
def index():
    return "Hello World"

def load_comments():
    api_key_yt = os.getenv("YT_API_KEY")
    video_url = "https://www.youtube.com/watch?v=BtytYWhg2mc&ab_channel=StarWars"
    #video_url = "https://www.youtube.com/watch?v=IfvxPX_urqA&list=PLMxI7hwGp5kcOhZSDhcaPpyd3Xf8tGJof&index=109&ab_channel=UKFOnAir"
    comments =  pre_process_comments(api_key_yt, video_url)
    return comments

@app.route('/analyze_video_gpt', methods=['GET'])
def analyze_video_gpt():
    api_gpt_key = os.getenv("OPENAI_API_KEY")    
    selected_comments = load_comments()
    gpt_response = run_gpt(api_gpt_key, selected_comments)
    return jsonify({
        "gpt_response": gpt_response
    })
@app.route('/analyze_video_vader', methods=['GET'])
def analyze_video_vader(): 
    selected_comments = load_comments()
    neg_and_pos_content = run_vader(selected_comments[:200])
    negative_points, positive_points = neg_and_pos_content
    return jsonify({
        "negative_points": negative_points,
        "positive_points": positive_points,
    })

if __name__ == "__main__":
    app.run(debug=True, port=8080)