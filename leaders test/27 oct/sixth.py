# 6) Convert Pascal Case string into snake_case (4 ქულა)

# You will receive a string which will contain words in PascalCase, your job is to convert them into snake_case.

# Examples:
# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7 Test"        -->  "app7_test"
# 1                 -->  "1"

# def pascal(text):
#     res = ""
#     if text == int(text):
#         return str(text)
#     else:
#         for i in text:
#             if i == i.upper():
#                 res += "_"
#                 res += i.lower()
#             else:
#                 res += i
#         if res[0] == "_":
#             return res[1:]
# print(pascal(5))

def pascal_sec(text):
    if isinstance(text, int):
        return str(text)
    res = ""
    for index, char in enumerate(text):
        if char.isupper() and index != 0:
            res += "_"
        res += char.lower()
    return res
print(pascal_sec("TestController"))