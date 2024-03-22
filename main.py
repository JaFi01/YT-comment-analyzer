from dotenv import load_dotenv
from googleapiclient.discovery import build
import os
import re

def main():
    load_dotenv()
    api_key_yt= os.getenv("YT_API_KEY")
    #video_url = str(input("Podaj adres url filmu"))
    video_url="https://www.youtube.com/watch?v=p4ZfkezDTXQ&ab_channel=AndrewHuberman"
    #this video is choosen to test, as feedback is positive.
    id = re.split('=|&' ,video_url)[1]

    youtube = build('youtube', 'v3', developerKey=api_key_yt)

    request = youtube.commentThreads().list(part="snippet", videoId=id, maxResults=100)
    response = request.execute()
    comments_array=[]
    for comment in response["items"]:
        author_name = comment["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
        comment_text = comment["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
        like_count = comment["snippet"]["topLevelComment"]["snippet"]["likeCount"]

        striped_comment = [like_count, author_name, comment_text]
        comments_array.append(striped_comment)

    comments_array.sort(key=lambda x: x[0], reverse=True)

    # Print the comments array
    for i, stripped_comment in enumerate(comments_array):
        output = str(stripped_comment[0]) + f" Likes + {stripped_comment[1]}:  {stripped_comment[2]}"
        print(i+1, ". "+output)

if __name__ == "__main__":
    main()