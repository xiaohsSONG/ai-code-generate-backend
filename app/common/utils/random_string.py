import random
import string

def random_string(length=8):
    """Generate a random string of fixed length."""
    all_string = list(string.ascii_letters)
    random.shuffle(all_string)
    return ''.join(all_string[:length])