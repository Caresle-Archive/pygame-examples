# Type hint examples

These are the same examples that in the others folders. But this include the type hints for each of them.

**Example of code without type hint**

```python
def main():
	text = 'Hi python'
	print(text)
```

**Example of code with type hint:**

```python
def main() -> None:
	text: str = 'Hi python'
	print(text)
```