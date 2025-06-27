import random

def doctor_bot():
    print("Hello! I'm Dr. Bot. How can I assist you today?")
    print("Please describe your symptoms or type 'exit' to end the conversation.")
    
    while True:
        user_input = input("\nYou: ").lower()
        
        if user_input == 'exit':
            print("Dr. Bot: Take care! If symptoms persist, please consult a real doctor. Goodbye!")
            break
        
        # Simple responses based on keywords
        if "fever" in user_input:
            print("Dr. Bot: It sounds like you might have a fever. Stay hydrated and rest. If it gets worse, see a doctor.")
        elif "headache" in user_input:
            print("Dr. Bot: Headaches can be caused by stress or dehydration. Try drinking water and resting.")
        elif "cough" in user_input:
            print("Dr. Bot: A cough could be a sign of a cold. Drink warm fluids and monitor your symptoms.")
        elif "stomach" in user_input:
            print("Dr. Bot: Stomach issues can be tricky. Avoid heavy meals and stay hydrated. If it persists, consult a doctor.")
        else:
            # Random generic responses
            responses = [
                "Dr. Bot: Hmm, that's interesting. Can you tell me more?",
                "Dr. Bot: I'm not sure about that. You might want to consult a healthcare professional.",
                "Dr. Bot: That sounds concerning. Please take care of yourself and monitor your symptoms."
            ]
            print(random.choice(responses))

# Run the chatbot
if __name__ == "__main__":
    doctor_bot()
