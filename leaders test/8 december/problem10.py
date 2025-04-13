def edit_distance(str1, str2):
    len1, len2 = len(str1), len(str2)
    matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = 1 + min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])

    return matrix[len1][len2]

print(edit_distance("horse", "ros"))
print(edit_distance("intention", "execution"))
print(edit_distance("kitten", "sitting"))

#18:20 მოვრჩი გამიორმაგეთ მწვანე <3