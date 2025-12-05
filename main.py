# Basic star pattern
print("star pattern\n")
for i in range(1,6):
    for j in range(i):
        print("*" ,end="")
    print('\n')

# Inverted star pattern
print("inverted star pattern\n")
for i in range(6,1,-1):
    for j in range(i):
         print("*" ,end="")
    print('\n')     