import hashlib

_cache = {}

def get(prompt):

    key = hashlib.sha256(prompt.encode()).hexdigest()

    return _cache.get(key)

def save(prompt,response):

    key = hashlib.sha256(prompt.encode()).hexdigest()

    _cache[key]=response