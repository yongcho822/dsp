# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

[![Think Python](img/think_python.png)](http://www.greenteapress.com/thinkpython/)

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

Complete the following exercises to check your ability with Python.

These exercises are implemented with doctests, which are runnable tests inside docstrings. Fill in the function definitions. Correct solutions will make it possible to run (for example) `python -m doctest strings.py` with no messages about failures.

 * [Strings](python/strings.py)
 * [Lists](python/lists.py)


---

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Python lists and tuples are both methods to store (usually multiple) values, which can both be accessed via index. Tuples are characterized by `( )` and lists are characterized by `[ ]`. The key difference is that a tuple, once created, is immutable. The order and values are set, and cannot be changed. Because of this characteristic, only tuples can be used as dictionary keys - only immutable elements can be used as dictionary keys.

---


---

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Unlike tuples, both sets and lists are mutable objects. But sets are unordered and have unique/non-duplicate values. A list could be something like `items = ["arrow", "spear", "arrow", "arrow", "rock"]`. but a set would be `things = {"arrow", "spear", "arrow", "arrow", "rock"}` or you could do `set(items)` to convert the list into a set, which rids of duplicate items.
In terms of performance for finding an element and checking for its existence, sets are faster than lists - that's because sets are implemented using hash tables, so that when searching for existence, python knows the exact position to check for the value. For lists, python will look at every value in the list to check if it is that value - so performance gets even worse for longer lists.

---


---

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Python's `lambda` is a way to succinctly define a 'one-time use' function (acts as a 'throw-away' fuction). It also allows you to easily pass functions as a parameter.
Here's an example of a basic lambda function: 
`squared = lambda x: x**2`
This is a more succinct line than:
`def squared(x):`
   `return x**2`
Another example:
`def sort_last(tuples):`
    `print sorted(tuples, key = lambda x: x[-1])`
What the lambda function does here is, when iterating over items in `tuples`, it takes the item, and then returns the last indexed value within that item. That is then assigned to the `key` parameter, which is the parameter of the `sorted()` function that tells you what item to sort the object by.


---


---

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions work by generating and populating a list in 'one-line' code. The format is something like this:

"[`operation to be done` for `whatever you'd like to run the operation on` in `where the 'whatever' is from` if `if clause`]"

A more concrete example would be (generating a max length 5 list of multiples of two that are not divisible by 6) :

    example_list = [x*2 for x in range(5) if x*2/6. != 1]
    
An equivalent using the `filter()` function would be:

    example_filter = filter(lambda x:x/6. != 1, [x*2 for x in range(5)])
    
The `filter()` function is interesting in that it needs a function passed in that returns a boolean value and then picks from a greater list only the values that return the value of True (or 1). The restricting part, compared to list comps, is that the full list has to be passed in to the filter function first. It's use is more restricted in being able to just select values from a list, rather than making a list out of nowhere, like list comps. 

An equivalent using the `map()` function would be:

    example_map = map(lambda x: x*2, filter(lambda x: x*2/6. != 1, range(5)))
    
You'll notice that the `filter()` function had to be used in conjunction. That's because lambdas cannot clealy handle conditionals like ifs on their owns, making this unusable: 

`example_map = map(lambda x:x*2 if x*2/6. != 1 else None, range(5))` - you'd get [0, 2, 4, None, 8], which isn't what we want.

Maps apply a function to every element of the sequence, no exceptions. Because of this, `map()` sometimes requires extra help, like `filter()`, which takes away from its readability.

List comp is more-readable, comprehensive, and preferred to both functions unless there's a specific need for either. The `filter()` function is just different than the `map()` function if you want to narrow down and list and use booleans in doing so. `map()` just applies the function to the whole sequence.

Set comp example - the snytax/form is the same as list comp:

    exampleset = {x for x in range(2, 5)} -- this returns `set([2, 3, 4])`
    
Dict comp example:

    exampledict = {n: n**2 for n in range(5)}
    
    #the difference is the colon, which identifies it as directionary keys and values we're adding within the curly brackets. 


---


Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

```bash
./markov.py chains.txt 40
```

A possible output would be:

> show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.
