def generate_hashtag(string):
    if not string or string.isspace():
        return False

    hashtag = '#' + ''.join(word.capitalize() for word in string.split())

    return hashtag if len(hashtag) <= 140 else False
