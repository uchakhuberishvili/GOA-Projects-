def smash(words):
    wordss = ""
    for i in words:
        wordss += i + " "
    return wordss[:-1]
print(smash(['hello', 'world', 'this', 'is', 'great']))
    

def square_sum(numbers):
    numbs = []
    Sum = 0
    for i in numbers:
        s = i * i
        numbs.append(s)
    for i in numbs:
        Sum += i
    return Sum
print(square_sum([2,5,3]))



def solution(string):
    return string[::-1]
print(solution("hello"))


def number_to_string(num):
    return str(num)
print(number_to_string(10))



def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return name + " plays banjo!"
    else:
        return name + " does not play banjo!"
print(are_you_playing_banjo("richard"))


def digitize(n):
    numbers = []
    n = str(n)
    for i in n:
        i = int(i)
        numbers.append(i)
    return numbers[::-1]
print(digitize(12546))


def find_smallest_int(arr):
    return min(arr)
print(find_smallest_int([12,54,67,34]))


def summation(num):
    Sum = 0
    n = 1
    while n != num + 1:
        Sum += n
        n += 1
    return Sum
print(summation(4))
    
def greet(name, owner):
    if name == owner:
        return("Hello boss")
    else:
        return("Hello guest")
print(greet("nika","nika"))

def repeat_str(repeat, string):
    return string * repeat
print(repeat_str(5,"Goa"))

def sum_array(a):
    Sum = 0
    for i in a:
        Sum += i
    return Sum
print(sum_array([-11,22,30]))    


def rps(p1, p2):
    if p1 == "rock" and p2 =="scissors":
        return "Player 1 won!"
    elif p1 == "scissors" and p2 == "rock":
        return "Player 2 won!"
    elif p1 == "rock" and p2 =="paper":
        return "Player 2 won!"
    elif p1 == "paper" and p2 =="rock":
        return "Player 1 won!"
    elif p1 == "paper" and p2 =="scissors":
        return "Player 2 won!"
    elif p1 == "scissors" and p2 =="paper":
        return "Player 1 won!"
    elif p1 == "rock" and p2 =="rock":
        return "Draw!"
    elif p1 == "scissors" and p2 =="scissors":
        return "Draw!"
    elif p1 == "paper" and p2 =="paper":
        return "Draw!"
print(rps("scissors","paper"))

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



def filter_list(l):
    nlist = []
    for i in l:
        if type(i) == int:
            nlist.append(i)
    return nlist
print(filter_list([12,56,234,"hello","good!"]))



def count_sheep(sheep_list):
    count = 0
    for sheep in sheep_list:
        if sheep:
            count += 1
    return count
sheep_array = [True,True,False,True,False,True,False,False,True,True]
print(count_sheep(sheep_array))


def maps(a):
    doubled = []
    for i in a:
        doubled.append(i * 2)
    return doubled

print(maps([23,45,12,54]))


def positive_sum(arr):
    Sum = 0
    for i in arr:
        if i > 0:
            Sum += i
    return Sum
print(positive_sum([-10,20,30,-15,123,45]))

def count_positives_sum_negatives(arr):
    List = []
    negatives = 0
    positives = 0
    for i in arr:
        if i >= 0:
            positives += 1
        elif i < 0:
            negatives += i
    return [positives,negatives]
print(count_positives_sum_negatives([1,3,2,3,4,-5,-10,-3,-123]))



def xo(s):
    s_lower = s.lower()
    count_x = s_lower.count("x")
    count_o = s_lower.count("o")
    return count_x == count_o

print(xo("xxoo"))

def remove_char(s):
    return s[1:-1]
print(remove_char("hello"))

def opposite(number):
    neg = 0
    pos = 0
    if number > 0:
        neg -= number * 2
    if number <0:
        pos += number * 2
    return [neg,pos]
print(opposite(20))

def make_negative(number):
    number = str(number)
    neg = "-" + number
    if "-" in number:
        return int(number)
    neg = int(neg)
    return neg
print(make_negative(20))

def validate_pin(pin):
    Leng = len(pin)
    if Leng == 4 or Leng == 6:
        return True
    else:
        return False
print(validate_pin("1234344"))

def solution(text, ending):
    if ending in text:
        return True
    elif ending not in text:
        return False
print(solution("brocode","code"))

def reverse_words(text):
    return text[::-1]
print(reverse_words("bro code"))


def get_grade(s1, s2, s3):
    if s1 >= 90:
        return "A"
    elif s2 >= 80:
        return "B"
    elif s3 >= 70:
        return "C"
    else:pass
print(get_grade(91,81,71))
    

def get_grade(s1,s2,s3):
    average_score = (s1 + s2 + s3) / 3

    if average_score >= 90:
        return 'A'
    elif average_score >= 80:
        return 'B'
    elif average_score >= 70:
        return 'C'
    elif average_score >= 60:
        return 'D'
    else:
        return 'F'


print(get_grade(85, 90, 88))  
print(get_grade(70, 65, 72))  
print(get_grade(55, 60, 58)) 


def square_digits(num):
    squared = []
    answer = []
    for i in str(num):
        squared.append(int(i) * int(i))
    for i in squared:
        answer.append(str(i))
    return int(''.join(answer))
