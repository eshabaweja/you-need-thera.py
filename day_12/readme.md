## Scope
A variable is only available from inside the region it is created. This is called scope.

### Local Scope
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

### Block Scope
No, there is no language support for creating block scope.

The following constructs create scope:

```    
    module
    class
    function (incl. lambda)
    generator expression
    comprehensions (dict, set, list(in Python 3.x))
```

### Global Constant naming convention in python

There are certain rules we need to follow while naming a constant.
```
    Rule-1: Constant name in python should be **capitalized** always.
    Rule-2: If there are multiple words in your constant name then they should be separated by an underscore(_).
```

### Global Keyword
If you need to create a global variable, but are stuck in the local scope, you can use the `global` keyword.
The `global` keyword makes the variable global.

```python
def myfunc():
  global x
  x = 300

myfunc()

print(x) 
```