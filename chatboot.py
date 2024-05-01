import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import emoji

def download_vader_lexicon():
    try:
        nltk.download('vader_lexicon')
    except LookupError:
        nltk.download('vader_lexicon')

def initialize_sentiment_analyzer():
    return SentimentIntensityAnalyzer()

def analyze_sentiment(message, sid):
    sentiment_scores = sid.polarity_scores(message)
    compound_score = sentiment_scores['compound']
    
    if compound_score >= 0.05:
        return "positive"
    elif compound_score <= -0.05:
        return "negative"
    else:
        return "neutral"

def get_sentiment_emoji(sentiment):
    emoji_mapping = {
        "positive": "😃",
        "negative": "😔",
        "neutral": "😐"
    }
    return emoji_mapping.get(sentiment, "😐")

def chatbot():
    download_vader_lexicon()
    sid = initialize_sentiment_analyzer()
    
    print("Chatbot: Hello! How can I assist you today?")
    
    conversation_history = []
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        
        sentiment = analyze_sentiment(user_input, sid)
        sentiment_emoji = get_sentiment_emoji(sentiment)
        
        response = response_for_sentiment(sentiment, conversation_history)
        conversation_history.append((user_input, response))
        
        print(f"Chatbot {sentiment_emoji}: {response}")
        
        # Display conversation history
        print("\nConversation History:")
        for i, (input_text, response_text) in enumerate(conversation_history, start=1):
            print(f"{i}. You: {input_text}")
            print(f"   Chatbot: {response_text}\n")

def response_for_sentiment(sentiment, conversation_history):
    responses = {
        "positive": ["That's wonderful!", "Great to hear!", "Tell me more about it."],
        "negative": ["I'm sorry to hear that. Can I help in any way?", "I'm here to listen. What's bothering you?", "Let's talk about it."],
        "neutral": ["I understand. How can I assist you further?", "Is there anything else you'd like to discuss?", "Feel free to ask me anything."]
    }
    
    # Check the last user input to determine the context of the conversation
    if conversation_history:
        last_user_input, _ = conversation_history[-1]
        if "name" in last_user_input.lower():
            responses["neutral"].append("By the way, what's your name?")
    
    return random.choice(responses.get(sentiment, ["I'm not sure how to respond to that."]))

if __name__ == "__main__":
    chatbot()
