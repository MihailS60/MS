from module_fake_math import divide as m_fake
from module_true_math import divide as  m_true, f_1,s_2,f_3,s_4

print(f_1,s_2)
result1=m_fake(f_1,s_2)
print('module_fake',result1,'\n','_'*20)

print(f_3,s_4)
result2=m_fake(f_3,s_4)
print('module_fake',result2,'\n','_'*20)

print(f_1,s_2)
result3=m_true(f_1,s_2)
print('module_true',result3,'\n','_'*20)

print(f_3,s_4)
result4=m_true(f_3,s_4)
print('module_true',result4,'\n')
