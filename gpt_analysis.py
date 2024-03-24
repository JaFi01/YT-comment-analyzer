from openai import OpenAI
def comments_for_gpt(selected_comments):
    selected_comments=selected_comments[:15]
    comments_to_string = ""
    for i, selected_comment in enumerate(selected_comments):
        output = str(selected_comment[0]) + f" Likes: {selected_comment[2]}"
        comments_to_string += output
        print(i+1, ". "+output)

    return comments_to_string


def main(gpt_api_key, selected_comments):
    client = OpenAI()
    client.api_key = gpt_api_key
    comments = comments_for_gpt(selected_comments)
    print("\n\n"+comments)
    
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages =[
            {"role": "user", "content": "You will be given 25 most"+ 
                "liked coments under YouTube video, with likes amount."+ 
                "Based on them determine what people think about video. Comments: "+comments+"+- The end of comments"}
        ]
    )
    asistant_response = response.choices[0].message.content
    usage = response.usage
    print(f"\n GPT-analysis: {asistant_response} cost: {usage}")

if __name__ == "__main__":
    main()