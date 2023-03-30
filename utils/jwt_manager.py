'''PyJWT is a Python library which allows you to encode and decode JSON Web Tokens (JWT). 
JWT is an open, industry-standard (RFC 7519) for representing claims securely between 
two parties.'''

from jwt import encode, decode

def create_token(data: dict) -> str:
    token: str = encode(payload=data, key="my_secret_key", algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    data: dict = decode(token, key="my_secret_key", algorithms=['HS256'])
    return data