import google.generativeai  as genai

genai.configure(api_key = "AIzaSyAQ7uIqUNqz5rCmq9K0MP2zhX5fxNMLtoI")
model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("Explain black holes like I'm five.")

print(response.text)
