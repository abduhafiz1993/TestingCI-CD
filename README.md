# Testing

## Assert


One of the simplest ways we can run tests in Python is by using the assert command. This command is followed by some expression that should be True. If the expression is True, nothing will happen, and if it is False, an exception will be thrown. Let’s look at how we could incorporate command to test the square function we wrote when first learning Python. When the function is written correctly, nothing happens as the assert is True


## Test-Driven Development


As you begin building larger projects, you may want to consider using test-driven development, a development style where every time you fix a bug, you add a test that checks for that bug to a growing set of tests that are run every time you make changes. This will help you to make sure that additional features you add to a project don’t interfere with your existing features.

Now, let’s look at a slightly more complex function, and think about how writing tests can help us to find errors. We’ll now write a function called is_prime that returns True if and only if its input is prime:


## Unit Testing


Even though we were able to run tests automatically using the above method, we still might want to avoid having to write out each of those tests. Thankfully, we can use the Python unittest library to make this process a little bit easier. Let’s take a look at what a testing program might look like for our is_prime function.


assertFalse(x) bool(x) is False

assertIs(a, b) a is b

assertIsNot(a, b) a is not b

assertIsNone(x) x is None

assertIsNotNone(x) x is not None

assertIn(a, b) a in b

assertNotIn(a, b) a not in b

assertIsInstance(a, b)  isinstance(a, b)

assertNotIsInstance(a, b) not isinstance(a,b)
