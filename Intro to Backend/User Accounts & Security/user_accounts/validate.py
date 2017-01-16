import re


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def verify_username(username):
    """Verifies usernames based on a regular expression.

    Args:
        username (string): The username entered by the user.

    Returns:
        boolean: Verification result.

    """
    return USER_RE.match(username) is not None

def verify_password(password):
    """Verifies passwords based on a regular expression. Also checks if
        original password and verification passwords are identical.

    Args:
        password (string): The password entered by the user.
        verify (string): The verification password entered by the user.

    Returns:
        boolean: Verification result.

    """
    return PASS_RE.match(password) is not None

def verify_verify(password, verify):
    """Verifies that the password and verifiction password are identical.

    Args:
        password (string): The password entered by the user.
        verify (string): The password verification entered by the user.

    Returns:
        boolean: Verification result.

    """
    return password == verify

def verify_email(email):
    """Verifies email addresses based on a regular expression.

    Args:
        email (string): The email address entered by the user.

    Returns:
        boolean: Verification result. Also returns True if the email is blank.

    """
    return EMAIL_RE.match(email) is not None or not email

