<style>
code, pre {
  font-size: 0.9rem;
}
</style>

# Basic While Loop

## Learning
A **while loop** allows your code to repeat an action as long as a condition is `True`.  
It’s great for running a block of code multiple times without having to write it out again.

Here’s a simple example:

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

This will print:

```
1
2
3
```

The loop keeps running while `count <= 3`.  
Each time it runs, it prints the number and then increases `count` by 1.  
Once `count` becomes 4, the condition is no longer true, and the loop stops.

---

## Your Task
Create a **while loop** that prints the numbers **1 through 5**, each on a new line.

### Steps
1. Start with a variable called `number` and set it to `1`.
2. Write a `while` loop that runs while `number` is less than or equal to `5`.
3. Inside the loop, print the current value of `number`.
4. Increase `number` by 1 each time the loop runs.

When done correctly, your program should print:

```
1
2
3
4
5
```

---

✅ **Tip:** Make sure your loop will eventually stop!  
If you forget to update the variable inside the loop, it will run forever.
