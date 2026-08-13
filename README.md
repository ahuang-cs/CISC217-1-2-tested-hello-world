# Week 1 Lab: Tested Hello World

## Course
CISC 217 - Intermediate Python Programming

## Module
**1.2 Lab - Tested Hello World**

## Learning goals
By completing this lab, you will practice the basic workflow used throughout the course:

- Accept a Classroom50 / GitHub Classroom assignment.
- Open the repository in GitHub Codespaces.
- Edit a Python source file.
- Run a Python program from the terminal.
- Run automated unit tests with `pytest`.
- Commit and push your work to GitHub.
- Confirm that GitHub Actions reports passing tests.

## What you will build
You will complete a small Python module that returns a personalized greeting and a short course-introduction message.

This lab is intentionally small. The goal is to verify that your GitHub, Codespaces, terminal, Python, pytest, and Git workflow are working before the programming assignments become more complex.

## Files you may edit
You may edit only this file:

```text
src/student_intro.py
```

Do not edit the files in the `tests/` folder. The tests represent the expected behavior for this assignment.

## How to complete the lab

1. Accept the Classroom50 assignment link from Canvas.
2. Open your new repository on GitHub.
3. Click **Code**.
4. Click **Codespaces**.
5. Click **Create codespace on main**.
6. Wait for VS Code in the browser to finish loading.
7. Open `src/student_intro.py`.
8. Replace the placeholder return values with your own information.
9. Run the tests in the terminal:

```bash
pytest
```

10. Fix your code until all tests pass.
11. Commit and push your changes:

```bash
git status
git add src/student_intro.py
git commit -m "Complete week 1 lab"
git push
```

12. Open the **Actions** tab on GitHub and confirm that the autograding workflow passes.
13. Submit your repository link in Canvas if directed.

## Program requirements

Complete the functions in `src/student_intro.py`.

### `get_student_name()`

Return your preferred display name as a string.

Requirements:

- Must return a string.
- Must not return the placeholder text.
- Must not return an empty string.

### `get_course_name()`

Return the course name.

Requirements:

- Must return a string.
- Must include `CISC 217`.
- Must include `Python`.

### `create_greeting(name)`

Return a greeting for the provided name.

Requirements:

- Must return a string.
- Must include the provided name.
- Must begin with `Hello`.

Example:

```python
create_greeting("Ada")
```

Could return:

```text
Hello, Ada! Welcome to CISC 217.
```

### `create_intro_message()`

Return a short course-introduction message.

Requirements:

- Must return a string.
- Must include your student name.
- Must include the course name.
- Must include either `Codespaces` or `GitHub`.

## Running the program manually

You can run the starter program with:

```bash
python src/student_intro.py
```

This should print your greeting and introduction message.

## Running tests

Run all tests with:

```bash
pytest
```

Run the tests with more detail:

```bash
pytest -v
```

## Grading

This lab is worth **1 point**.

Full credit requires:

- All required tests pass.
- Your work is committed and pushed to GitHub.
- The GitHub Actions workflow completes successfully.
- Your submitted work follows the instructions and only modifies allowed files.

## Academic integrity reminder

You may ask for help understanding error messages, test output, Git commands, or Python syntax. You must submit work that you understand and can explain. Do not copy another student’s solution.
