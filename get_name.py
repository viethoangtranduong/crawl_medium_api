def get_name(test_str):

    # initializing punctuations string  
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~ '''
    
    # Removing punctuations in string 
    # Using loop + punctuation string 
    for ele in test_str:  
        if ele in punc:  
            test_str = test_str.replace(ele, "")  

    # printing result  
    return test_str