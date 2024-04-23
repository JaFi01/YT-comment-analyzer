# YouTube Comment Analyzer #
**YouTube Comment Analyzer** is a web application that analyzes sentiment in comments posted under YouTube videos. It utilizes machine learning techniques to provide insights into the sentiment of the comments and generates visualizations to help users understand the sentiment distribution.

## Features ##
**Sentiment Analysis**: Utilizes Natural Language Processing (NLP) techniques to analyze the sentiment of comments.
GPT-3.5 Integration: Incorporates OpenAI's GPT-3.5-turbo model to generate AI responses based on the comments.

**VADER Sentiment Analysis**: Implements the VADER sentiment analysis tool to provide sentiment scores for comments.

**Word Cloud Generation**: Generates word clouds to visualize the most frequent words in the comments.

**React Frontend with Vite**: Utilizes React.js for the frontend to provide an interactive user interface.

**Python Flask Backend**: Implements a Flask backend to handle API requests and perform sentiment analysis.

**Deployment on Google Cloud Platform:**
This application is deployed on Google Cloud Platform using serverless containers.


## Try app now ##
For the deployed, running version, visit [THIS PAGE](https://yt-comment-analyzer-kbyafchtdq-lm.a.run.app/)

## Getting Started ##


1. Clone the repository:

```bash
   git clone https://github.com/JaFi01/YT-comment-analyzer
```

2. Navigate to the project directory:
  ```bash
cd YouTube-Comment-Analyzer
```

3. Select branch local (which contains app running on localhost)
  ```bash
git fetch --all
git checkout local
```
4.  Install dependencies: 

```bash
cd client
npm install
cd ../server
pip install -r requirements.txt
```
5. Set up environment variables:

Create a `.env` file in the `server` directory and add the following variables:

```makefile
YT_API_KEY=your-youtube-api-key
OPENAI_API_KEY=your-openai-api-key
```
6. 1 Run the client aplication:
In terminal 1: client directory
```bash
npm run dev
```

6. 2 Run server aplication
```bash
python3 app.py
```
or
```bash
python app.py
```

7. Access the application:

Open your web browser and navigate to `http://localhost:5173` or other localhost providded by vite to access the **YouTube Comment Analyzer**.

## Usage ##
1. Enter the YouTube video URL in the provided input field.
2. Click the "Check sentiment" button to analyze the sentiment of comments under the specified video.
3. View the AI response, sentiment analysis results, highlighted comments, and word cloud generated for the video.

## License ##
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements ##

[OpenAI](https://openai.com/) for providing the GPT-3 model.

[NLTK](https://www.nltk.org/) for providing the VADER sentiment analysis tool.