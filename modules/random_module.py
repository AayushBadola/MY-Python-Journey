# modules are basically hepler packages containing some fucntions we can use ,
# so we dont have write them from scratch

# module to provide us random values 
import random 
rand_float = random.random() # floats between 0 -> 1

rand_int = random.randint(0,10) # takes a random value between 0->10 , can change the range

rand_decimal = random.uniform(1,10) # takes decimal value or integer value so , 1.4 , 5 , 9, 9.3..

rand_choice = random.choice([1,4,65,100]) # using list

rand_choice2 = random.choice((1,2,65,100)) # using tuple

# same can be done with strings

rand_choices = random.choices(["A","B","C"], k=2) 
# it chooses "2"  values at random and gives out a single result 
# it can give out [A,C] OR [B,A] .......[B,B] OR [A,A] ...


normal = random.normalvariate(mu=0, sigma=1)

# Normal Distribution (Bell Curve)
# μ = Mean
# σ = Standard Deviation
#
# Formula:
# f(x) = (1/(σ√(2π))) * e^(-(x-μ)^2/(2σ^2))
#
# Examples:
# Heights, IQ, Exam Scores


gaussian = random.gauss(mu=0, sigma=1)

# Gaussian Distribution
# Same idea as Normal Distribution
#
# Formula:
# f(x) = (1/(σ√(2π))) * e^(-(x-μ)^2/(2σ^2))
#
# Examples:
# Scientific Data, ML Datasets


binomial = random.binomialvariate(n=10, p=0.5)

# Binomial Distribution
# n = number of trials
# p = probability of success
#
# Formula:
# P(X=k)=C(n,k)p^k(1-p)^(n-k)
#
# Examples:
# Coin Tosses
# Pass/Fail Questions
# Defective Products


lognormal = random.lognormvariate(mu=0, sigma=1)

# Lognormal Distribution
#
# Formula:
# ln(X) ~ N(μ,σ²)
#
# Meaning:
# Logarithm of X follows a Normal Distribution
#
# Examples:
# Income
# Stock Prices
# Company Sizes


exponential = random.expovariate(lambd=1)

# Exponential Distribution
# λ = Rate Parameter
#
# Formula:
# f(x)=λe^(-λx)
#
# Examples:
# Waiting Time
# Customer Arrivals
# Server Requests


triangular = random.triangular(0,100,50)

# Triangular Distribution
#
# Parameters:
# low, high, mode
#
# Formula:
# Piecewise function
# (Usually not memorized)
#
# Examples:
# Project Estimates
# Risk Analysis


# =========================
# QUICK PSLP NOTES
# =========================

# Mean:
# μ = Σx / n

# Variance:
# σ² = Σ(x-μ)² / n

# Standard Deviation:
# σ = √Variance

# Z-Score:
# z = (x-μ)/σ