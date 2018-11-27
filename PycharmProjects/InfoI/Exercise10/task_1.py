from base64_encoder import encode_base64_str as encode
from base64_decoder import decode_base64_str as decode

def verify_encoding_decoding(string):
    encodedstr = encode(string)
    if string == decode(encodedstr):
        return True
    else:
        return False

if __name__ == '__main__':
    # verify_encoding_decoding should return True
    assert verify_encoding_decoding("Try out any test string here!")
