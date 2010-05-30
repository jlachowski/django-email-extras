
__version__ = "0.1.0"


try:
    from email_extras.settings import USE_GNUPG
    pass
else:
    if USE_GNUPG:
        try:
            import gnupg
        except ImportError:
            raise ImproperlyConfigured, "Could not import gnupg"
