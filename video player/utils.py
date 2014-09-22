def isGray(image):
    """Return True if the image has one channel per pixel."""
    return image.ndim < 3

def widthHeightDividedBy(image, divisor):
    """Return an image's dimensions, divided by a value."""
    h, w = image.shape[:2]
    return (w/divisor, h/divisor)