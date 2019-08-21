from numpy.testing import assert_allclose

def mean(num_list):
    return sum(num_list)/len(num_list)

def mean_assert(num_list):
    assert len(num_list) != 0
    return sum(num_list)/len(num_list)

def mean_exception_1(num_list):
    if len(num_list) == 0:
      raise Exception("The algebraic mean of an empty list is undefined. "
                      "Please provide a list of numbers")
    else:
      return sum(num_list)/len(num_list)

def mean_exception_2(num_list):
    try:
        return sum(num_list)/len(num_list)
    except ZeroDivisionError :
        return 0
    except TypeError as detail :
        msg = "The algebraic mean of an non-numerical list is undefined.\
               Please provide a list of numbers."
        raise TypeError(detail.__str__() + "\n" +  msg)

a=[1, 2, 3]
print mean_assert(a)
b=[7]
print mean_exception_1(b)
#c={"a":1, "b":2, "c":3}
c=[]
print mean_exception_2(c)

assert_allclose(2.01, 2, atol=0.03, rtol=0)
