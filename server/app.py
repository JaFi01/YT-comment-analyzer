from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask.helpers import send_from_directory
from dotenv import load_dotenv
import os
import requests
from process_comments import main as pre_process_comments
from gpt_analysis import main as run_gpt
from models_analysis import main as run_vader
from wordcloud import prepare_word_cloud

app = Flask (__name__, static_folder='client/build', static_url_path='')
CORS(app)  

def check_video_existence(video_url):
    try:
        response = requests.head(video_url)
        return response.status_code == 200
    except requests.RequestException:
        return False

@app.route('/analyze_video', methods=['POST'])
@cross_origin()
def analyze_video():
    api_key_yt = os.getenv("YT_API_KEY")
    video_url = request.json.get('video_url')


    selected_comments = pre_process_comments(api_key_yt, video_url)
    if selected_comments == False:
        return jsonify({
        "error_status_YT_url": True        
    })
       
    # GPT
    api_gpt_key = os.getenv("OPENAI_API_KEY")
    gpt_response = run_gpt(api_gpt_key, selected_comments)
    
    # VADER
    neg_and_pos_content = run_vader(selected_comments[:200])
    negative_points, positive_points = neg_and_pos_content
    comments_highlights =(selected_comments[:3])
    
    #wordcloud
    wordcloud_querry = prepare_word_cloud(selected_comments)
    return jsonify({
        "gpt_response": gpt_response,
        "negative_points": negative_points,
        "positive_points": positive_points,
        "comments_highlights": comments_highlights,
        "wordcloud_content": wordcloud_querry,
        "error_status_YT_url": False   
    })
@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(debug=True, port=8080)