import requests
import os
with open('config.txt', 'wb') as file:
    file.write("hello world\n")
    file.write("00000101223")
                
with open('config.txt', 'r') as file:
    content = file.read()
    print(content)   