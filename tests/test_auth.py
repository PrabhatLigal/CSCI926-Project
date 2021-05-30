from notebook import auth
import string
import random

def unique_strings(k: int, ntokens: int,
               pool: str=string.ascii_letters) -> set:
    """Generate a set of unique string tokens.

    k: Length of each token
    ntokens: Number of tokens
    pool: Iterable of characters to choose from

    For a highly optimized version:
    https://stackoverflow.com/a/48421303/7954504
    """

    seen = set()

    # An optimization for tightly-bound loops:
    # Bind these methods outside of a loop
    join = ''.join
    add = seen.add

    while len(seen) < ntokens:
        token = join(random.choices(pool, k=k))
        add(token)
    return seen

def test_hash_argon2():
    
    passwords = unique_strings(k=100, ntokens=8)
    for password in passwords:
        hash = auth.passwd(password)
        assert auth.security.passwd_check(hash, password)


def test_hash_sha():
    passwords = unique_strings(k=100, ntokens=8)
    for password in passwords:
        hash = auth.passwd(password,"SHA1")
        assert auth.security.passwd_check(hash, password)

def test_hash_sha256():
    passwords = unique_strings(k=100, ntokens=8)
    for password in passwords:
        hash = auth.passwd(password,"SHA256")
        assert auth.security.passwd_check(hash, password)
