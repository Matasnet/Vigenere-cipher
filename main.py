from decode import *
from encode import *
    
print('If you want encode press 1 if you want decode press 2')

input_number = int(input('Press 1 for encode 2 for decode >> '))

if input_number == 1:
    text = input('Now write text to encode >> ')
    code = input('Now write code they must be letters for encode >> ')
    result = encode(text.upper(), code.upper())
    print(result)
elif input_number == 2:
    print("Remember to decode your code must be the same what was used to encode !")
    text = input('Now write text to decode >> ')
    code = input('Now write code they must be letters for decode >> ')
    result = decode(text.upper(), code.upper())
    print(result)
else:
    print("Something wrong please try again !")