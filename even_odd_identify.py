import random

# declare for randomlist
randomlist = []
# declare for loopstate
loopstate = []

# function to create the number list
def even_odd_create(arg1):
    # create random number
    randomlist = random.sample(range(0,1000), arg1)
    # then print it out the screen
    even_odd_print(randomlist)
    # then return the value
    return randomlist

# function to print out the number list
def even_odd_print(arg2):
    print ('this is the number list:', arg2)

# main function
def main():
    # declare value for step_num
    step_num = 0
    # pass the value to even_odd_create function
    loopstate = even_odd_create(10)
    # main loop
    for num in loopstate:
        # increase step_num by 1
        step_num += 1
        # condition for even
        if (num % 2) == 0: 
            print (f'step number {step_num} : {num} is an even number')
        # condition for odd
        else:
            print (f'step number {step_num} : {num} is an odd number')

# call main function
if __name__ == "__main__":
    main()