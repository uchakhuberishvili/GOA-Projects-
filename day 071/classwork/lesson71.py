def cake_slice(n):
    return (n * (n + 1)) // 2 + 1

def fizz_buzz_cuckoo_clock(time_str):
    hour, minute = map(int, time_str.split(':'))
    if minute == 0:
        cuckoo_count = hour % 12
        cuckoo_count = 12 if cuckoo_count == 0 else cuckoo_count
        return ' '.join(['Cuckoo'] * cuckoo_count)
    elif minute == 30:
        return 'Cuckoo'
    if minute % 3 == 0 and minute % 5 == 0:
        return 'Fizz Buzz'
    elif minute % 3 == 0:
        return 'Fizz'
    elif minute % 5 == 0:
        return 'Buzz'
    else:
        return 'tick'
