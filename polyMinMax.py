#tests:
#x^2+2x+1
#x^2-2x+1
#4x^3+x^2-2x+1
#x^4+x^3-2x^2

import math as m
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application
transformations = (standard_transformations + (implicit_multiplication_application,))


x = Symbol('x')     #from sympy

#equ = raw_input("Equation: ")
equ = "x^4+x^3-2x^2"
equ = equ.replace('^', '**')
y = parse_expr(equ, transformations=transformations)    #from str to sympy equation type

yprime = y.diff(x)     #derivative of y
CPs = solve(yprime)     #solves for zeros, set them as a list of critical points

print '\n' + str(len(CPs))

CPs.sort()

#convert CPs from str to float
#for i in range(len(CPs)):
#    if str( type(CPs[i]) ) is not "<type 'complex'>":  
#    CPs[i] = float(CPs[i])
#    else:
#	print 'no cmplex pls'


#creates a dictionary
#keys are intervals
#values are testPoints

print CPs

testPoints = {}
testPoints["before " + str(CPs[0])] = CPs[0]-1

if len(CPs) > 1:
    for point in range(len(CPs)-1):
	 testPoints[str(CPs[point]) + ' through ' + 
str(CPs[point + 1])] = (CPs[point] + CPs[point + 1])/2

testPoints['after ' + str(CPs[len(CPs)-1])] = CPs[len(CPs)-1] + 1

#replaces x with CPs
for key in testPoints:
    yprime_str = str(yprime)    #sets yprime to str for further manipulation
    yprime_str = yprime_str.replace('x', str(testPoints[key]))    #replaces x with point
#    print yprime_str + '\n'    #print operation to be solved for

    ###########################################
    ####theres an error in sympy's exponent####
    ####using negative numbers in that even####
    ####  exponents do not make them pos   ####
    ###########################################
    
    yprime_str_split = yprime_str.split(' ')    #splits yprime by ' ' to handle individual operations
    for operation in yprime_str_split:
        if '-' and '**' in operation and not operation.startswith('-'):   #if the operation has an exponent and a negative number; control for negative coefficients
            if int(operation[operation.find( '**' )+ 2 ] ) % 2 is 0:    #if exponent is even, then the negative exponent changes signs
                yprime_str_split[ yprime_str_split.index( operation ) ] = operation.replace('-', '')    #removing the '-' makes exponent positive
        
    ###########################################
    
    yprime_str = str(yprime_str_split).replace('\'', '').replace('[', '').replace(']', '').replace(',','')  #"converting" yprime_str_split back into a str

                
    yprime_solve = parse_expr(yprime_str, transformations=transformations)   #converting yprime_str into a sympy equation

#moatylt a test for critical points
#    if yprime_solve < 0 and '.' in str(yprime_solve):     
#           if len(str(yprime_solve)[str(yprime_solve).index('.'):]) > 4 and yprime_solve < 0:     #control for large exponents that are literally 0
#                yprime_solve = 0
#

    if( yprime_solve < 0 ):
	testPoints[key] = 'dec'
    elif ( yprime_solve  > 0 ):
	testPoints[key] = 'inc'
	
print testPoints

    #find before and after the CPs to make find inc and dec intervals
