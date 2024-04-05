import re
import json

def prepare_word_cloud(selected_comments):
    first_comments = " ".join(comment[2] for comment in selected_comments[:10])
    # Usunięcie znaków interpunkcyjnych
    first_comments = re.sub(r'[^\w\s]', '', first_comments)
    # Zamiana spacji na znak '%20'
    first_comments = first_comments.replace(" ", "%20").replace("\n", "%20")
    colors_rgba = [
    "rgba(143, 191, 224, 1)",   # Light Blue
    "rgba(124, 119, 185, 1)",   # Purple
    "rgba(29, 138, 153, 1)",    # Teal
    "rgba(11, 201, 205, 1)",    # Turquoise
    "rgba(20, 255, 247, 1)"     # Aqua
]
    colors_json = json.dumps(colors_rgba)
    query = f"https://quickchart.io/wordcloud?text={first_comments}&rotation=0&colors={colors_json}&height=400"
    return(query)
    
    #https://quickchart.io/wordcloud?text=To%20be%20or%20not%20to%20be%2C%20that%20is%20the%20question