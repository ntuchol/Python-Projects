subjects = []
for sentence in first_100_sentences:
    try:
        # Find the first NP before the verb
        np_start = None
        verb_index = None
        for i, (word, tag) in enumerate(sentence):
            if tag.startswith('VB'):  # Assuming verb tags start with VB
                verb_index = i
                break
            if tag.startswith('NN'):  # Assuming nouns are tagged with NN
                np_start = i
        if np_start is not None and verb_index is not None and np_start < verb_index:
            # Extract the subject (first NP)
            subject = ' '.join([word for word, tag in sentence[np_start:verb_index]])
            subjects.append(subject)
    except (IndexError, TypeError):
        pass  # Handle cases where parsing might fail