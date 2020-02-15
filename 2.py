position, _  = input().split()

dec = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

int_pos = dec.index(position[0]) + 1
integer_pos = int(position[1])
def predict_ch():
    res_list = []
    if int_pos - 2 >= 0 and integer_pos - 1 >= 0:
        res_list.append(dec[int_pos - 3] + str(integer_pos - 1))
    if int_pos - 1 >= 0 and integer_pos - 2 >= 0:
        res_list.append(dec[int_pos - 2] + str(integer_pos - 2))
    if int_pos + 1 <= 8 and integer_pos - 2 >= 0:
        res_list.append(dec[int_pos] + str(integer_pos - 2))
    if int_pos + 2 <= 8 and integer_pos - 1 >= 0:
        res_list.append(dec[int_pos + 2] + str(integer_pos - 1))
    if int_pos + 1 <= 8 and integer_pos + 2 <= 8:
        res_list.append(dec[int_pos + 1] + str(integer_pos + 2))
    if int_pos + 2 <= 8 and integer_pos + 1 <= 8:
        res_list.append(dec[int_pos + 2] + str(integer_pos + 1))
    if int_pos - 1 >= 0 and integer_pos + 2 <= 8:
        res_list.append(dec[int_pos - 2] + str(integer_pos + 2))
    if int_pos - 2 >= 0 and integer_pos + 1 <= 8:
        res_list.append(dec[int_pos - 3] + str(integer_pos + 1))
  
    return res_list

l = predict_ch()
my_l = [] 
figures = input().split()
for i in figures:
    if i in l: 
        my_l.append(i)
print(len(l) - len(my_l)) 
