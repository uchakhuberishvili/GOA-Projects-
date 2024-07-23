def make_upper_case(s):
    return s.upper()
print(make_upper_case("hello"))


def no_space(x):
    nospace = ""
    for i in x:
        if i != " ":
            nospace += i
    return nospace
print(no_space("Hello My Children!"))
