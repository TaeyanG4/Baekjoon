import base64
string = input()
string_bytes = string.encode('utf-8')
encoded_bytes = base64.b64encode(string_bytes)
encoded_string = encoded_bytes.decode('utf-8')
print(encoded_string)