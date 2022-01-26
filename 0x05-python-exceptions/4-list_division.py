#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    try:
        division_list = []
        for i in range(list_length):
            try:
                result = my_list_1[i] / my_list_2[i]
                division_list.append(result)
            except IndexError:
                print('out or range')
                raise
            except (ValueError, TypeError):
                print('wrong type')
                division_list.append(0)
                continue
            except ZeroDivisionError:
                print('division by 0')
                division_list.append(0)
                continue
    except IndexError:
        division_list.append(0)
    finally:
        return division_list
