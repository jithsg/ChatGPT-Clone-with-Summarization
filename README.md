# ChatGPT-Clone-with-Summarization

This repository contains the code for a Chat GPT Clone application, built using Python and Streamlit. The application simulates a conversation with an AI, leveraging OpenAI's GPT models. It's designed to be interactive, user-friendly, and easily customizable.

## Features

- **Interactive Chat Interface**: Users can input their questions or statements, and the AI will respond accordingly.
- **Conversation Summarization**: A feature to summarize the conversation.
- **API Key Protection**: Users can enter their OpenAI API key securely.
- **Streamlit Integration**: The application is built using Streamlit, making it easy to run and deploy as a web app.

## Installation

To run this application, you need to have Python installed on your system. If you haven't installed Python yet, download it from [python.org](https://www.python.org/downloads/).

1. **Clone the Repository**

   ```
   git clone https://github.com/your-username/chat-gpt-clone.git
   cd chat-gpt-clone
   ```
2. **Install Dependencies**

The application requires several dependencies, which can be installed using pip:
```
pip install openai streamlit dotenv langchain tiktoken
```

3. **Environment Variables**

The application uses an environment variable for the OpenAI API key. You can set this up by creating a .env file in the root directory and adding your OpenAI API key:

```
    OPENAI_API_KEY=your_api_key_here
```
Uncomment the load_dotenv() and related lines in the script to enable loading from the .env file.

4. **Usage**

To run the application, execute the following command in the terminal:

```
streamlit run app.py
```
Navigate to the local URL provided by Streamlit to interact with the application.
5. **How It Works**
- The application uses Streamlit for the web interface.
- OpenAI's GPT models are used to generate responses to user inputs.
- The langchain library is utilized to manage conversation flow and memory.
- Users can input their questions or statements in a text box, and the AI will respond in the chat interface.
- The conversation can be summarized by clicking the "Summarise the conversation" button.

6. **Customization**

You can customize the application by modifying the model_name in the getresponse function to use different versions of GPT models.

7. **Contributing**

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

8. **License**

This project is licensed under the MIT License - see the LICENSE file for details.

9. **Acknowledgements**
- OpenAI for the GPT models.
- Streamlit for the web app framework.
- LangChain for conversation management.
