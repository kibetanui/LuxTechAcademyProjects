import random

num_char = 8
num_upper = 2
num_lower = 2
num_special = 2
num_digits = 2

upper_list = [chr(i) for i in range(65, 91)]
lower_list = [chr(i) for i in range(97, 123)]
special_list = [chr(i) for i in range(33, 47)]
special_list += [chr(i) for i in range(58, 65)]
special_list += [chr(i) for i in range(91,97)]
special_list += [chr(i) for i in range(123, 127)]
digits_list = [chr(i) for i in range(48, 57)]

def get_char(char_list, number):
    temp_list = []
    for i in range(number):
        temp_list.append(random.choice(char_list))
    return temp_list



upper_char = get_char(upper_list, num_upper)
lower_char = get_char(lower_list, num_lower)
digits_char = get_char(digits_list, num_digits)
special_char = get_char(special_list, num_special)

password_generated = upper_char + digits_char + lower_char + special_char
random.shuffle(password_generated)
password_generated = ''.join(password_generated)
print(password_generated)





