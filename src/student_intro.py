"""Week 1 student introduction lab.

Complete the functions in this file so the unit tests pass.
Run the tests with:

    pytest
"""


def get_student_name():
    """Return your preferred display name as a string."""
    # TODO: Replace this placeholder with your preferred display name.
    return "YOUR NAME HERE"


def get_course_name():
    """Return the course name as a string."""
    # TODO: Return a string that includes both "CISC 217" and "Python".
    return "COURSE NAME HERE"


def create_greeting(name):
    """Return a greeting that includes the provided name.

    Args:
        name: The name to include in the greeting.

    Returns:
        A greeting string that starts with "Hello" and includes name.
    """
    # TODO: Build and return a greeting using the name parameter.
    return "GREETING HERE"


def create_intro_message():
    """Return a short introduction message for the course.

    The message should include your student name, the course name, and either
    "Codespaces" or "GitHub".
    """
    # TODO: Use the functions above to build a complete introduction message.
    return "INTRO MESSAGE HERE"


if __name__ == "__main__":
    print(create_greeting(get_student_name()))
    print(create_intro_message())
