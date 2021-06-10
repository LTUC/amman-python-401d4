# Implementation: Singly Linked Lists

## Specifications
- Read all of these instructions carefully. Name things exactly as described. 
- Do all your work in a public repository called `data-structures-and-algorithms`, with a well-formatted, detailed top-level README.md.
- Create a new branch in your repo called `linked-list`.
- Your top-level readme should contain a "Table of Contents" navigation to all of your challenges and implementations so far. (Don't forget to update it!)
- Place this implementation in your `Data-Structures` folder within your repository.
- On your branch, create...
  - _C#_: a new .NET core class library named `LinkedList.cs`. 
  - _JavaScript_: a folder named `linkedList` which contains a file called `linked-list.js`
  - _Python_: a folder named `linked_list` which contains a file called `linked_list.py`
  - _Java_: a package named `linkedList` which contains a file called `LinkedList.java`
- Include any language-specific configuration files required for this challenge to become an individual component, module, library, etc.
  - _NOTE: You can find an example of this configuration for your course in your class lecture repository._

## Features
- Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node. 
- Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
  - Define a method called `insert` which takes any value as an argument and adds a new node with that value to the `head` of the list with an O(1) Time performance.
  - Define a method called `includes` which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node's value somewhere within the list.
  - Define a method called `toString` (or `__str__` in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as: 
    - `"{ a } -> { b } -> { c } -> NULL"`
- Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.
- Be sure to follow your language/frameworks standard naming conventions (e.g. _C#_ uses PascalCasing for all method and class names).

## Structure and Testing
Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write tests to prove the following functionality:

1. Can successfully instantiate an empty linked list
1. Can properly insert into the linked list
1. The head property will properly point to the first node in the linked list
1. Can properly insert multiple nodes into the linked list
1. Will return true when finding a value within the linked list that exists
1. Will return false when searching for a value in the linked list that does not exist
1. Can properly return a collection of all the values that exist in the linked list

Ensure your tests are passing before you submit your solution.

## Stretch Goal

Create a new branch called `doubly-linked-list`, and, using the resources available to you online, implement a doubly linked list (completely separate from your singly linked list). 

## Documentation: Your README.md

```markdown
# Singly Linked List
<!-- Short summary or background information -->

## Challenge
<!-- Description of the challenge -->

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## API
<!-- Description of each method publicly available to your Linked List -->
```

## Submission Instructions
1. Create a pull request from your branch to your `master` branch
1. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents){:target="_blank"} of the specifications and tasks above, with the actual steps that you completed checked off
1. Submitting your completed work to Canvas:
   1. Copy the link to your open pull request and paste it into the corresponding Canvas assignment
   1. Leave a description of how long this assignment took you in the comments box
   1. Add any additional comments you like about your process or any difficulties you may have had with the assignment
1. Merge your branch into `master`, and delete your branch (don't worry, the PR link will still work)
