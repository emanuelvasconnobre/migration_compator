from utils.get_headers_skeleton import get_headers_skeleton
from utils.compare_skeletons import compare_skeletons

def compare_header_structure(old_headers: dict, new_headers: dict):
    old_headers_skeleton = get_headers_skeleton(old_headers)
    new_headers_skeleton = get_headers_skeleton(new_headers)

    headers_differences = compare_skeletons(old_headers_skeleton, new_headers_skeleton)