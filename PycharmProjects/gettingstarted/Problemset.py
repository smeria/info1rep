"""Code to derive the derivative of the function f(teta)"""

import sympy
from sympy import symbols
theta = sympy.symbols('theta')
ybar= sympy.symbols('ybar')
ygeneral= ybar + theta/((1-theta)* sympy.log(1-theta)) #function
yprime = y.diff(theta) # deriving the derivative of the function
yprime
print "The derivative of the function f(theta) is: " \
      " f'(theta)= %.4f" %yprime

"""Code to derive the limits of the function f(theta). The function is defined in the range (-oo, 1)"""
from sympy import limit
from sympy import oo
f= theta/((1-theta)*sympy.log(1-theta))
limitminusinfinity = sympy.limit (f, theta, -oo)
limitone = sympy.limit (f, theta, 1,'-')
limitminusinfinity
print "If theta converges to -oo, the limit is: %s" %limitminusinfinity
limitone
print "If theta converges to one, the limit is: %s" %limitone

"""To proof that f(theta^*)=0 is unique, the function is plotted at a mean of ybar=1.474"""
import matplotlib.pyplot as plt
import numpy
import pylab
theta= numpy.linspace(-10,1,500) #This defines the lenght of the axis.
y= 1.474 + (theta/((1-theta)*numpy.log(1-theta))) #function with mean 1.474
plt.xlabel('theta') #label of the x axis
plt.ylabel('f(theta)') #label of the y axis
plt.grid(True)
pylab.plot(theta,y)

"""In the next section the generated data has to be read by the program and analyzed."""

import pandas
df = pandas.read_csv ('testdata.csv') #tell the program to read the file testdata.csv
statistics = df.describe()
print "The following chart shows the summary statistic form the data in testdata.csv:"
print statistics

"""The next section is about evaluating the function. Therefore the Newton-Raphson-Method is used.
Firstly the code has been written and evaluated with the data in testdata.csv. The variabl is
therefore denoted by x."""

import math
xnot= -3.9 #inital guess of x^*
epsilon = 0.00001
delta= 0.00001
ybar= 0.498 # mean of the data in testdata.csv
gnot= ybar + xnot/((1-xnot)*math.log(1-xnot))
diff= xnot
norm= math.fabs(gnot)
iguess=0
maxIter=100 # max. iterations
print "At guess %.4f for x^* the function is %4f. " %( xnot, gnot)
print "Guess\t xnot\t Func\t Slope\t xhat"
while ((norm > epsilon) & (diff > delta) & (iguess < maxIter)):
    gnot= ybar + xnot/((1-xnot) * math.log(1-xnot))
    hnot= xnot/((-xnot + 1)**2*numpy.log(-xnot + 1)) + xnot/((-xnot + 1)**2*numpy.log(-xnot + 1)**2) + 1/((xnot + 1)*numpy.log(-xnot + 1))
    xhat = thetanot- (gnot/hnot)
    print "%3d\t%.4f\t%.4f\t%.4f\t%.4f" %(iguess, thetanot, gnot, hnot, xhat) #in the following part the course of the iteration can be seen
    ghat= ybar+ xnot/((1-xnot) * numpy.log(1-xnot))
    diff= math.fabs(xhat - xnot)
    norm= math.fabs(ghat)
    thetanot= xhat
    iguess = iguess + 1 #this command counts the number of iterations
iguess = iguess - 1
print "\nThe estimate of x^* is %.4f." %xhat
print "At this value the function is %.4f" %ghat
print "%d iterations were used to calculate the estimate."%iguess

"""Another method of getting this solution is to use the command scipy.optimize.newton"""
import scipy
from scipy import optimize
def f(thetahat, ybary1):
    return ybary1 + (thetahat/ ((1-thetahat)*numpy.log(1-thetahat)))
thetahat0 = 0.5 # initial guess of thetahat that solves the function or zero
ybary1= 0.498
thetahat = scipy.optimize.newton(f, thetahat0, args= (ybary1,))
print "The program provides a estimate thetahat = %f" %thetahat

"""After verifying the script we can now go one with the data provided by the problemset. Firstly the mean of
the provided data has to be derived."""

Y = [1,2,3,4,5,6,7,8,9]
frequency = [700, 205, 50, 26, 10, 6, 1, 1, 1]
mean= numpy.average(Y, None, frequency, True)
print mean

"""Now that we have the mean, the script above is used again to get the solution requested."""

thetanot= 0.7 #inital guess of x^*
epsilon = 0.00001
delta= 0.00001
ybar= 1.474 # mean of the data in testdata.csv
gnot= ybar + thetanot/((1-thetanot)*math.log(1-thetanot))
diff= thetanot
norm= math.fabs(gnot)
iguess=0
maxIter=100 # max. iterations
print "At guess %.4f for theta^* the function is %4f. " %( thetanot, gnot)
print "Guess\t thetanot\t Func\t Slope\t thetahat"
while ((norm > epsilon) & (diff > delta) & (iguess < maxIter)):
    gnot= ybar + thetanot/((1-thetanot) * math.log(1-thetanot))
    hnot= thetanot/((-thetanot + 1)**2*numpy.log(-thetanot + 1)) + thetanot/((-thetanot + 1)**2*numpy.log(-thetanot + 1)**2) + 1/((-thetanot + 1)*numpy.log(-thetanot + 1))
    theta_hat = thetanot- (gnot/hnot)
    print "%3d\t%.4f\t%.4f\t%.4f\t%.4f" %(iguess, thetanot, gnot, hnot, theta_hat) #in the following part the course of the iteration can be seen
    ghat= ybar+ thetanot/((1-thetanot) * math.log(1-thetanot))
    diff= math.fabs(theta_hat - thetanot)
    norm= math.fabs(ghat)
    thetanot= theta_hat
    iguess = iguess + 1 #this command counts the number of iterations
iguess = iguess - 1
print "\nThe estimate of theta^* is %.4f." %theta_hat
print "At this value the function is %.4f" %ghat
print "%d iterations were used to calculate the estimate."%iguess





