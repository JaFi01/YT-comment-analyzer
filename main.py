from dotenv import load_dotenv
import os
from process_comments import main as pre_process_comments
from gpt_analysis import main as run_gpt

def main():
    load_dotenv()
    api_key_yt = os.getenv("YT_API_KEY")
    api_gpt_key = os.getenv("OPENAI_API_KEY")
    video_url = str(input("Podaj adres url filmu: "))
    #video_url="https://www.youtube.com/watch?v=p4ZfkezDTXQ&ab_channel=AndrewHuberman"
    
    # video_url="https://www.youtube.com/watch?v=V4gGJ7XXlC0&ab_channel=Fireship"
    selected_comments = pre_process_comments(api_key_yt, video_url)
    run_gpt(api_gpt_key, selected_comments)
    

if __name__ == "__main__":
    main()