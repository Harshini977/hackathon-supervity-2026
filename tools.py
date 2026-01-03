import joblib

# Load the combined pipeline
try:
    model = joblib.load('financial_model.joblib')
except:
    print("Error: Run train.py first to generate financial_model.joblib")

def ml_sentiment_tool(text):
    prediction = model.predict([text])[0]
    return prediction.capitalize()

def llm_sentiment_tool(text):
    text = text.lower()
    
    # ALWAYS check negative words first
    negative_words = ['loss', 'decline', 'slowdown', 'risk', 'fell', 'dropped']
    positive_words = ['profit', 'gain', 'growth', 'increase', 'record', 'rise']
    
    if any(word in text for word in negative_words):
        return 'Negative'
    elif any(word in text for word in positive_words):
        return 'Positive'
    else:
        return 'Neutral'
