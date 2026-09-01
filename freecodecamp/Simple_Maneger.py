tst ={
    'key':'value',
    'head': 'data'
}
def view(dic):
    for h in dic:
        k = str(h).capitalize()
        v = str(dic[h])
        print(f'{k} : {v}')

view(tst)