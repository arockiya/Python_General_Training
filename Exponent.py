print (2**3)


def pow_func(base_num,pow_num):
    result=1
    for i in range(pow_num):
        result=result*base_num
    return result


print(pow_func(2,3))

print(pow_func(2,4))