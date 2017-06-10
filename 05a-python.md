# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

> Tuples and lists are similar because they are constructs that store values. They are different because lists are mutable (values may be modified) while tuples are immutable. Only tuples will work as keys for dictionaries because only immutable elements can be used as dictionary keys.

--
-
### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

> Sets are similar to lists in that they are constructs to store values. However, there are differeces such as: sets can't contain duplicates, set's have mathematical functions available for comparison of 2 sets (union, intersect, difference, symmetric difference) which are not present in lists.

>> For example:  
    code:  
          my_list = ["Rafael", 22, "Isabella", 25, "Rafael", 22]  
    	  my_set = {"Rafael", 22, "Isabella", 25, "Rafael", 22}  
	  print (my_list)  
	  print (my_set)  	  
    output:  
            ['Rafael', 22, 'Isabella', 25, 'Rafael', 22]  
            {25, 'Rafael', 'Isabella', 22}  

> Moreover, when finding an element in a list we are able to make use of indexing which is not available for sets. For example, we are able to insert/delete values for a specific index of a list or find the corresponding index of a given value; for sets however, since indexing is not available we can make use of available functions such as add() / update() to add values & discard() / remove () to remove values.
---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is used when we want to perform functional programming. Lambdas are similar to functions but are useful for cases when we don't use them repeatedly since once they are used, they are destroyed immediately.

For example:
    code: my_list = [6,1,3,4,5,2]
          print (my_list)
	  print (sorted(my_list, key=lambda x: x%2==0))
    output: [6, 1, 3, 4, 5, 2]
            [1, 3, 5, 6, 4, 2]
    note: what is returned by lambda is [1,0,0,1,0,1]. sorted performs sorting on these returned values only once and thus why we expect the seen values on the second print. 

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are useful for quickly creating lists based on logic.

For example (list comprehension & corresponding map/filter):
    code: squared_to_10 = [x**2 for x in range(1,11)]
          print (squared_to_10)

	  values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	  squared_to_10_map = map(lambda x: x**2, values)
	  print (list(squared_to_10_map))

	  evens_to_10 = [x for x in range (1,11) if x%2==0]
	  print (evens_to_10)

	  evens_to_10_filter = filter(lambda x: x%2==0, values)
	  print (list(evens_to_10_filter))
    output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    	    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	    [2, 4, 6, 8, 10]
	    [2, 4, 6, 8, 10]

Upon comparison, I have found that list comprehension is able to quickly create lists based on logic similar to map and filter. However, map and filter introduce a new scope for defined variables and thusare less prone to bugs because variables are not silently overwritten unlike when list comprehension is used. An example of this potential bug is seen below:

For example:
    #case 1
    for x in values:
    	# x is not overwritten when lambda is used
    	squared_to_10_map = map(lambda x: x**2, values)

    #case 2
    for x in values
    	#x is silently overwritten thus prone to bugs
    	squared_to_10 = [x**2 for x in range(1,11)]

Moreover, we can also quickly create sets and dictionaries using comprehensions.

For example:
	code: my_set_comprehension = {x for x in range(0,11) if x%2 != 0}
	      print (my_set_comprehension)

	      my_dic_comprehension = {x : chr(65+x) for x in range(0,11)}
	      print (my_dic_comprehension)
	output:{1, 3, 5, 9, 7}
	       {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K'}


---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





