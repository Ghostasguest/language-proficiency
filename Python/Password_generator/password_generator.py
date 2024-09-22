import random
import string

def reset_counter():
    global password, cap_count, small_count, special_char_count, nums_count
    cap_count = 0
    small_count = 0
    special_char_count = 0
    nums_count = 0
def generate_password(length):
    global cap_count, small_count, special_char_count, nums_count, args
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    special = string.punctuation
    digits = string.digits

    caps, small, special_chars, nums = args

    #no of true values
    count = 0

    # Create a list to store keys that need to be removed
    keys_to_remove = []

    duplicate = {}
    # Iterate over a snapshot of dictionary items
    for key, value in list(args.items()):
        if value == 1:
            duplicate[key] = value
            count += 1
        else:
            keys_to_remove.append(key)

    # Remove the keys after iteration
    for key in keys_to_remove:
        args.pop(key)



    def check_parameter_count(parameter):
        global args
        global cap_count, small_count, special_char_count, nums_count
        if parameter == caps:
            cap_count += 1
            if cap_count+1 > length/count:
                args.pop(caps)
                return -1
            return cap_count

        elif parameter == small:
            small_count += 1
            if small_count+1 > length/count:
                args.pop(small)
                return -1
            return small_count

        elif parameter == nums:
            nums_count += 1
            if nums_count+1 > length/count:
                args.pop(nums)
                return -1
            return nums_count

        elif parameter == special_chars:
            special_char_count += 1
            if special_char_count+1 > length/count:
                args.pop(special_chars)
                return -1
            return special_char_count

    global password
    password = []
    i=0
    while i < length:
        if len(args)== 0:
            args = duplicate
            cap_count = 0
            small_count = 0
            special_char_count = 0
            nums_count = 0

        param = random.choice(list(args.keys()))
        if check_parameter_count(param) != -1:
            if param == caps:
                password.append(random.choice(upper))

            elif param == small:
                password.append(random.choice(lower))

            elif param == special_chars:
                password.append(random.choice(special))

            elif param == nums:
                password.append(random.choice(digits))
        else:
            length+=1
        i+=1
    return password

#Enquiry
if __name__ == '__main__':
    global length, caps, small, special_chars, nums, args
    print("******** Welcome to Password Generator *********")

    print("Enter '0' for NO & '1' for YES")
    length = int(input("Length of the password? - "))
    caps = int(input("Capitals? - "))
    small = int(input("Small letters? - "))
    special_chars = int(input("Special characters? - "))
    nums = int(input("Numbers? - "))
    password = []
    cap_count = 0
    small_count = 0
    special_char_count = 0
    nums_count = 0

    password_generated = ''.join(generate_password(length))
    print("Your password is:\n\n", password_generated)

if __name__ != '__main__':
    length = 12
    caps = 1
    small = 1
    special_chars = 1
    nums = 1
    args = {
        'caps' : caps,
        'small' : small,
        'special_chars' : special_chars,
        'nums' : nums
    }

    password = []
    cap_count = 0
    small_count = 0
    special_char_count = 0
    nums_count = 0