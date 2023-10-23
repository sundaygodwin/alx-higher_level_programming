#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    newList = []
    initial = 0
    for i in range(0, list_length):
        try:
            initial = my_list_1[i] / my_list_2[i]
        except TypeError:
            initial = 0
            print("wrong type")
        except ZeroDivisionError:
            initial = 0
            print("division by 0")
        except IndexError:
            initial = 0
            print("out of range")
        finally:
            pass
        newList.append(initial)
    return newList
