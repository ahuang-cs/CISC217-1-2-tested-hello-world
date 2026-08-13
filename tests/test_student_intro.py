"""Tests for the Week 1 student introduction lab."""

from src.student_intro import (
    create_greeting,
    create_intro_message,
    get_course_name,
    get_student_name,
)


def test_get_student_name_returns_non_placeholder_string():
    name = get_student_name()

    assert isinstance(name, str), "get_student_name() must return a string."
    assert name.strip(), "get_student_name() must not return an empty string."
    assert name != "YOUR NAME HERE", "Replace the placeholder name."
    assert "TODO" not in name.upper(), "Return your actual preferred display name."


def test_get_course_name_identifies_course():
    course_name = get_course_name()

    assert isinstance(course_name, str), "get_course_name() must return a string."
    assert "CISC 217" in course_name, "The course name must include CISC 217."
    assert "Python" in course_name, "The course name must include Python."
    assert course_name != "COURSE NAME HERE", "Replace the placeholder course name."


def test_create_greeting_includes_name_and_starts_with_hello():
    greeting = create_greeting("Ada")

    assert isinstance(greeting, str), "create_greeting() must return a string."
    assert greeting.startswith("Hello"), "The greeting must start with Hello."
    assert "Ada" in greeting, "The greeting must include the provided name."
    assert greeting != "GREETING HERE", "Replace the placeholder greeting."


def test_create_greeting_uses_parameter_for_different_names():
    grace_greeting = create_greeting("Grace")
    guido_greeting = create_greeting("Guido")

    assert "Grace" in grace_greeting, "The greeting must include the name argument."
    assert "Guido" in guido_greeting, "The greeting must include the name argument."
    assert grace_greeting != guido_greeting, "Different names should produce different greetings."


def test_intro_message_contains_student_name_course_and_tool():
    name = get_student_name()
    course_name = get_course_name()
    message = create_intro_message()

    assert isinstance(message, str), "create_intro_message() must return a string."
    assert message != "INTRO MESSAGE HERE", "Replace the placeholder introduction message."
    assert name in message, "The intro message must include the student name."
    assert course_name in message, "The intro message must include the course name."
    assert (
        "Codespaces" in message or "GitHub" in message
    ), "The intro message must mention Codespaces or GitHub."
