# Language Page

This is a webpage made to help none native English speakers learn *phrasal verbs* as it's something my students always have problems with.

## Linked Data

The file *questions_data.json* has the questions that are used in the quiz. More items can be added in at a later time without effecting the current code since the list length is used to choose a random question.

The data is laid out in the following format:

Key : Phrasal Verb, Example sentence 1, Example sentence 2, Answer 1, Answer 2.

## Known issues

* Since moving the correct answer to different radio buttons, it no longer displays correctly when the correct answer is selected.
    This has now been resolved. The problem was that a new correct answer was generated when the page refreshed. I resolved this by storing the correct answer in a global variable however this means the function might not function as inteded if called in another part of the code making the overall code less robust however it does now function as inteded. 

* Wrong answers are listed as such. I plan to have these populated with answers from other questions soon, so its a less obvious incorrect answer.

