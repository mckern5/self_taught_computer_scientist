def two_sum(a_list, target):
    a_dict={}
    for index, n in enumerate(a_list):
        rem=target-n
        if rem in a_dict:
            return index, a_dict[rem]
        else:
            a_dict[n]=index

a_list=[-1,4,7,2,3]
print(two_sum(a_list,5))