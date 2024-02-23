# LISTS

The fundamental data structure in Python is the sequence. Each element, or item, within a sequence is allocated a number, referred to as its position or index. 
The item’s initial index is 0, followed by 1 for the second index, 2 for the third, and so on. Python encompasses six types of sequences, with the two most prevalent 
being lists and tuples. 

Tuples will be explored further in the next lesson in this module, Tuples and Dictionaries.

## Defining a list
a collection of values (items) separated by commas and enclosed within square brackets ([]). A crucial aspect of lists is that the items contained within them are not obligated to consist of the same data type.

EXAMPLE:

``` python
list1=[1,2.5,"hello", True]
list2=[2,1, 9, 5]
```
## Accessing and updating list
You can use slicing ([]) and range slicing ([:]) to access elements within a list.

You can modify the list items themselves. 

Additionally, list items can be accessed from the end by using its negative index, like strings, with -1 being the last item in the sequence, -2 being the second from last, and so on .

EXAMPLE:

``` python
ls1=[5,"RoboGarden", 20.2, 66, False]
print("ls1=", ls1) 
# ls1=[5,"RoboGarden", 20.2, 66, False]

print("ls1[0]=",ls1[0]) #access an item at index 
# ind 0 = 5

print("ls1[-2]=",ls1[-2]) #access an item at index -2 
# ind -2 = 66

print("ls1[1:3]=",ls1[1:3])  ## access a range of items at indices from 1 to 3 
# ls1[1:3]= ['RoboGarden', 20.2]

ls1[1]="Hello" ## update one item of the list
print("ls1=", ls1) 
# ls1= [5, 'Hello', 20.2, 66, False]

ls1[2:4]=[4,20] ## update multiple items of the list
print("ls1=", ls1)
# ls1= [5, 'Hello', 4, 20, False]
```
## Deleting list items
- Option 1: You can use the 'del statement' when you have the exact index number(s) of the element(s) you want to delete.
- Option 2: You can use utilize the remove() method if you don't know these indices of list element. 
        It is worth noting that the remove() function eliminates the initial matching element (provided as an argument) from the list.

