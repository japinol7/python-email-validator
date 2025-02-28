class EmailNotValidError(ValueError):
    """Parent class of all exceptions raised by this module."""
    pass


class EmailSyntaxError(EmailNotValidError):
    """Exception raised when an email address fails validation because of its form."""
    pass


class EmailUndeliverableError(EmailNotValidError):
    """Exception raised when an email address fails validation because its domain name does not appear deliverable."""
    pass
