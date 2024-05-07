# Functions in Python Cheatsheet

The following document contains everything you need to know about functions in Python. Instead of allowing 
overloading of functions and methods like Java or C#, Python allows different function signatures through optional 
parameters with a default value. You can even type hint in Python, to make it feel more like your favorite programming 
language.

## Defining Functions
```py
def function_name(parameters):
    """Documentation string"""
    # Function body
    return result
```

- def: Keyword used to define a function.
- function_name: Name of the function.
- parameters: Input parameters passed to the function.
- """Documentation string""": Optional docstring providing documentation for the function.
- return: Keyword used to return a value from the function.

## Calling Functions

```py
result = function_name(arguments)
```

- function_name: Name of the function to call.
- arguments: Values passed to the function as inputs.
- result: Return value of the function (if any).

Functions that do not return any value are also called **void** functions. They do not return anything, 
which means the value of `result` would be set to `None` in this case.

## Default Arguments

This is the option Python offers to use a function with different signatures. By assigning a default value, 
we make the passing of the information completely optional.

```py
def function_name(param1, param2=default_value):
    # Function body
```

- default_value: Default value assigned to the parameter if no argument is provided.

## Type hinting for optional values

Optional from the typing library helps us indicate that we may or may not receive a value.

```py
from typing import Optional

def function_name(param1: int, param2: Optional[list] = None):
    # Function body
```

Now we have a function with optional parameters that can also be `None`, with the default also set to `None`. 
This can be great for those functions where additional information is useful, but not strictly necesary.

## Variable Number of Arguments
```py
def function_name(*args):
    # args is a tuple containing variable number of positional arguments

def function_name(**kwargs):
    # kwargs is a dictionary containing variable number of keyword arguments
```

- *args: Allows passing variable number of positional arguments as a tuple.
- **kwargs: Allows passing variable number of keyword arguments as a dictionary. 

## Lambda Functions

```py
lambda arguments: expression
```

- lambda: Keyword used to define an anonymous function.
- arguments: Input arguments of the lambda function.
- expression: Single expression whose result is returned by the function. 

## Returning Multiple Values
 
```py 
def function_name():
    return value1, value2
```

Returns multiple values as a tuple. Tuples work a lot like lists, but can not be changed.

## Docstrings

```py
def function_name():
    """Documentation string"""
```

- Docstrings provide documentation for functions, modules, and classes.
- Enclosed in triple quotes (""" """) and placed immediately after the function definition.

## Function Annotations

```py
def function_name(param: annotation) -> return_annotation:
    # Function body
```

Annotations/type hints provide metadata about the types of function parameters and return values.
Optional and used for documentation purposes.

## Recursion

```py
def recursive_function():
    if base_case:
        return base_case_result
    else:
        return recursive_function(...)
```
        
- Recursion involves defining a function that calls itself.
- Requires a base case to prevent infinite recursion. 

## Function Scope

- Variables defined inside a function are scoped to that function.
- Variables defined outside any function have global scope.