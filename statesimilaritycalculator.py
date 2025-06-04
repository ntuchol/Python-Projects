from difflib import SequenceMatcher

def calculate_string_similarity(str1, str2):
    """
    Calculates the similarity ratio between two strings.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        float: The similarity ratio between 0 and 1.
    """
    return SequenceMatcher(None, str1, str2).ratio()

# Example usage:
state1 = "running"
state2 = "runing"
similarity_score = calculate_string_similarity(state1, state2)
print(f"The similarity between '{state1}' and '{state2}' is: {similarity_score}")

state3 = "idle"
state4 = "stopped"
similarity_score2 = calculate_string_similarity(state3, state4)
print(f"The similarity between '{state3}' and '{state4}' is: {similarity_score2}")  