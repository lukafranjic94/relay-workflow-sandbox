import re


def hello():
    """Return the Relay greeting string."""
    return 'Hello, Relay'


def slugify(text):
    """Lowercase text and convert to a URL-friendly slug."""
    slug = text.lower()
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    return slug.strip('-')
