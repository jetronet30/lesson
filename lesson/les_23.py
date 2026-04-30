# binar

from pickle import *

import json

# with open('test.txt', 'wb') as f:
#     f.write(b'hello world')
# with open('test.txt', 'rb') as f:
#     print(f.read())

# with open('test.txt', 'wb') as f:
#     f.write(b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f')

# with open('test.txt', 'rb') as f:
#     print(type(f.read()))
#     print(f.read().decode())

# print('გამარჯობა'.encode('utf-8'))
# print('გამარჯობა'.encode('utf-16'))
# print('გამარჯობა'.encode('utf-32'))   

# with open('test.bin', 'wb') as f:
#     f.write(b'\xe1\x83\x92\xe1\x83\x90\xe1\x83\x9b\xe1\x83\x90\xe1\x83\xa0\xe1\x83\xaf\xe1\x83\x9d\xe1\x83\x91\xe1\x83\x90')

# with open('test.bin', 'rb') as f:   
#     print(f.read().decode('utf-8'))  


with open('pl.png', 'rb') as f:   
    res = f.read()
    fl_new = open('pl_new.png', 'wb')
    fl_new.write(res)
    fl_new.close()


with open('tast.bin', 'wb') as f:   
    dump("python", f)
    dump(123, f)
    dump(3.14, f)
    dump([1, 2, 3], f)
    dump({'a': 1, 'b': 2}, f)
    
with open('tast.bin', 'rb') as f:
    try:
        while True:
            print(load(f))
    except EOFError:
        pass


with open('data.json', 'wt', encoding='utf-8') as f:
    json.dump({'a': 1, 'b': 2}, f)

with open('data.json', 'rt', encoding='utf-8') as f:
    print(json.load(f))





