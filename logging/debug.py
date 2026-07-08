import logging

"""
Exercise 1 - Student Login System
Goal

Understand the difference between INFO, WARNING, and ERROR.

Scenario

A student is trying to log in.

Rules:

Username entered → INFO
Password too short (<8 characters) → WARNING
Password correct → INFO
Wrong password → ERROR
Three failed attempts → CRITICAL

Example output:

INFO: User Rahul is trying to log in
WARNING: Password is too short
ERROR: Incorrect password
CRITICAL: Account locked after 3 failed attempts

What you'll learn

INFO = normal events
WARNING = suspicious but program continues
ERROR = operation failed
CRITICAL = something very serious

"""

