name='Mihail'
print('Имя:',name, type(name))
age=64
print('Возраст:',age, type(age))
print('указатель на месторасположение в памяти age',id(age))
# новое значение age, добавление age_new
age=age + 10
print('указатель на новое месторасположение в памяти age',id(age))
print('Возраст измененный:',age, type(age))
is_student=True
print('логическое значение:',is_student, type(is_student))