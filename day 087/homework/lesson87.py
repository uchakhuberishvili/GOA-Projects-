def reverse_second(st):
    splited = st.split()
    splited = splited[::-1]
    return' '.join(splited)
print(reverse_second("hello world"))
    

x = ['111','2222222222222', '22','2222']
integer = []
string = []
for i in x:
    integer.append(int(i))
integer = sorted(integer)
for i in integer:
    i = str(i)
    string.append(i)
print(string)
