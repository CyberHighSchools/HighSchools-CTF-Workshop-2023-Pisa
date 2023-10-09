def sanitize_filename(filename):
    sanitized = filename
    found = sanitized.find("../")
    while found != -1:
        sanitized = sanitized[:found] + sanitized[found + 3:]
        found = sanitized.find("../")

    found = sanitized.find("..\\")
    while found != -1:
        sanitized = sanitized[:found] + sanitized[found + 3:]
        found = sanitized.find("..\\")
    sanitized = sanitized.lstrip()
    sanitized = sanitized.rstrip()
    if sanitized and (sanitized[0] == '/' or sanitized[0] == '\\'):
        sanitized = sanitized[1:]
    return sanitized
