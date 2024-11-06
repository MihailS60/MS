def single_root_words(root_w_,*other_words):
    s_words=[]
    j = 0
    for i, v in enumerate(words_copy):
        if root_w_ in words_copy[i]:
            s_words.append([])
            s_words[j].append(words_[i])
            s_words[j].append(str(i))
            j += 1
    return s_words

def copy_low_str(str_l):
    # создание копии строки words_copy из words_
    str_copy = [' ']
    str_copy = str_copy + str_l
    str_copy.remove(' ')
    # перевод элементов str_copy в нижний регистр
    for k in range(len(str_l)):
            str_copy[k] = str_copy[k].lower()
    return str_copy


root_w=['rich','Able']
print('\n','________________','\n','заданы поисковые строки root_word',root_w)
words_=['rich','richiest','orichalcum','cheers','richies','Disablement','Able','Mable','Disable','Bagel']
print('\n','задан список root_word',words_)

words_copy=[]
root_w_copy=[]
same_words=[]

words_copy=copy_low_str(words_)  # создана копия заданного списка в нижнем регистре , не зависимая по размещению от words_
root_w_copy=copy_low_str(root_w)  # создана копия заданного списка поисковой строки в нижнем регистре , не зависимая по размещению от root_w


same_words=single_root_words(root_w_copy[0],words_,words_copy)
print('\n',f'совпадающие строки для "{root_w[0]}" и порядковый индекс в списке')
print (same_words)

same_words=single_root_words(root_w_copy[1],words_,words_copy)
print('\n',f'совпадающие строки для "{root_w[1]}" без учета регистра и порядковый индекс в списке')
print (same_words)