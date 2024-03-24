from googleapiclient.discovery import build
import requests

def get_video_id(video_url: str):
    """Quick function stripping url to get video id"""
    return video_url.split('?v=')[1].split('&')[0]


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
        total_comments = int(data['items'][0]['statistics']['commentCount'])
        
        return total_comments

    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return None
    

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
    
    selected_comments = get_comments_above_median_likes(comments_array=comments_array)
    return selected_comments
    
def get_comments_above_median_likes(comments_array):
    """this function sorts comments by likes, and select best ones

    Args:
        comments_array (_type_): array of parsed coments
    """

    # Sort comments array by like count
    sorted_comments = sorted(comments_array, key=lambda x: x[0], reverse=True)

    # Calculate median
    num_comments = len(sorted_comments)
    if num_comments % 2 == 0:
        median_index = num_comments // 2
        median_likes = (sorted_comments[median_index - 1][0] + sorted_comments[median_index][0]) / 2
    else:
        median_index = num_comments // 2
        median_likes = sorted_comments[median_index][0]

    # Return comments with likes higher than median or top 50 liked comments
    median_comments = [comment for comment in sorted_comments if comment[0] > median_likes][:50]
    return median_comments
    


def main(api_key_yt, video_url):
    id = get_video_id(video_url)

     # Limiting amount of comment to read
    comments_limit_amount = 500
    total_comments = get_video_comment_count(video_url, api_key_yt)
    total_comments = min(total_comments, comments_limit_amount) if total_comments else 0
    #print(total_comments)
    
    selected_comments = prepare_comments(api_key_yt, id, total_comments)
    return selected_comments


if __name__ == "__main__":
    main()