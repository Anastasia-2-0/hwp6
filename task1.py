my_list = [1.1, 1.2, 3.1, 5, 10.01]
new_list = [round(i % 1, 2) for i in my_list if i % 1 != 0]
print(f'{my_list} = > {max(new_list) - min(new_list)}')