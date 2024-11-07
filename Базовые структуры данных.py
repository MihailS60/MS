print('Входные данные')
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print('Оценки студентов:', grades)
Students_list = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print('Множество имен студентов:', Students_list)
print('\r ') # сброс строк
students=sorted(Students_list)
print('Сортировка имен студентов:',students,'Количество студентов:',len(Students_list))
s=[]
i=0
while i <len(Students_list):
    s.insert(i,(sum(grades[i]))/(len(grades[i])) )
    i +=1
print('Средние оценки:',s)
print('\r ') # сброс строк
# создание файла с оценками
print('Формируем структуру файла Имя + средний бал + перечень оценок :')
with open('marks.txt', 'w') as f_grades:
    j=0
    f_grades.write(str('/'))
    while j <len(Students_list):
        f_grades.write(str(students[j]+'/'))
        f_grades.write(str(s[j])+'/')
        f_grades.write(str(grades[j])+'/')
        j+=1
# открываем файл
with open('marks.txt', 'r') as f_grades:
    marks = f_grades.read()
    lenth=len(marks)
print('длинна полной строки со всеми параметрами',len(marks))
# вывод содержимого файла Имя+средний бал+перечень оценок
print('вывод содержимого файла Имя+средний бал+перечень оценок',marks)
k=0
num=0
num_1=0
# создаем структуру словаря
my_dict={}
my_dict_grades={}
while k < len(Students_list) :
    # находим смещение от начала ИМЯ
    num_1=marks.find('/',num+1,)
    # формирование строки ИМЯ
    name=marks[num+1:num_1]
    # находим среднее значение
    num=num_1
    num_1=(marks.find('/',num_1+1,))
    av_mark=(float)(marks[num+1:num_1]) # след символ после ' '
    av_mark=('{:.1f}'.format(av_mark)) # округление
    # формирование строки оценка: av_mark)
    # создаем словарь
    my_dict[name] =av_mark
# пропускаем третий элемент триады [список оценок]
    num = marks.find('/', num_1+1, )
    my_dict_grades[name] =grades[k]
    k += 1
    if k == len(Students_list):
            break
f_grades.close()
print('словарь ср балов',my_dict) # первый словарь
print('словарь оценок',my_dict_grades ) # второй словарь