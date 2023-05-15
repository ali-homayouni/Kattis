num = 2466
num = str(num)
outcom = ''
_len = len(num)
i = 0
token = 'r5'
token_index = 0
while i < _len:
    count = 1
    pointer = i+1
    while pointer < _len and num[i] == num[pointer]:
        count += 1
        pointer += 1
    _token1 = token[token_index] if token_index < len(token) else ''
    _token2 = token[token_index+1] if token_index+1 < len(token) else ''
    outcom += str(count) + _token1 + num[i] + _token2
    i += count
    token_index += 2
print(outcom + token[token_index:]

