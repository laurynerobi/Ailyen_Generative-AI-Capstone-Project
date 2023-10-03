import openai  # Import OpenAI API
from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler  # Imports libraries for handling HTTP requests

openai.api_key = ""  # Personal OpenAI product key
openAIModelVersion = "gpt-3.5-turbo"  # GPT Version to use
messageHistory = []  # Global table to keep track of the message history between the user and the system

# Class that handles the requests by implementing the BaseHTTPRequestHandler class

class myRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)     # Reponse code
        self.wfile.write(bytes("<html><head><title>Title</title></head>", "utf-8"))     # Message that will be sent to the user (head and title of HTML page)
        self.wfile.write(bytes("<body><p>Hello world</p>", "utf-8"))                    # The body of the HTML
        self.wfile.write(bytes("</body></html>", "utf-8"))                              # The closing tags

# Function that runs the HTTP server on the specified port

def run(server_class=HTTPServer, handler_class=myRequestHandler):
    server_address = ('', 8000)                 # Will run the server on port 3500
    httpd = server_class(server_address, handler_class)     # Creates an instance of a HTTP server
    httpd.serve_forever()       # Starts the HTTP server


# Function that allows multiple user prompts, each wither their own response factoring message history
def multiMemoryPrompt():

    while input != "exit()":  # While the user input isn't the exit command
        promptMessage = input("Enter a prompt: ")  # User inputs message they would like to send
        promptInfo = {"role": "user", "content": promptMessage}  # Compile user role and message into a dictionary

        messageHistory.append(promptInfo)  # Add the prompt to the message history array

        promptResponseInfo = openai.ChatCompletion.create(model=openAIModelVersion, messages=messageHistory)  # Receive the latest prompt response given the message history
        promptReply = promptResponseInfo.choices[0].message.content  # Opens the first response choice and displays the message's content
        promptReplyInfo = {"role": "system", "content": promptReply}  # Compile system role and message into a dictionary

        messageHistory.append(promptReplyInfo)  # Add the prompt to the message history array

        # Print the response
        print("")
        print("Output: ")
        print(promptReply)


# Function that allows multiple user prompts, each wither their own response without message history
def multiNoMemoryPrompt():

    while input != "exit()":  # While the user input isn't the exit command
        promptMessage = input("Enter a prompt: ")  # User inputs message they would like to send
        promptInfo = {"role": "user", "content": promptMessage}  # Compile user role and message into a dictionary

        promptResponseInfo = openai.ChatCompletion.create(model=openAIModelVersion, messages=[promptInfo])  # Receive the latest prompt response given the message history
        promptReply = promptResponseInfo.choices[0].message.content  # Opens the first response choice and displays the message's content

        # Print the response
        print("")
        print("Output: ")
        print(promptReply)


# Function that allows a single user prompt and receives a single response with no history
def singleNoMemoryPrompt():

    promptRole = input("What is the role of this prompt? User, or System? ")  # User input that determines if the following prompt is a request to the system or a request of the system
    promptMessage = input("Enter the according prompt: ")  # User inputs message they would like to send
    promptInfo = {"role": promptRole, "content": promptMessage}  # Compile role and message into a dictionary

    promptResponseInfo = openai.ChatCompletion.create(model=openAIModelVersion, messages=[promptInfo])  # Receive the latest prompt response given the message history
    promptReply = promptResponseInfo.choices[0].message.content  # Opens the first response choice and displays the message's content

    # Print the response
    print("")
    print("Output: ")
    print(promptReply)


#singleNoMemoryPrompt()
#multiNoMemoryPrompt()
multiMemoryPrompt()
