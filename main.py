from dotenv import load_dotenv
import os
from process_comments import main as pre_process_comments

def main():
    load_dotenv()
    api_key_yt= os.getenv("YT_API_KEY")
    #video_url = str(input("Podaj adres url filmu"))
    #video_url="https://www.youtube.com/watch?v=p4ZfkezDTXQ&ab_channel=AndrewHuberman"
    
    video_url="https://www.youtube.com/watch?v=V4gGJ7XXlC0&ab_channel=Fireship"
    pre_process_comments(api_key_yt, video_url)
    

if __name__ == "__main__":
    main()