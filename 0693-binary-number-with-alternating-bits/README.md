# Difference between 'and' and '&' in Python
In python

`and` is a boolean operation.
https://docs.python.org/3/reference/expressions.html#boolean-operations

`&` is a bitwise operation.
https://docs.python.org/3/reference/expressions.html#binary-bitwise-operations

Example:
```python
print(1 & 3)
print(1 and 3)
```

Output:
```python
1
3
```


# Lazy evaluation

Example:
```python
print(0 and 3)
print(0 or 3)
print(1 and 3)
print(1 or 3)
```

Output:
```python
0
3
3
1
```
