# s1 = 'hello'

# number  =  732

# s2 = str(number)

# print(type(s1))
# print(type(s2))

# s3  = s1 +' '+ s2

# print(s3)

# print ('------------------')    

# print(s3 * 3)


# print ('------------------')
# print(s3[0])


# if s1 in s3:
#     print('yes')
# else:
#     print('no')    


# sa = 'a'

# if sa in  'programming':
#     print('yes')
# else:
#     print('no')    

# str1 = 'python termit'    

# print(str1.index('o'))

# print(str1[3])
# print(str1[-2])

# print(str1[3:9])
# print("------------------")
# print(str1[::-1])


srt3 = 'PYthon hello world'

print(srt3.title())

print(srt3.capitalize())

print(srt3.upper())

print(srt3.lower())

print(srt3.isupper())

print(srt3.isdigit())

print("------------------")
srt4 = '456545676'
print(srt4.isdigit())
print(srt4.isalpha())
print("------------------")

strlist = ['python', 'java', 'c++', 'c#', 'c']

print('! '.join(strlist))

srt5 = 'python hello world'

print(srt5.replace('python', 'java'))

print(srt5.split())

print(srt5.split('l',1))

print(srt5.split('l',2))

str6 = srt5.split('o')

print(str6)


print('------------------')

str7 = "python hello world"
print(' '.join(str7))
print(str7.partition(' '))

print("------------------")

str8 = '*****python hello world*****'

print(str8.strip("*"))
print(str8.lstrip("*"))
print(str8.rstrip("*"))
print(str8.find('*'))
print(str8.rfind('*'))

print(str8.count('*'))

print(str8.endswith('*'))
print(str8.startswith('*'))
print(str8.find('-'))


print('------------------')

str9 = 'python hello world'

print(str9.replace(' ', '='))
print(str9.replace('o', '0', 1))

print(len(str9))
print(sorted(str9))
print(sorted(str9, reverse=True))


print('------------------')

sim = 'a'
print(ord(sim))

print(chr(97))

print("------------------")

str10 = 'python hello world, Java, c++, c#, c'

for i in str10:
    print(ord(i), end=' ')