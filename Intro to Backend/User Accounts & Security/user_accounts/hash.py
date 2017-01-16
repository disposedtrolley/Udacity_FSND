import hmac
import hashlib
import string
import random

SECRET = "imsosecret"

def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()

def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))

def check_secure_val(h):
    val = h.split('|')[0]
    if h == make_secure_val(val):
        return val

def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

def make_pw_hash(name, pw):
    salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)

def valid_pw(name, pw, h):
    vals = h.split(',')
    salt = vals[1]
    hash = hashlib.sha256(name + pw + salt).hexdigest()
    hash_and_salt = "%s,%s" % (hash, salt)
    return hash_and_salt == h
