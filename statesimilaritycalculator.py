from difflib import SequenceMatcher

def calculate_string_similarity(str1, str2):
    return SequenceMatcher(None, str1, str2).ratio()

state1 = "running"
state2 = "runing"
similarity_score = calculate_string_similarity(state1, state2)
print(f"The similarity between '{state1}' and '{state2}' is: {similarity_score}")

state3 = "idle"
state4 = "stopped"
similarity_score2 = calculate_string_similarity(state3, state4)
print(f"The similarity between '{state3}' and '{state4}' is: {similarity_score2}")  
