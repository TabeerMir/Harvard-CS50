'''meows = 3

for i in range(meows):
    print("meow")'''

'''class Cat:
    MEOWS = 3 

    def meow(self):
        for i in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()'''

def meow(n: int) -> str:
    return "meow\n" * n #for i in range (n):
        #print("meow")

number: int = int(input("Number:"))
meows: str = meow(number)
print(meows, end="")