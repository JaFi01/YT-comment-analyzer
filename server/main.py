from dotenv import load_dotenv
import os
from process_comments import main as pre_process_comments
from gpt_analysis import main as run_gpt
from models_analysis import main as run_vader


    
def main():
    """This is file kept as program was in console only at the begining. 
        main.py can be used if You dont want to run whole app in web.
    """
    load_dotenv()
    api_key_yt = os.getenv("YT_API_KEY")
    api_gpt_key = os.getenv("OPENAI_API_KEY")
    video_url = str(input("Input URL to specific YouTube video: "))
    selected_comments = pre_process_comments(api_key_yt, video_url)
    neg_and_pos_content = run_vader(selected_comments)
    print(f'Negative sentiment content: {neg_and_pos_content[0]} Positive sentiment content: {neg_and_pos_content[1]}')
    run_gpt(api_gpt_key, selected_comments)
    
    
if __name__ == "__main__":
    main()
    