import time #for time function
import math #for floor function

# Get current time in seconds since the epoch

def time_clac(a):
    current_time = time.time()
    print("starting 9 lines from here is for debugging issues")
    print("\n")
    print("*****************************************************************")
    print("Current time in seconds since the epoch:", current_time)


    array_time =current_time
    print(array_time)
    floored=math.floor(array_time)
    decimal_term=array_time-floored
    if "." in str(decimal_term):
        zeros,dec_whole_term= (str(decimal_term)).split('.')
        print (zeros,dec_whole_term, "zeros and decimal terms")
    else:
        zeros,dec_whole_term=0,0
    print (floored, decimal_term, "floored values and decimal terms")



    #replacing a number in a random long number 
    addition=str(floored)+str(dec_whole_term)
    zero_rem=addition.replace("0", "1")
    length=len(zero_rem)
    div=int(dec_whole_term)//length
    div_rem=str(div).replace((a), "9")   #possible 4 cases from 1-4
    print(zero_rem,div_rem)



    #shorening number part
    summ=0
    for i in str(div_rem):       #to find sum of the string over each term which can be int
        summ += int(i)
    print(summ, "summing of div_rem ints")

    lengthofdiv=len(div_rem)
    midlen=lengthofdiv%2


    if midlen==0 & lengthofdiv>10:
        middleterm=div_rem[3:lengthofdiv//2+3]
    elif midlen==1 & lengthofdiv>10:
        middleterm=div_rem[3:lengthofdiv//2+2]
    elif lengthofdiv>5 & lengthofdiv<10:
        middleterm=div_rem[1:5]
    else:
        current_time=current_time+1
    print (middleterm, "middle term")



    #choosing part
    ftm= int(middleterm)+(summ*len(middleterm))
    ftmm=str(ftm)
    print("addition of mid with sum",ftm)
    if len(ftmm)>1:
        abcd=ftmm[0:1]
        addd=abcd.replace("0","1")
        addition_of_middleterm = addd+ftmm[1:int(a)+1]
        addition_of_middleterm
    fint=addition_of_middleterm[0:int(a)]
    fin_term=int(fint)
    final_term=str(fin_term)
    print("*****************************************************************")
    
    
    print("\n")
    print("\n")
    print("\n")
    print("\n")

    if len(final_term)!=int(a):
        while len(final_term)>int(a):
            fin_term= int(final_term)//10
        
        while len(final_term)<int(a):
            fin_term= int(final_term)*a
        return fin_term
    else:
        return final_term


a=(str(input("enter the number of digits required (upto 4)")))
if a.isnumeric():
    if (int(a) > 0) & (int(a) <5 ):         #for safety, failed in 2 test cases
        
        (print ("random number varies from 0 to 9999 for inputs 1,2,3,4" ))
        print("\n")
        print("\033[1m The random " + a + " digit number is  : \033[1m" + time_clac(str(a))) #  \033[1m is used to bold the letters in python

    elif  int(a)<= 0:
        print("enter numeric values except 0 and values should only be in range from 1 to 4.")

    else:
        print("values should only be in range from 1 to 4.  "+a+"  is not in range. ")
else:
    print("enter NUMBERES ONLY so, is ~~ " + a + " ~~  a number????")
