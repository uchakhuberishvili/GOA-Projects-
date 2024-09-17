def advanced_sort(l: list, key: callable):
    return sorted(l, key=key, reverse=True)

def find_smallest_int(l: list):
    if not l:
        return None
    return min(l)

def validate_password(password: str):
    if len(password) < 8:
        return False
    if not any(char.islower() for char in password):
        return False
