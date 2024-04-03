from flask import jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def normalize_like_amount(like_amount, max_like_amount):
    return like_amount/max_like_amount * 10


def analyze_sentiment(comment: str, value: float):
    """Analyse Positive and negative content in message, and pultiply sentiment based on likes count in that comment

    Args:
        comment (str): comment by user
        value (float): normalized like count. Value <0; 5>

    Returns:
        array: how much is positive and negative sentiment in comment times normalized like count
    """
    analyzer = SentimentIntensityAnalyzer()   
    # Sentiment analysis
    sentiment_score = analyzer.polarity_scores(comment)
    NEG_weighted  =  sentiment_score['neg'] * value
    POS_weighted  =  sentiment_score['pos'] * value
    
    #reducing querry, so comments which were unable to be valued are skipped
    if POS_weighted != 0 or NEG_weighted != 0:
        return [NEG_weighted, POS_weighted]
    else:
        pass


def main(comments_array):
    sum_of_points = [0, 0] #negative, and positive
    max_likes_amount = comments_array[0][0]
    for comment in comments_array:
        comment_value = normalize_like_amount(comment[0], max_likes_amount)
        sentiment = analyze_sentiment(comment[2], comment_value)
        
        if sentiment is not None:
            sum_of_points[0] += sentiment[0]  # Negative
            sum_of_points[1] += sentiment[1]  # Positive
    return sum_of_points 
    
    
    