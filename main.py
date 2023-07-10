# Import the necessary modules from Flask and OpenAI
from flask import Flask, request, render_template
import openai

# Provide a instance for the Flask object. The argument __name__ helps Flask know where to look for resources, such as templates and static files.
app = Flask(__name__)

# Set the OpenAI API key. This is needed to make a call to the OpenAI API.
openai.api_key = "put your api key here"

# Define the route for the home page. This tells Flask what to display at the main URL of the web app.
@app.route("/")
def index():
    # Renders and returns the "index.html" template. This should be in your templates folder.
    return render_template("index.html")

# Define the route for the "/get" URL. This will handle the logic for generating responses to user input.
@app.route("/get")
def get_bot_response():
    # Get the 'msg' parameter value from the request URL. This should be the user's input text.
    userText = request.args.get('msg')

    # Create a prompt completion with OpenAI using the user's text. This generates a text response based on the user's input.
    response = openai.Completion.create(
        engine="text-davinci-003",  # The AI model we are using
        prompt=userText,  # The user's input text
        max_tokens=1024,  # The maximum length of the response
        n=1,  # Number of generated responses to return
        stop=None,  # Tokens at which generation will stop early
        temperature=1  # Controls randomness of the output. Higher values (closer to 1) means more random.
    )

    # Extract the generated text from the response object and convert it to string.
    answer = response["choices"][0]["text"]
    return str(answer)

# Checks if this script is being run directly. If so, start the Flask development server.
if __name__ == "__main__":
    app.run(port=5001)  # Start the app on port 5001
