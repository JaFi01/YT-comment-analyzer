from googleapiclient.discovery import build
import requests

def get_video_id(video_url: str):
    """Quick function stripping url to get video id"""
    try:
        return video_url.split('?v=')[1].split('&')[0]
    except:
        return False



def get_video_comment_count(video_url: str, api_key_yt: str):
    """This method gets total amount of comments for url provided

    Args:
        video_url (str): link to video
        api_key_yt (str): api key stored in .env file

    Returns:
        _type_: total amount of comments
    """

    video_id = get_video_id(video_url)
    api_endpoint = f'https://www.googleapis.com/youtube/v3/videos?key={api_key_yt}&part=statistics&id={video_id}'

    try:
        response = requests.get(api_endpoint)
        response.raise_for_status() 
        data = response.json()
        #Extracting total comment threads count
        try:
            total_comments = int(data['items'][0]['statistics']['commentCount'])        
            return total_comments
        except:
            return False

    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}. Mayby URL to video might be incorrect")
        ans = "Error ocured during requesting comments for video. Is URL address correct? Error: {e}"
        return ans
    

def prepare_comments(api_key_yt: str, id: str, total_comments: int):
    """This method gets content of comments, likes and save them to array for further processing

    Args:
        api_key_yt (str): api key stored in .env file
        id (str): id of video parsed from url
        total_comments (int): amount of comments
    """
    youtube = build('youtube', 'v3', developerKey=api_key_yt)
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
    
    comments_array= sorted(comments_array, key=lambda x: x[0], reverse=True)
    return comments_array
    


def main(api_key_yt, video_url):
    id = get_video_id(video_url)
    if (id == False):
        return False
    # Limiting amount of comment to read
    total_comments = False
    comments_limit_amount = 2000 #request on YT api are limited, so i need to limit amount of my request aswell
    total_comments = get_video_comment_count(video_url, api_key_yt)
    if (total_comments == False):
        return False
    else:
        total_comments = min(total_comments, comments_limit_amount) if total_comments else 0
        
        selected_comments = prepare_comments(api_key_yt, id, total_comments)
        return selected_comments
