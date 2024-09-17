def asc(s):
    int_list = [int(x) for x in s] 
    result = []
    
    while int_list:
        min_int = min(int_list)
        
        result.append(str(min_int))
        
        int_list.remove(min_int)
    
    return result

print(asc(['1231', '2131231' , '312','12353456','23']))