EXAMPLE: 
``` python
ls=[2,19,3, "hello", 3, 9.2]
print("ls=", ls)
# ls= [2, 19, 3, 'hello', 3, 9.2]

del ls[1]  # delete the list item (19) at index 1 
print("ls=", ls)
# ls= [2, 3, 'hello', 3, 9.2]

ls.remove(3) # will remove the first matching number (3) from list
print("ls=", ls)
# ls= [2, 'hello', 3, 9.2]
```
## List operators
1. Concatenation (+)
EXAMPLE:
``` python
ls1=[2,7,8]
ls2=["hi","hello", "welcome"]
print("ls1+ls2:", ls1+ls2) # concatenation
# ls1+ls2: [2, 7, 8, 'hi', 'hello', 'welcome']
```
2. Repetition (*)
EXAMPLE:
``` python
ls1=[2,7,8]
ls2=["hi","hello", "welcome"]
print("ls1*3:", ls1*3) # repetition
# ls1*3: [2, 7, 8, 2, 7, 8, 2, 7, 8]
```
3. Membership operators (in & not in)
EXAMPLE:
``` python
ls1=[2,7,8]
ls2=["hi","hello", "welcome"]
print("7 in ls1:", 7 in ls1) # membership
# 7 in ls1: True
print('hi" not in ls2:', "hi" not in ls2) # membership
# "hi" not in ls2: False
```
## Built-in list methods
| Functions | Description |
| --------- | ------------|
| len(list)	| Returns the total length of the list.|
``` python
ls=[2,19,3, "hello", 3, 9.2]
print("ls=", ls)
# ls= [2, 19, 3, 'hello', 3, 9.2]
print("len(ls)=", len(ls)) # length of list
# len(ls)= 6
```
list.append(item) | Adds an additional item to the list.
```python
ls=[2,19,3, "hello", 3, 9.2]
ls.append(20)  #Adds an item to the list
print("ls=",ls)
# ls= [2, 19, 3, 'hello', 3, 9.2, 20]
```
max(list)	| Returns the maximum value of the list’s items.
```python
ls3=[2,8,2,11,1,7]
print("max(ls3)=", max(ls3)) # maximum value of the list
# max(ls3)= 11
```
min(list)	| Returns the minimum value of the list’s items.
```python
ls3=[2,8,2,11,1,7]
print("min(ls3)=", min(ls3)) # minimum value of the list
# min(ls3)= 1
```
List.count(item) | Outputs the count of how many times the object item occurs in the list.
```python
ls4=[1, 2, 15, 2, 7, 8, 11, 2]
print("ls4.count(2)=", ls4.count(2)) # Count how many times the object item 2 occurs in the list
# ls4.count(2)= 3
```
list.extend(seq)|	Adds the contents of the sequence (seq) to the end of the list.
```python
ls=[2,19,3, "hello", 3, 9.2]
ls2=["hi", "welcome"]
ls.extend(ls2) # Adds sequence to the list
print("ls=",ls)
# ls= [2, 19, 3, 'hello', 3, 9.2, 20, 'hi', 'welcome']
```
list.index(item)|	Returns the first index in the list where the (item) appears.
```python
ls3=[1, 2, 15, 2, 7, 8, 11]
print("ls3.index(15)=", ls3.index(15)) # get index
# ls3.index(15)= 2
```
list.insert(idx, itm) |	At a specific index (idx,) in the list, inserts an item (itm)
```python
ls3=[1, 2, 2, 7, 8, 11]
ls3.insert(2,15) # insert value at a specific index
print("ls3.insert(15,2):",ls3)
# ls3.insert(15,2): [1, 2, 15, 2, 7, 8, 11]
```
List.sort(key=[func], reverse=[True/False]|	Sorts list items in ascending order if the reverse argument equals False, and descending order if it equals True. This function can also sort list items with a specific function ([func]) assigned to a key argument.
```python
ls3=[2,8,2,11,1,7]
print("ls3.sort():", ls3) 
# ls3.sort(): [1, 2, 2, 7, 8, 11]
```
# DEFINING STRINGS
Strings are a list of characters (items) and can be treated as such. Enclosing characters within single, double, and triple quotes quotation marks creates strings

EXAMPLE
```python
a='Laura' #define string by utilizing single quote marks

b="really" #define string by utilizing double quote marks

c='''loves''' #define string by utilizing triple single quote marks

d= """food""" #define string by utilizing triple double quote marks 
```

## Accessing values in strings
Each character within a string is associated with an index number starting from 0. For example, if the string is "Laura," the index breakdown is like this:

| L | a | u | r | a |
| - | - | - | - | - |
| 0 | 1 | 2 | 3 | 4 |

The first letter of the string 'L' is indexed by 0, while the last letter, ‘a,’ is indexed by 4, which equals the total number of characters in the string minus one (5-1=4). 

To retrieve a particular substring from the string, "the colon operator (:)" and "square bracket ([])" are proposed, with the syntax as follows:

    Str[start:end] 
    where “start” is the first index of the desired substring, 
    “end” is the last index of the desired substring+1

EXAMPLE:

```python
var="Lauralovesfood" 

print("var[2]=", var[2]) 
# var[2]= u
print("var[4:6]=", var[4:6]) 
# var[4:6]= al
print("var[5:]=", var[5:]) # from the index 5 onward 
# var[4:]= lovesfood
```
### Negative indexing
In situations where an element near the end of the string needs identifying, it is possible to work in reverse by counting from the string's end, backwards.
|L |a |u |r |a |
|- |- |- |- |- |
|-5|-4|-3|-2|-1|

EXAMPLE:
```python
var="Lauralovesfood" 

print("var[-2]=", var[-2]) 
# var[-2]= o
print("var[-6:-4]=", var[-6:-4]) 
# var[-6:-4]= es
print("var[-4:]=", var[-4:]) # from the index 4 onward 
# var[-5:]= food
```

## Updating Strings
In Python programming language, strings are considered immutable (you cannot alter their individual characters directly).

However, it's possible to modify an existing string by assigning a variable with a new string. This new value can either be connected to the previous value or entirely distinct from it.
``` python
st1="hello everyone" 
st2="RoboGarden" 
st3="hi" 

## assign one string to another string 

st3=st2 

print("st2=", st2) 
print("st3=", st3) 

##change string with its previous content 

print("The original value of st1=",st1) 

st1=st1[0:3]+" Python" 
print("After modification: st1=",st1) 

## Try to change the entire content of the string 

st1[0]="f" 

print("st1=",st1)
```

## String operators
Python supports a range of string operators that can be used for manipulating strings. Some of these operators are outlined below:

1. Concatenate operator (+): This concatenates string values on either side of the operator.
``` python
st= "hello" 
st=st+" everyone" # concatenation operator 
print("st=",st) # st= hello everyone 
```
2. Repetition operator (*): This performs string repetition and concatenation of the number of times specified by the value on the right-hand side of the operator.
``` python
st= "hello" 
st2= st*3 # repetition operator 
print("st2=", st2) # st2= hello everyonehello everyonehello everyone 
```
3. Slice operator ([]): This retrieves a character from a string at the given index specified by the number inside the square brackets.
``` python
print("st2[1]=", st2[1]) # slice operator  
# st2[1]= e 
```
4. Range slice operator ([:]): This retrieves a substring from a string, as described before.
``` python
print("st2[0:4]=",st2[0:4]) # range slice operator 
# st2[0:4]= hell
```
5. Assignment operator (=): This assigns one string to another.
```python
st= "hello" # assignment operator 
print("st=",st) # st= hello 
```
6. Membership operator (in & not in): This checks if a character/substring does or does not exist in the string.
``` python
if "eve" in st2: # membership operator 
    print("'eve' exists in the st2:", st2)
```    
7. Escape sequence operator (\): The backslash (\) is used to represent certain whitespace characters, as such: 
    1. \t is a tab
        ```python
        print("hello\tworld")
        # hello   world
        ```
    2. \n means a new line
        ``` python
        print("hello \nworld") 
        # hello 
        # world
        ```
    3. \r is a carriage return
        ```python
        print("hello!!\rworld")
        # world!!
        ```
8. Formatting operator: This is described later in this section.
