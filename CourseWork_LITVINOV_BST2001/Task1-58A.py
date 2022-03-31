

print("Enter a string with a length of at least 1 and no more than 100 letters!")
input_string = input("Enter a string to say hello - ")
base_string = "hello"

input_string = input_string.lower()

if len(input_string) > 100:
    print("\nYour string will be truncated because the character limit has been exceeded!")
    print("Now your line looks like - " + input_string[0:100])
elif len(input_string) < 1:
    print("Incorrect input!")
    quit()

def standart_search(s, sub):
    k = -1
    for i in range(len(s) - len(sub) + 1):
        success = True
        for j in range(len(sub)):
            if sub[j] != s[i + j]:
                success = False
                break

        if success:
            k = i
            break

    if k != -1:
        return "\nANSWER - YES"
    else:
        return "\nANSWER - NO"

print(standart_search(input_string,base_string))