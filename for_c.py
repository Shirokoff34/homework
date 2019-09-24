lists = [1, 5, 3, 6, 9, 11, 12, 14, 8, 10]

for element in lists:
    print(element + 1)

print('----------------')

ex_st = input("Введите строку:")

list('ex_st')

for letter in "ex_st":
    print(ex_st) 

scoolboy_scores = [
    {'scool_class': '4a', 'scores': [3,4,5,2,5,4,1]},
    {'scool_class': '4b', 'scores': [2,2,2,5,2,3,2]},
    {'scool_class': '4c', 'scores': [5,5,5,5,5,5,5]},
    {'scool_class': '4d', 'scores': [4,2,1,4,5,1,2]}
]

sum_scool = 0
for score in scoolboy_scores['scores']:
    sum_scool += score
    print(sum_scool)
