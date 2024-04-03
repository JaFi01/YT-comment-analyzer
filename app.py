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

@app.route('/analyze_video', methods=['POST'])
def analyze_video():
    api_key_yt = os.getenv("YT_API_KEY")
    video_url = request.json.get('video_url')
    
    selected_comments = pre_process_comments(api_key_yt, video_url)
    
    # Analiza GPT
    api_gpt_key = os.getenv("OPENAI_API_KEY")
    gpt_response = run_gpt(api_gpt_key, selected_comments)
    
    # Analiza VADER
    neg_and_pos_content = run_vader(selected_comments[:200])
    negative_points, positive_points = neg_and_pos_content
    
    return jsonify({
        "gpt_response": gpt_response,
        "negative_points": negative_points,
        "positive_points": positive_points
    })

if __name__ == "__main__":
    app.run(debug=True, port=8080)