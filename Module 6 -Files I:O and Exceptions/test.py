def main(): 

    dictionary={"a": "apple", "b":"banana"} 

    key="c" 

    ## Type your code below 
    try:
        print(dictionary[key])
        return True
    except KeyError:
        return False
  

    ######### 

  

print(main()) 