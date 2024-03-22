from dotenv import load_dotenv
from googleapiclient.discovery import build
import os
import re
import requests

def get_video_comment_count(video_url, api_key):
    # Extracting video ID from the URL
    video_id = video_url.split('?v=')[1].split('&')[0]

    # Constructing the API request URL
    api_endpoint = f'https://www.googleapis.com/youtube/v3/videos?key={api_key}&part=statistics&id={video_id}'


    try:
        # Sending GET request to the YouTube API
        response = requests.get(api_endpoint)
        response.raise_for_status()  # Raises exception for bad responses

        # Parsing the JSON response
        data = response.json()

        # Extracting total comment threads count
        total_comments = int(data['items'][0]['statistics']['commentCount'])


        return total_comments

    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return None

def main():
    load_dotenv()
    api_key_yt= os.getenv("YT_API_KEY")
    #video_url = str(input("Podaj adres url filmu"))
    video_url="https://www.youtube.com/watch?v=p4ZfkezDTXQ&ab_channel=AndrewHuberman"
    #this video is choosen to test, as feedback is positive.
    id = re.split('=|&' ,video_url)[1]

    youtube = build('youtube', 'v3', developerKey=api_key_yt)

    # Getting amount of comments
    total_comments = get_video_comment_count(video_url, api_key_yt)
    total_comments = min(total_comments, 500) if total_comments else 0
    print(total_comments)

    comments_array=[]
    next_page_token = None

    while total_comments > 0:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=id,
            maxResults=min(total_comments, 100),  # Max 100 comments per request
            pageToken=next_page_token
        )
        response = request.execute()
        for comment in response["items"]:
            author_name = comment["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
            comment_text = comment["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
            like_count = comment["snippet"]["topLevelComment"]["snippet"]["likeCount"]
            striped_comment = [like_count, author_name, comment_text]
            comments_array.append(striped_comment)
            total_comments -= 1
            if total_comments <= 0:
                break
        next_page_token = response.get("nextPageToken")
        if not next_page_token or total_comments <= 0:
            break
    
    comments_array.sort(key=lambda x: x[0], reverse=True)

    # Print the comments array
    for i, stripped_comment in enumerate(comments_array[:50]):
        output = str(stripped_comment[0]) + f" Likes + {stripped_comment[1]}:  {stripped_comment[2]}"
        print(i+1, ". "+output)

if __name__ == "__main__":
    main()