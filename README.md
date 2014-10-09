Backend Test
============

This test includes two parts.

1) Create a simple Django todo list application.  It should be contained in
   a folder called `ToDo`.  This application should have a page that at the top
   allows you to save text input to a new todo and then beneath the input lists
   all unfinished todos.  Additionally, you should be able to mark a todo item
   as done.


2) Write a stand alone Python script that creates word clouds.  To do this,
   you'll first need to build the data. Write code that takes a long string and
   builds its word cloud data in a dictionary, where the keys are the words and
   the values are the number of times the words occured.  For example, if the
   input is

   > After beating the eggs, Dana read the next step

   the output should be

   ```
   {
    'after': 1,
    'beating': 1,
    'the': 2,
    'eggs': 1,
    'dana': 1,
    'next': 1,
    'step': 1
   }
   ```

   You may assume the input will only contain words and standard punctuation.
