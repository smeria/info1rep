from base64 import urlsafe_b64encode

def encode_base64_str(string):
    string = string.encode('ascii')
    newstring = urlsafe_b64encode(string)
    return newstring