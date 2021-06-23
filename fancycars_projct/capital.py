string = "how is the weather. we are doing well today. today i am well!"
string = string.capitalize()
string = string.replace(" i ", " I ")
print(string)
special_char = ['.','?','!']
for index in range(len(string)-1):
#     print(index, string[index])
    if string[index] in special_char:
        print(string[index])
        letterToChange = string[index+2].upper()
        print(letterToChange)
        before_spc = string[0:index+2]
        print(before_spc)
        after_spc = string[index+3:]
        print(after_spc)
        string = before_spc + letterToChange + after_spc
print(string)