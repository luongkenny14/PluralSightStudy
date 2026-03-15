# Import libraries
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Set the endpoint url
endpoint_url = "https://klcogservice.cognitiveservices.azure.com/"

# This is your own subscription key .  We need to go to https://azure.microsoft.com/free/cognitive-services
# to create a free account subscription or pay as you go plan.  Once you done, copy the subscript key and paste it here
subscription_key = "xxxxxxxxxxxxxxxxxxxxxxx"

# this will create credential for access azure based on  our subscription key
credential = AzureKeyCredential(subscription_key)

# Create a text analytics client
client = TextAnalyticsClient(
    endpoint = endpoint_url,
    credential = credential)

testText = [
    "My goodness! setting prerequisite to run this program is not that fun!!!",
    "I love it, I was able to setup account and  run first Ai program",
    "I am relieved now"
]

# Analyze the sentiment of the documents
results = client.analyze_sentiment(
    documents = testText)

# Print the results
for result in results:
    print(f"Text sentence: {result.sentences[0].text}")
    print(f" - Sentiment Result: {result.sentiment}")
    print(f" - Positive Eval: {result.confidence_scores.positive:.1f}")
    print(f" - Neutral Eval: {result.confidence_scores.neutral:.1f}")
    print(f" - Negative Eval: {result.confidence_scores.negative:.1f}")
    print("")