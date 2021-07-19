def add(s):
     flag = 1
     sl = list(s)
     for i in range(len(s) - 1, -1, -1):
             if sl[i] == '0':
                     sl[i] = '1'
                     flag = 0
                     break
             else:
                     sl[i] = '0'
     if flag:
             return '1' + ''.join(sl)
     return ''.join(sl)


print(add('101'))