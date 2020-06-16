# the variable "args" is already defined

my_list = []
for arg in args:
    if arg.isnumeric():
        my_list.append(int(arg))

print(str(my_list))
