subjects = []
for sentence in first_100_sentences:
    try:
        np_start = None
        verb_index = None
        for i, (word, tag) in enumerate(sentence):
            if tag.startswith('VB'):  
                verb_index = i
                break
            if tag.startswith('NN'):  
                np_start = i
        if np_start is not None and verb_index is not None and np_start < verb_index:
            subject = ' '.join([word for word, tag in sentence[np_start:verb_index]])
            subjects.append(subject)
    except (IndexError, TypeError):
        pass  