print(square_digits(998))

def greet(name):
    return "Hello, " + name + " how are you doing today?"
print(greet("ucha"))
    
def multiple(x):
    if x % 3 == 0 and x % 5 == 0:
        return "BangBoom"
    elif x % 3 == 0:
        return "Bang"
    elif x % 5 == 0:
        return "Boom"
    else:
        return "Miss"
print(multiple(105))  

def find_needle(haystack):
    index = haystack.index("needle")
    for i in haystack:
        if i == "needle":
            i = len(i)
            return "found the needle at position " + str(index)
print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))


def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"
print(bool_to_word(10.5))

def count_by(x, n):
    multipled = x * n
    List = []
    BetterList = []
    for i in range(0,multipled + 1,x):
        List.append(i)
    for i in List:
        if i != 0:
            BetterList.append(i)
    return BetterList
print(count_by(2,5))

def invert(lst):
    inverted_lst = []
    for i in lst:
        inverted_lst.append(i * -1)
    return inverted_lst
print(invert(([10,-10,5,20,-60])))

def sum_mix(arr):
    lst = []
    for i in arr:
        lst.append(int(i))
    return sum(lst)
print(sum_mix([10,20,"20"]))

def remove_every_other(my_list):
    removed = []
    for i in range(0,len(my_list),2):
        removed.append(my_list[i])
    return removed
print(remove_every_other(["hi","bye","hi","bye"]))


def find_average(numbers):
    if numbers:
        return sum(numbers) / len(numbers)
    elif numbers ==0:
        return 0
    elif numbers == []:
        return 0
print(find_average([20,30]))


def fake_bin(x):
    numbers = ("")
    for i in x:
        if int(i) <5:
            numbers += "0"
        elif int(i) >=5:
            numbers += "1"
    return numbers
print(fake_bin(["1","4","10","20"]))

def litres(time):
    wph = 0.5
    total = wph * time
    return int(total)
print(litres(10))

def count_sheep(n):
    text = ""
    for i in range(1,n+1):
        text += (str(i) + " sheep...")
    return text
print(count_sheep(15))

def string_to_number(s):
    return int(s)
print(string_to_number("10"))

def generate_hashtag(s):
    result = "#"
    if s == "":
        return False
    s = s.title()
    for i in s:
        if i != " ":
            result += i
    Len = len(result)
    if Len <= 140:
        return result
    else:
        return False

print(generate_hashtag("hello my name is cristiano ronaldo!"))

def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

print(digital_root(122))

def if_chuck_says_so():
    return 1 > 2

def two_oldest_ages(ages):
    Sort = sorted(ages)
    Len = Sort[-1,-2]
    return Len

def two_oldest_ages(ages):
    sorted_ages = sorted(ages)
    oldest_ages = sorted_ages[-2:]
    return oldest_ages

def sort_array(source_array):
    even = []
    odd = []
    final = []
    for i in source_array:
        if i % 2 ==0:
            even.append(i)
        if i % 2 !=0:
            odd.append(i)
    odd = sorted(odd)
    for i in range(0,len(source_array)+1):
        final.append(even)
        final.append(odd)
    return final
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
reverse_words

def solution(number):
    if number < 0:
        return 0
    total_sum = 0
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            total_sum += num
    
    return total_sum
print(solution(10)) 

def square(n):
    if n == str:
        return 0
    return n * n

def billboard(name, price=30):
    total_price = 0
    for i in name:
        total_price += price
    return total_price
print(billboard("ucha"))

def even_or_odd(number):
    if number % 2 ==0:
        return "Even"
    else:
        return "Odd"

def high_and_low(numbers):
    numbers = sorted(numbers)
    numberss = [numbers[0], numbers[-1]]
    return numberss

print(high_and_low([12, 23, 432, 54, 123, 43, 54]))

def sum_two_smallest_numbers(numbers):
    numbers = sorted(numbers)
    return numbers[0] + numbers[1]

def string_to_array(s):
    string = []
    for i in s:
        if i == " ":
            string.append(",")
        else:
            string.append(i)
    return string

def simple_multiplication(number) :
    if number % 2 ==0:
        return number * 8
    else:
        return number * 9
    

def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result
arr = [1, 2, 3, 4]
print(grow(arr))


def find_uniq(arr):
    result = ""
    l = arr[0]
    for i in arr:
        if i != l:
            result += str(i)
    return int(result)
print(find_uniq([1,1,1,1,3,1,1]))

def reverse_seq(n):
    result = []
    for i in range(n,0,-1):
        result.append(i)
    return result

def double_integer(i):
    return i * 2

def odd_or_even(arr):
    full = 0
    for i in arr:
        full += i
    if full % 2 == 0:
        return "even"
    else:
        return "odd"
    
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

def sum_str(a, b):
    if b == '':
        return str(a)
    elif a == '':
        return str(b)
    elif int(a) + int(b) == 0:
        return '0'
    f = int(a) + int(b)
    return str(f)
print(sum_str("9",""))

def reverse_words(text):
    words_list = text.split(" ")
    reversed_words = []
    
    for word in words_list:
        reversed_words.append(word[::-1])
    
    return " ".join(reversed_words)
