import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator

import hashlib
import random
import string


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )


token_generator = TokenGenerator()


# simples gerador de key
def random_digits(size=5):
    chars = string.digits
    return ''.join(random.choice(chars) for x in range(size))


def random_letters(size=5):
    chars = string.digits
    return ''.join(random.choice(chars) for x in range(size))


def random_key(size=5):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for x in range(size))


def generate_hash_key_sha224_semi_random(salt, random_str_size=5):
    random_str = random_key(random_str_size)
    text = random_str + salt
    return hashlib.sha224(text.encode('utf8')).hexdigest()


def generate_hash_key_sha224_random(random_str_size=5):
    random_str = random_key(random_str_size)
    return hashlib.sha224(random_str.encode('utf8')).hexdigest()


def generate_hash_key_md5_random(random_str_size=5):
    random_str = random_key(random_str_size)
    return hashlib.md5(random_str.encode('utf8')).hexdigest()


def generate_hash_digits_random(random_str_size=5):
    random_str = random_digits(random_str_size)
    return random_str


def generate_hash_letter_random(random_str_size=5):
    random_str = random_letters(random_str_size)
    return random_str
###
