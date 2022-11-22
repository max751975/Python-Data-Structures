def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    count_num1 = {}
    num1_str = str(num1)
    for i in num1_str:
        count_num1[i] = count_num1.get(i,0) + 1
    
    count_num2 = {}
    num2_str = str(num2)
    for i in num2_str:
        count_num2[i] = count_num2.get(i,0) + 1
    return count_num1 == count_num2
     