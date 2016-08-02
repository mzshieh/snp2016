# 整數不是零都是真的
if (1):
    print('1 is a truthy value')
else:
    print('1 is a falsey value')

# 整數零是假的
if (0):
    print('0 is a truthy value')
else:
    print('0 is a falsey value')

# 不是零的浮點數，是真的。
if (1 / 10 ** 50):
    print('1 / 10 ** 50 is a truthy value')
else:
    print('1 / 10 ** 50 is a falsey value')

# 浮點數要是太靠近 0 會變成 0 ，也就是假的。
if (1 / 10 ** 500):
    print('1 / 10 ** 500 is a truthy value')
else:
    print('1 / 10 ** 500 is a falsey value')

# 空字串是假的
if (''):
    print('\'\' is a truthy value')
else:
    print('\'\' is a falsey value')

# 字串值是'空'則是真的
if ('empty'):
    print('\'empty\' is a truthy value')
else:
    print('\'empty\' is a falsey value')


# 有空再說
if (float('nan') == float('NaN')):
    print("float('nan') == float('NaN')")
if (float('nan') != float('NaN')):
    print("float('nan') != float('NaN')")

if (float('nan') == float('nan')):
    print("float('nan') == float('nan')")
if (float('nan') != float('nan')):
    print("float('nan') != float('nan')")
