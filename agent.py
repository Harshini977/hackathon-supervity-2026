from tools import ml_sentiment_tool, llm_sentiment_tool

def agent_decide(text):
    ml_pred = ml_sentiment_tool(text)
    llm_pred = llm_sentiment_tool(text)

    if ml_pred == llm_pred:
        final = ml_pred
        reason = "ML and LLM agree"
    else:
        final = "Neutral"
        reason = f"ML predicted {ml_pred}, LLM predicted {llm_pred}, disagreement → marked Neutral"

    return final, reason

if __name__ == "__main__":
    while True:
        text = input("Enter financial news headline (or 'quit' to exit): ")
        if text.lower() == 'quit':
            break
        sentiment, explanation = agent_decide(text)
        print(f"Final Sentiment: {sentiment}")
        print(f"Reason: {explanation}")
        print("-"*50)
