def single_root_words(root_w_,*other_words):
    same_words = []
    w_ = list(*other_words)
    for i in range(len(w_)):
        if ((w_[i]).lower()).find((root_w_).lower())!=-1:
            same_words.append(w_[i])

    return same_words

root_w=['rich','Able']
print('\n','________________','\n','заданы поисковые строки root_word',root_w)
words_=['rich','richiest','orichalcum','cheers','richies','Disablement','Able','Mable','Disable','Bagel']
print('\n','задан список words_',words_,'\n','________________')

result1=single_root_words(root_w[0],words_)
print('\n',f'совпадающие строки для "{root_w[0]}"  в списке {result1}')

result2=single_root_words(root_w[1],words_)
print('\n',f'совпадающие строки для "{root_w[1]}" без учета регистра в списке {result2}')
