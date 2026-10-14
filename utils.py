import re
import unicodedata


def hello():
    """Return the Relay greeting string."""
    return 'Hello, Relay'


def slugify(text):
    """Lowercase text and convert to a URL-friendly slug."""
    normalized = unicodedata.normalize('NFKD', text)
    ascii_text = ''.join(
        char for char in normalized if not unicodedata.combining(char)
    )
    slug = ascii_text.lower()
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    return slug.strip('-')
