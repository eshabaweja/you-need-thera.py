import random
import my_module

for i in range(1,10):
    print(i*str(random.randint(0,i)))
    print(i*my_module.pi)
