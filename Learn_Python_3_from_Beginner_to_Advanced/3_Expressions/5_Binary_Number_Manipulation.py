
print(1 << 3)       # 8
# (x << y)          # is the same as multiplying x by 2**y
x = 1
y = 3
print(x * 2**y)     # 8


print(32 >> 5)      # 1
# (x << y)          # is the same as dividing x by 2**y
x = 32
y = 5
print(x / 2**y)     # 1.0


print(256 & 255)    # 0     Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0. [internet]
# 100000000         # 256
# 011111111         # 255
# 0000000000        # 0


print(256 | 255)    # 511   Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1. [internet]
# 100000000         # 256
# 011111111         # 255
# 111111111         # 511


print(~5)           # -6
# (~x)              # is the same as -x-1
# 101               # 5
print(-5-1)         # -6


print(60 ^ 13)      # 49    Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1. [internet]
# 00111100          # 60
# 00001101          # 13
# 00110001          # 49