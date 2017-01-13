def five_most_common(phrases):
    letters_dict = {}

    for p in phrases:
        for c in p:
            if c not in letters_dict:
                letters_dict[c] = -1
            else:
                letters_dict[c] -= 1

    flattened = [(j, i) for i, j in letters_dict.items()]
    flattened.sort()
    top5 = [j[1] for j in flattened][:5]
    return top5


def rotate(letters, sec_id):
    rotations = sec_id % 26
    sentence = " ".join(letters)
    decrypted_sentence = ''
    for c in sentence:
        if c == ' ':
            decrypted_sentence += ' '
        else:
            new_ord = (ord(c) + rotations)
            if new_ord > 122:
                new_ord = new_ord % 122
                new_ord = 97 + new_ord
            decrypted_sentence += chr(new_ord)
    return decrypted_sentence


def parse_encrypted(s):
    sum_sector_ids = 0
    tmp = s.split('-')
    letters = tmp[:-1]
    sec_id, checksum = tmp[-1][:-1].split('[')
    top5 = "".join(five_most_common(letters))
    if top5 == checksum:
        return letters, int(sec_id)
    else:
        return '', 0
