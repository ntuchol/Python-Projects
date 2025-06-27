import re
import random

# Define a dictionary of patterns and responses
responses = {
    r"(?i)i need (.*)": [
        "Why do you need {0}?",
        "Would it really help you to get {0}?",
        "Are you sure you need {0}?"
    ],
    r"(?i)why don'?t you ([^\?]*)\??": [
        "Do you really think I don't {0}?",
        "Perhaps eventually I will {0}.",
        "Do you want me to {0}?"
    ],
    r"(?i)why can'?t i ([^\?]*)\??": [
        "Do you think you should be able to {0}?",
        "If you could {0}, what would you do?",
        "I don't know -- why can't you {0}?",
        "Have you really tried?"
    ],
    r"(?i)i can'?t (.*)": [
        "How do you know you can't {0}?",
        "Perhaps you could {0} if you tried.",
        "What would it take for you to {0}?"
    ],
    r"(?i)i am (.*)": [
        "Did you come to me because you are {0}?",
        "How long have you been {0}?",
        "How do you feel about being {0}?"
    ],
    r"(?i)i feel (.*)": [
        "Tell me more about these feelings.",
        "Do you often feel {0}?",
        "When do you usually feel {0}?",
        "When you feel {0}, what do you do?"
    ],
    r"(?i)hello|hi|hey": [
        "Hello! How can I help you today?",
        "Hi there! What’s on your mind?",
        "Hey! How are you feeling today?"
    ],
    r"(?i)quit": [
        "Goodbye! Take care.",
        "It was nice talking to you. Goodbye!",
        "See you next time. Take care!"
    ],
    r"(.*)": [
        "Can you elaborate on that?",
        "Why do you say that?",
        "How does that make you feel?",
        "What do you think about that?"
    ]
}

# Function to generate a response
def eliza_response(user_input):
    for pattern, responses_list in responses.items():
        match = re.match(pattern, user_input)
        if match:
            response = random.choice(responses_list)
            return response.format(*[g.strip() for g in match.groups()])
    return "I'm not sure I understand. Can you explain?"

# Main loop for interaction
if __name__ == "__main__":
    print("ELIZA: Hello! I'm here to help. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("ELIZA: Goodbye! Take care.")
            break
        print(f"ELIZA: {eliza_response(user_input)}")