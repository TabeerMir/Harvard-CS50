import argparse

parser = argparse.ArgumentParser(description = "meow like a cat") 
parser.add_argument("-n", default =1, help = "number of meows", type = int)
args = parser.parse_args()

for i in range(int(args.n)):
    print('meow')
