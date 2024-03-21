from dotenv import load_dotenv
from googleapiclient.discovery import build
import os

def main():
    load_dotenv()
    api_key_yt= os.getenv("YT_API_KEY")

    video_url="https://www.youtube.com/watch?v=bRwvhAGdMBM"
    id = video_url.split("=")[1]

    youtube = build('youtube', 'v3', developerKey=api_key_yt)

    request = youtube.commentThreads().list(part="snippet", videoId=id)
    response = request.execute()
    print(response)
    print('\n koniec bazowego response\n')
    for comment in response["items"]:
        author_name = comment["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
        comment_text = comment["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        print(f'{author_name}:  {comment_text} ')

if __name__ == "__main__":
    main()