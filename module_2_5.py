def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return(matrix)


print('Исходные данные 1 :', 'result1=get_matrix(2,2,10)')
result1=get_matrix(2,2,10)
print('Вывод значений матрицы : ',result1)
print('\n')
print('Исходные данные 2 :', 'result2=get_matrix(3,5,42)')
result2=get_matrix(3,5,42)
print('Вывод значений матрицы : ',result2)
print('\n')
print('Исходные данные 3 :', 'result3=get_matrix(4,2,13)')
result3=get_matrix(4,2,13)
print('Вывод значений матрицы : ',result3)