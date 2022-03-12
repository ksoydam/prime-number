#!/usr/bin/env python
# coding: utf-8

# In[1]:


'this is a uppercase string'.upper()


# In[2]:


type(123)


# In[3]:


print('Hello!')


# In[29]:


ls1 = list(range(5, 11))

print(all(ls1))


# In[30]:


any(ls1)


# In[31]:


x = 5
callable(x)


# In[32]:


callable(print)


# In[33]:


callable(type)


# In[46]:


ls2 = ['a', 'b', 'c', 'd', 'e']


# In[47]:


ls1 = [10, 9, 8, 7, 6, 5]


# In[48]:


for i in zip(ls1, ls2):
    print(i)


# In[49]:


list(enumerate(ls1))


# In[50]:


list(zip(ls1, ls2))


# In[51]:


zip(ls1, ls2)


# In[53]:


listA = ["susan", "tom", False, 0, "0"]
filtered_list = filter(None, listA)

print("The filtered elements are : ")
for i in filtered_list:
     print(i)


# In[54]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# returns True if number is even
def check_even(number):
    if number % 2 == 0:
          return True  

    return False


# In[67]:


filtered_even = filter(check_even, numbers)
print(list(filtered_even))


# In[68]:


print(filtered_even)


# In[70]:


for i in filter(check_even, numbers):
    print(i)


# In[74]:


grocery = ["bread", "water", "olive"]
enum_grocery = enumerate(grocery)
enum_grocery_100 = enumerate(grocery, 101)
print(list(enum_grocery))
print(list(enum_grocery_100))


# In[83]:


numbers = [2.5, 30, 4, -15]
numbers_sum = sum(numbers)
print(numbers_sum)


# In[85]:


numbers_sum = sum(numbers, 20)
print(numbers_sum)


# In[90]:


strg = ['a', 'b', 'c']
strg_sum = sum(strg, 'a')
strg_sum


# In[99]:


print(round(12))
print(round(10.8))
print(round(3.665, 2))
print(round(3.675, 2))


# In[102]:


def sum_square(arg1, arg2):
    print(arg1**2 + arg2**2)


# In[103]:


sum_square(3,7)


# In[104]:


sum_square(4,8)


# In[105]:


sum_square(9, 21)


# In[109]:


def st_repeat(arg1, arg2):
    print(arg1 * arg2)


# In[110]:


st_repeat('a', 5)


# In[111]:


st_repeat(2, 3)


# In[113]:


def battery_low_warning():
    print('Battery Low!')


# In[114]:


battery_low_warning()


# In[117]:


def battery_manager(battery):
    if battery == 100:
        print('Battery Full!')
    elif battery >= 50:
        print('Battery medium charge')
    elif battery < 50 and battery > 10:
        battery_low_warning()
    else:
        print('Please charge your battery!')
        


# In[120]:


battery_manager(5)


# In[121]:


def add_2(arg1):
    return arg1 + 2  # gonna store the otput in the function (as variable)


# In[122]:


num = add_2(4) + 5
num


# In[125]:


def add_3(x):
    return add_2(x) + 1


# In[126]:


print(add_3(11))


# In[127]:


def what_is_print():
    print('I print things and return nothing!')

def what_is_return():
    return 'I return values and print nothing!'


# In[128]:


what_is_print()
what_is_return()


# In[129]:


print(type(what_is_print()))
print(type(what_is_return()))


# In[ ]:




