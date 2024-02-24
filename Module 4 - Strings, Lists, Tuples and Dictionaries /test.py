def main():  
    st="Kindly check your code. your code looks interesting"   

   # Extract the first two and last two characters
    st_out = st[:2] + st[-2:]
    print(st_out)

    #Repeating firt time
    st_out1 = st_out[:2] + st_out[-2]
    print (st_out1)

    #repeating 2nd time
    st_out2 = st_out1[:2] + st_out1[-2]
    print (st_out2)
    return (st_out2)
main() 