#built-in funcs can be used without importing module or configuring

# Built-in Functions
print(len('python'))
print(len([1,2,3,4,5]))
print(len({'name':'John','age':30}))

Some of the most commonly used Python built-in functions are the following: print(), len(), type(), int(), float(), str(), input(), list(), dict(), min(), max(), sum(), sorted(), open(), file(), help(), and dir().

In Python, the concept of an "object" is fundamental because **everything in Python is an object**. But what exactly does that mean?

### What is an object?

Conceptually, an object is a way to bundle **data** (state) and **behavior** (actions) together into a single, cohesive unit. 

You can think of an object as a digital representation of a real-world thing or a specific concept.
*   **Data (Attributes/Properties):** What the object *knows* or what it *is*. (e.g., A `Car` object might have data like `color="red"`, `speed=0`).
*   **Behavior (Methods):** What the object can *do*. (e.g., A `Car` object might have methods like `accelerate()`, `brake()`).

In Python, when you create a variable like `x = 5`, `x` isn't just a raw chunk of memory holding the number 5. It's an **integer object**. This object contains the data (the value 5) but also comes with built-in behavior (methods) that define how it can interact with other things (like how it adds itself to another number, or how it converts itself to a string).

### Why is it called an "object"?

The term "object" comes from **Object-Oriented Programming (OOP)**, a programming paradigm that organizes software design around data, or objects, rather than functions and logic.

It's called an "object" because it's treated as a distinct, tangible entity within your code—much like objects in the real world. Just as a physical object has characteristics (a ball is round, red, bouncy) and things you can do with it (you can throw it, catch it), a programming object has data attributes and methods.

### "Everything is an object" in Python

Unlike some other languages (like Java or C++) which have "primitive" data types (basic numbers or characters that aren't objects), Python takes the OOP concept to the extreme: **literally everything is an object.**

This includes:
*   **Numbers:** `5`, `3.14`
*   **Strings:** `"Hello"`
*   **Lists and Dictionaries:** `[1, 2, 3]`, `{"key": "value"}`
*   **Functions:** Even the functions you write are objects! You can pass them around like variables.
*   **Modules:** Imported files are objects.
*   **Classes themselves:** The blueprints you use to create objects are *also* objects.

### An example you can test

Because everything is an object, everything has built-in methods. For instance, you know a string is text, but as an object, it has behaviors attached to it:

```python
my_word = "hello"

# "hello" is a string object.
# Because it's an object, we can use its built-in method (behavior) .upper()
big_word = my_word.upper() 

print(big_word) # Outputs: HELLO
```

Even simple numbers are objects. If you have Python running in your terminal right now, you can try:

```python
x = 5
# You can check its type (what kind of object it is)
print(type(x))  # <class 'int'>

# You can even see the methods attached to the integer object '5'
print(dir(x)) 
```

In summary: An object is a container that holds both data and the specific actions that can be performed on that data. It's called an object because it mimics distinct entities, making code easier to organize, read, and model after real-world concepts.


Edited BuiltinFuncs.md
Viewed BuiltinFuncs.md:1-12

This error happens because of how the built-in `sum()` function is designed to work in Python.

### The Problem

When you call `sum(20, 30)`, you are passing two separate integer objects (`20` and `30`) to the function. 

However, the `sum()` function is not designed to take multiple numbers separated by commas. Instead, it expects its **first argument to be an "iterable"** — a collection of items that Python can loop over, like a list, a tuple, or a set.

When Python receives `sum(20, 30)`, it looks at the first argument (`20`) and tries to loop through it to add up the values inside. Since `20` is just a single integer (an `'int' object`) and not a collection of items, Python complains: **`TypeError: 'int' object is not iterable`** (meaning "I can't loop over a single integer!").

### How to fix it

**1. If you want to use `sum()`:**
You need to put your numbers inside an iterable, like a list `[]` or a tuple `()`.

```python
# Using a list
>>> sum([20, 30])
50

# Using a tuple
>>> sum((20, 30))
50
```

**2. If you just want to add two numbers:**
The standard addition operator (`+`) is the most Pythonic and efficient way to add individual numbers.

```python
>>> 20 + 30
50
```

*(Note: The `sum()` function actually accepts an optional second argument called `start`, which is what it thinks the `30` is in your original code. But it still needs the first argument to be a list/tuple!)*