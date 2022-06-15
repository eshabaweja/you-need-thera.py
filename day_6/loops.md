| For loop | While loop |  
| --- | --- |
|Initialization may be either in loop statement or outside the loop. | Initialization is always outside the loop.|
| Once the statement(s) is executed then after increment is done. | Increment can be done before or after the execution of the statement(s). |
| It is normally used when the number of iterations is known. | It is normally used when the number of iterations is unknown. |
| Condition is a relational expression. | Condition may be expression or non-zero value. |
| It is used when initialization and increment is simple. | It is used for complex initialization. |
| For is entry controlled loop. | While is also entry controlled loop. |
| for ( init ; condition ; iteration ) { statement(s); } | while ( condition ) { statement(s); } |
| used to obtain the result only when number of iterations is known. | used to satisfy the condition when the number of iterations is unknown |

## do-while loops

Unlike for and while loops, which test the loop condition at the top of the loop, the do...while loop in C programming checks its condition at the bottom of the loop.

A do...while loop is similar to a while loop, except the fact that it is guaranteed to execute at least one time.
Syntax

The syntax of a do...while loop in C programming language is −
```
do {
   statement(s);
} while( condition );
```
Notice that the conditional expression appears at the end of the loop, so the statement(s) in the loop executes once before the condition is tested.

If the condition is true, the flow of control jumps back up to do, and the statement(s) in the loop executes again. This process repeats until the given condition becomes false.
AD
