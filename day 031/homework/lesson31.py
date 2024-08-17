def capitalize_names(names_list):
    formated_list = []
    for name in names_list:
        formated_list.append(name.capitalize())
    return formated_list

print(capitalize_names(["david", "chad", "gigachad"]))



def separate_evens_odds(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number // 2)
        else:
            result.append(number * 2)
    return result


print(separate_evens_odds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def find(Str):
    index = Str.find("n")
    if index % 2 == 0:
        return Str.upper()
    else:
        return Str.capitalize()

test_case = "ucha"
result = find(test_case)
print(result)