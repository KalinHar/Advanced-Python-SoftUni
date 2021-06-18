text = input()
try:
    repeat = int(input())
    print(text*repeat)  #
except ValueError:
    print("Variable times must be an integer")
# except NameError:  #
#     pass
# else:  #
#     print(text * repeat)  #
# finally:  #
#     print("no matter what in except and else")
#