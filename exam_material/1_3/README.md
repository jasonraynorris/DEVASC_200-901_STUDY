# DEVASC_200-901_STUDY
<p>Author: Jason Ray Norris</p>
<h4>Developed using Python3.7.4</h4>
<hr>
<h5>1.3 Describe the concepts of test-driven development
</h5>
<hr>

 <h6>Section 1.3.1</h6>
 
# What is test driven development?

Reference: https://en.wikipedia.org/wiki/Test-driven_development

1. Add a test
2. Run all tests and see if the new test fails
3. Write the code
4. Run tests
5. Refactor code

"If ever I believe my work is done
Then I'll start back at one"

Did anyone else hear Brian McKnight?

"One
You're like a dream come true
Two
Just want to be with you
Three
Girl, it's plain to see
That you're the only one for me
And four
Repeat steps one through three
Five
Make you fall in love with me
If ever I believe my work is done
Then I'll start back at one"

Back to a more serious note.  Let's summarize my interpretation of these steps.

1. Add a test
<br>&nbsp;&nbsp;This is synonymous with writing pseudo code for me. Gather your requirements and define what you will try to do to meet the requirement.
2. Run all tests and see if the new test fails
<br>&nbsp;&nbsp;Verify that your code does not already meet the requirement.
3. Write the code
<br>&nbsp;&nbsp;This is a dirty coding process.  Just make it pass your test.
4. Run tests
<br>&nbsp;&nbsp;Test your code. Does it pass test? Iterate over Step 3 and Step 4 until you pass test.
5. Refactor code
<br>&nbsp;&nbsp;Now that your code is passing test, lets clean it up. Then test your refactored code.

Reference: https://en.wikipedia.org/wiki/Code_refactoring

<b>Code refactoring</b> is the process of restructuring existing computer code—changing the factoring—without changing its external behavior. Refactoring is intended to improve nonfunctional attributes of the software. Advantages include improved code readability and reduced complexity; these can improve source-code maintainability and create a more expressive internal architecture or object model to improve extensibility.
