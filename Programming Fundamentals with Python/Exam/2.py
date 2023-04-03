import re

N = int(input())
for i in range(N):
    password = input()
    match = re.match(r'^(.+)>(\d{3}\|[a-z]{3}\|[A-Z]{3}\|[^<>]{3})<\1$', password)
    if match:
        uncrypted = ''.join(match.group(2).split('|'))
        print(f"Password: {uncrypted}")
    else:
        print("Try another password!")