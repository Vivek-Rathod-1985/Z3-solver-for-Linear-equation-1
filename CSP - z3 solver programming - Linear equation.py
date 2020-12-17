#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install z3-solver')


# In[2]:


from z3 import *
print(f"z3 version: {z3.get_version_string()}")


# In[3]:


X = Int('X')
print(f"X class name: {type(X)}")
print(f"X variable type: {X.sort()}")


# In[4]:


x, y, z = Reals('x y z')
print(f"y class name: {type(y)}")
print(f"y variable type: {y.sort()}")


# In[5]:


solver = Solver()
solver.add(2*x + 3*y == 5)
solver.add(y + 3*z > 3)
solver.add(x - 3*z <= 10)
print(f"A set of constraints has been added")


# In[6]:


solver.add(x > -5, x < 5)
solver.add(y > 0)


# In[7]:


print(f"Check solver satisfiability: {solver.check()}")


# In[8]:


print(f"Solver solutions: {solver.model()}")


# In[9]:


print("Access to individual variables:")
print(f"x value is: {solver.model()[x]}")
print(f"y value is: {solver.model()[y]}")
print(f"z value is: {solver.model()[z]}")


# In[ ]:




