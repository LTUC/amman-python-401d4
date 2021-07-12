# Lab: Django Custom User

## Overview

Django does a great job at allowing to get started with a solid foundation. But a foundation is just the beginning. We still need to "build the house."

One of the first things many developers need to do is have a custom user.

For this lab you'll build your application from the very beginning with a Custom User model.

## Feature Tasks and Requirements

- create Django application from scratch that has a custom user model named `CustomUser`
- Custom user should use *email* instead of *username* for signup / login
- Application should work with Django Admin

## Implementation Notes

- Make sure to create custom user model **before** migrating data

### User Acceptance Tests

- Verify the creation of a new user with email and password
- Verify that duplicate emails are not allowed

## Configuration

Use `poetry` to initialize `django-custom-user` project.

```console
> $ mkdir django-custom-user
> $ cd django-custom-user
> $ poetry init -n
```

Use the folder created by Poetry as the root of your project's git repository.

Refer to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed instructions.

## Stretch

Create a Django application using [DjangoX](https://github.com/wsvincent/djangox){:target="_blank"}
