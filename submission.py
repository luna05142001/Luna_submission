#!/usr/bin/env python
# coding: utf-8

# In[1]:


def multiply_list(s):
    if not s:
        return 0
    str_list=s.split()
    int_list=list(map(int,str_list))
    product=1
    for num in int_list:
        product=product*num
        
    return product
input_str = "1 2 3 4"
result = multiply_list(input_str)
print(result)


# In[6]:


def count_common_chars(s):
    str_list=s.split()
    word1=list(str_list[0])
    word2=list(str_list[1])
    set1=set(word1) #set is the function  used to store collections of unique elements.
    set2=set(word2)
    common_char=set1&set2 # & is used to find the intersection of two sets.
    return len(common_char)


input_str = "green red"
result = count_common_chars(input_str)
print(result)
        
    


# In[19]:


def sum_divisible_by_k(N,K):
    if N<1:
        return -1
    if K==0:
        return -1
    number_list=list(range(1,N+1))
    subset_list=[]
    
    for i in number_list:
        if i%K==0:
            subset_list.append(i)
            
    sum_number=sum(subset_list)
    return sum_number

result = sum_divisible_by_k(5,2)
print(result)


# In[28]:


def highest_common_factor(number1,number2):
    factor1=[]
    factor2=[]
    for i in range(1,number1+1):
        if number1%i==0:
            factor1.append(i)
    for p in range(1,number2+1):
        if number2%p==0:
            factor2.append(p)
            
    set1=set(factor1)
    set2=set(factor2)
    common_factor=set1&set2
    return max(common_factor)

result = highest_common_factor(8,6)
print(result)            


# In[30]:


def get_minimum(list):
    set0=set(list)
    return min(set0)
result = get_minimum([2,2,3,4,5,7,10])
print(result)  


# In[31]:


import pandas as pd
def rename_col(dataframe,old_col_name,new_col_name):
    df=dataframe.rename(columns={old_col_name:new_col_name})
    return df


# In[41]:


import math
def standard_deviation(series):
    if len(series)==0:
        return 0
    mean=sum(series)/len(series)
    sum_num=0
    for i in series:
        num=(i-mean)**2
        sum_num=sum_num+num
    variance=sum_num/len(series)
    std_dev = math.sqrt(variance)
    return std_dev


# In[61]:


import numpy as np
import pandas as pd

def correlation_sum(string):
    str_list=string.split()
    if len(str_list)<9:
        return 0
    matrix=np.array(str_list).reshape(3,3)
    df=pd.DataFrame(matrix)
    return df


correlation_matrix=result.corr()
sum_of_correlation = correlation_matrix.values.sum()
sum_of_correlation_rounded = round(sum_of_correlation, 1)
sum_of_correlation_rounded
  

