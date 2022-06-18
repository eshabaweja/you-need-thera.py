# Debugging
Grace Hopper found the first bug: an actual moth in the computer.

1. Recognize that a bug exists.
2. Isolate the source of the bug.
3. Identify the cause of the bug.
4. Determine a fix for the bug.
5. Apply the fix and test it.
6. Rinse. Repeat.
7. Take a break.
8. Ask a friend \<fresh set of eyes>.
9. Run your code often.
10. Ask StackOverflow.

# Types of errors
No matter how smart or how careful you are, errors are your constant companion. With practice, you will get slightly better at not making errors, and much, much better at finding and correcting them.

There are three kinds of errors: syntax errors, runtime errors, and logic errors.

## Syntax errors

- These are errors where the `compiler finds something wrong with your program, and you can't even try to execute it`. For example, you may have incorrect punctuation, or may be trying to use a variable that hasn't been declared.

- Syntax errors are the `easiest to find and correct`. The compiler will tell you where it got into trouble, and its best guess as to what you did wrong. Usually the error is on the exact line indicated by the compiler, or the line just before it; however, if the problem is incorrectly nested braces, the actual error may be at the beginning of the nested block.

## Runtime errors

- If there are no syntax errors, Java may detect an error `while your program is running`. You will get an error message telling you the kind of error, and a stack trace that tells not only where the error occurred, but also what other method or methods you were in. For example,

    ```java
    Exception in thread "main" java.lang.NullPointerException
            at Car.placeInCity(Car.java:25)
            at City.<init>(City.java:38)
            at City.main(City.java:49)
    ```

    This says that a NullPointerException was detected in the method placeCarInCity at line 25 in Car.java, which was called from the constructor for City at line 38 in City.java, which was called from the main method at line 49 in City.java. Sometimes there will be additional lines describing methods in the Java system itself; you can ignore these.

- Runtime errors are `intermediate in difficulty`. Java tells you where it discovered that your program had gone wrong, but `you need to trace back` from there to figure out where the problem originated.

## Logic errors

- A logic error, or **bug**, is when your `program compiles and runs, but does the wrong thing`. The Java system, of course, has no idea what your program is supposed to do, so it provides `no additional information to help you find the error`.

- Ways to track down a logic error include:

  - **Think** about what the program must have done in order to produce the results it did. This will lead you to where the error must have occurred.
  - Put in **print statements** to help you figure out what the program is actually doing.
  - Use a **debugger** to step through your program and watch what it does.

<hr>

# Philosophy

> You may have heard that "There's no such thing as a dumb question." Well, ` there's no such thing as a smart error.` Almost all errors are stupid errors--ones that you can recognize in a second once they are pointed out to you. And you will make stupid errors in every program you ever write, no matter how many years of experience you have.

As a result, beginners are often embarrassed to let others see their programs, for fear of being thought stupid.

The solution is to realize that everybody else--everybody else--makes the same kind of stupid errors. `Human beings are incapable of avoiding errors.` You might as well be embarrassed that you have a nose.

Both good programmers and bad programmers make stupid mistakes. The difference is that **good programmers**:

- write code that is simpler and easier to debug,
- use tools such as JUnit to help ensure that their code is correct, and
- are not satisfied with code that "mostly" works.
