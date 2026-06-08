Viewed helloworld.py:1-19

These are the four built-in "collections" in Python. They are all used to store multiple items in a single variable, but they have different rules and use cases. 

Here is a breakdown of how they differ:

### 1. List `[1, 2, 3]`
A List is like a standard array or an ordered checklist.
* **Syntax:** Uses square brackets `[]`
* **Ordered:** The items stay in the exact order you put them in.
* **Mutable (Changeable):** You can add, remove, or change items after creating it.
* **Duplicates:** Allows duplicate values (e.g., `[1, 2, 2, 3]`).
* **Use case:** When you need a simple collection of items where the order matters and you might want to modify it later (e.g., a list of usernames, a shopping list).

### 2. Tuple `(1, 2, 3)`
A Tuple is like a List, but it is locked and cannot be changed.
* **Syntax:** Uses parentheses `()`
* **Ordered:** The items stay in the exact order you put them in.
* **Immutable (Unchangeable):** Once you create a tuple, you **cannot** add, remove, or change items.
* **Duplicates:** Allows duplicate values.
* **Use case:** When you have data that should *never* change throughout your program (e.g., days of the week, coordinates like `(latitude, longitude)`). Because they are locked, they are slightly faster and more memory-efficient than lists.

### 3. Set `{1, 2, 3}`
A Set is a collection where order doesn't matter, and every item must be unique.
* **Syntax:** Uses curly braces `{}` with just values.
* **Unordered:** The items don't have a guaranteed order (you can't ask for "the first item" because there is no first item).
* **Mutable (Changeable):** You can add or remove items.
* **No Duplicates:** If you try to add a duplicate, it just ignores it (e.g., `{1, 2, 2, 3}` becomes `{1, 2, 3}`).
* **Use case:** When you only care *if* an item exists in the collection, or when you need to remove duplicates from a list (e.g., keeping track of unique website visitors).

### 4. Dictionary `{'name': 'Asabeneh'}`
A Dictionary stores data in "Key-Value" pairs, like a real-world dictionary (Word -> Definition).
* **Syntax:** Uses curly braces `{}` with `key: value` pairs.
* **Ordered:** (As of modern Python 3.7+), they remember the order items were inserted.
* **Mutable (Changeable):** You can add, remove, or change key-value pairs.
* **No Duplicate Keys:** You can have duplicate values, but the **keys** must be unique.
* **Use case:** When you need to label your data and look it up by that label (e.g., storing a user's profile where the keys are `'name'`, `'age'`, `'email'`).

### Summary Cheat Sheet:
| Collection | Brackets | Ordered? | Changeable? | Duplicates? | How it looks |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **List** | `[ ]` | Yes | Yes | Yes | `["apple", "banana"]` |
| **Tuple** | `( )` | Yes | No | Yes | `("apple", "banana")` |
| **Set** | `{ }` | No | Yes | **No** | `{"apple", "banana"}` |
| **Dictionary** | `{ }` | Yes | Yes | **No** (keys) | `{"fruit": "apple"}` |


Viewed helloworld.py:1-19

The difference between the two comes down to how they handle the leftovers of a division. 

If we divide 3 by 2 in standard math: `3 ÷ 2 = 1.5`
It can also be written as: `3 ÷ 2 = 1 with a remainder of 1`.

Here is how `%` and `//` handle this:

### 1. Modulus `%` (The Remainder)
The modulus operator gives you **only the remainder** after dividing the two numbers. 
* "How much is left over after dividing 3 by 2 as many whole times as possible?"
* 2 goes into 3 exactly 1 time, with **1** left over.
```python
print(3 % 2)  # Output: 1
```
**Common Use Case:** Modulus is used a lot in programming to check if a number is even or odd (e.g., `num % 2 == 0` means it's even, because there's no remainder).

### 2. Floor Division `//` (The Quotient)
The floor division operator gives you **only the whole number** of times the first number can be divided by the second, discarding any remainder or decimals. It rounds the result *down* to the nearest whole number (the "floor").
* "How many whole times does 2 go into 3?"
* 2 goes into 3 exactly **1** time.
```python
print(3 // 2)  # Output: 1
```

### Another Example to Make It Clearer
Let's try it with 10 and 3:
* **Standard Division (`/`):** `10 / 3 = 3.33333...`
* **Floor Division (`//`):** `10 // 3 = 3` (Because 3 goes into 10 exactly 3 whole times).
* **Modulus (`%`):** `10 % 3 = 1` (Because 3 * 3 = 9, and there is 1 left over to get to 10).


Great question! In Python, **everything is an object**, and a **class** is the blueprint that defines what an object is and what it can do.

Think of it like this:

| Analogy | Class | Object |
|---|---|---|
| Cookie cutter | The cutter shape | Each cookie made from it |
| Blueprint | House design | The actual house |
| Python | `int` | `10`, `42`, `99` |

When Python says `<class 'int'>`, it's telling you:

> "The value `10` was made from the **`int` blueprint**"

That's why `10` knows how to do math — the `int` class gave it those abilities.

### A simple example

```python
# These are all objects made from different classes:
10          # object made from class 'int'
3.14        # object made from class 'float'
"hello"     # object made from class 'str'
[1, 2, 3]   # object made from class 'list'
```

You can even make your **own** class:

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog("Buddy")   # object made from class 'Dog'
print(type(my_dog))      # <class 'Dog'>
my_dog.bark()            # Buddy says Woof!
```

### Key takeaway

A **class** = a template that defines a type of thing. An **object** = an actual thing created from that template. In Python, even basic types like `int`, `str`, and `list` are classes — which is why `type()` always says `<class '...'>`.

You'll dive deeper into classes later in your 30 days of Python journey — for now, just know that `<class 'int'>` simply means "this value is an integer." 🙂