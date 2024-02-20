# Import QRCode from pyqrcode
import pyqrcode
import png
from django.conf import settings
from django.templatetags.static import get_media_prefix

def qrnow(text):
    # Generate QR code
    media_pre = get_media_prefix
    media_url = settings.MEDIA_URL
    print(media_url)
    url = pyqrcode.create(text)

    return url



