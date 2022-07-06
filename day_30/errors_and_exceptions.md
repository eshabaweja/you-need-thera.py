# Errors and Exceptions

**Errors** are the problems in a program due to which the program will stop the execution. 

In computer programming, an **exception** is a special condition encountered during program execution that is unexpected or anomalous.

Two types of Error occurs in python. 

-  Syntax errors
-  Logical errors (Exceptions) 

```python
try:
    print("Something that might cause an exception.")

except:
    print("Do this if there WAS an exception.")

else:
    print("Do this if there were NO exceptions.")

finally:
    print("Execute this block of code NO MATTER WHAT HAPPENS.")

```

Generating your own exceptions:

```python
raise:
    print("Use the raise keyword + error name to generate your own.")
```

