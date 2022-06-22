# Expression: Describes a computation and evaluates to a value
# Evaluate the expression and display the value

# What is a CS program
# We will use the programs to do manipulation of values
# Expressions in programs evaluate to the values
# These expressions can be represented by functions

from operator import add, mul
x = add(1,2) # add is the operator, and 2 and 3 are the operand
y = mul(3,5)
print(x)
print(y)

# How does the computer know which one to express first:
# 1. Evaluate the operator 2. Evaluate operands 3. Apply (There is nested call expression)

# ----
# Values Expression Objects and Data
{w for w in words if w == w[::-1] and len(w) >4}

