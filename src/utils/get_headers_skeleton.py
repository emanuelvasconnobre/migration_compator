def get_headers_skeleton(headers):
    return {key: type(value).__name__ for key, value in headers.items()}