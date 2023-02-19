inp=input('enter text: ').lower()
key=int(input('enter key: '))
alphabet = "abcdefghijklmnopqrstuvwxyz"
text=list(inp)
array=['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
       'o','p','q','r','s','t','u','v','w','x','y','z']
result =''
if key in range(1,26):
    array = array[+key:] + array[:+key]
    for letter in text:
        result += array[alphabet.find(letter)]
else:
    print('error key...')
print(result)
input()