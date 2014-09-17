#!/usr/bin/python
import sys

def get_number():
    ints = []
    nput = []
    for x in range(3):
        num = x + 1
        nput.append(float(input("Enter integer %d: " % num)))
    ints.append(nput)
    check_value = (float(input("Enter your check value")))
    ints.append(check_value) 
    return ints

def get_avg(ints_list):
    return sum(ints_list)/len(ints_list)

def get_max(ints_list):
    return max(ints_list)

def get_min(ints_list):
    return min(ints_list)       

def get_zones(check_value, avg_value, min_value, max_value):
    lower_mean = get_avg([avg_value, min_value])
    middle_mean = get_avg([avg_value, max_value])
   
    if check_value < min_value or check_value >= max_value:
        print 'Check value %f is out of bounds' % check_value
    else:
        if check_value < lower_mean:
            print 'Check value %f is in the lower region' % check_value 
        
        elif check_value < middle_mean:
            print 'Check value %f is in the middle region' % check_value 
        else:  
            print 'Check value %f is in the upper region' % check_value 
    
def main(num_list=None):
    if num_list:
        numbers = num_list
    else:
        numbers = get_number()
    number_list = numbers[0]
    check_value = numbers[1]
    max_value = get_max(number_list)
    min_value = get_min(number_list)
    avg_value = get_avg(number_list)

    print 'max value is %f' % max_value
    print 'min value is %f' % min_value
    print 'avg value is %f' % avg_value
    print 'The check value is %f ' % check_value
    
    get_zones(check_value, avg_value, min_value, max_value)

if __name__ == "__main__":
    val_list = []
    for line in sys.stdin:
        val_list.append(float(line))
    last_val = val_list.pop()
    num_list = [val_list, last_val] 
    main(num_list)
