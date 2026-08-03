from google import genai

client = genai.Client(
    api_key="YOUR_API_KEY",
    vertexai=False
)

print("Chatbot is ready! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=user_input
    )

    print("Chatbot:", response.text)