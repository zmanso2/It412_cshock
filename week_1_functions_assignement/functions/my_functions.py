def divideTwonumbers(passed_list):
   """ processes a list of numbers, and divides one number by the other """
   """ Square a number provided by user
    Arguments:
        passed_list {list of dictionaries} -- each dictionary has the format of {top_number : int, bottom_number: int}
    Returns:
        al ist of values obtained when we divide top number by bottom number for each dictionary
""""

    divide_results = []
    numbers_ok = True
    passed_number1 = 1
    passed_number2 = 1

    for divide_vals in passed_list:
        numbers_ok = True
        try:
            passed_number1 = int(divide_vals["top_number"])
        except:
            print("The first parameter is not an integer")
            numbers_ok = False
        try:
            passed_number2 = int (divide_vals["bottom_number"])
        except:
            print("The second parameter is not an integer")
            numbers_ok = False
        
        if numbers_ok:
            divide_results = passed_number1 / passed_number2
            divide_results.append(divide_results)
    
    return divide_results


def mulitplyTwonumbers(passed_list):
   """ processes a list of numbers, and multiplies one number by the other """
   """ Square a number provided by user
    Arguments:
        passed_list {list of dictionaries} -- each dictionary has the format of {top_number : int, bottom_number: int}
    Returns:
        al ist of values obtained when we multiply top number by bottom number for each dictionary
""""

    mulitply_results = []
    numbers_ok = True
    passed_number1 = 1
    passed_number2 = 1

    for mulitply_vals in passed_list:
        numbers_ok = True
        try:
            passed_number1 = int(mulitply_vals["top_number"])
        except:
            print("The first parameter is not an integer")
            numbers_ok = False
        try:
            passed_number2 = int (mulitply_vals["bottom_number"])
        except:
            print("The second parameter is not an integer")
            numbers_ok = False
        
        if numbers_ok:
            mulitply_results = passed_number1 * passed_number2
            mulitply_results.append(mulitply_results)
    
    return mulitply_results

