from utils.compare_skeletons import compare_skeletons
from utils.get_json_skeleton import get_json_skeleton

def compare_body_structure(old_json: dict, new_json: dict):
    old_skeleton = get_json_skeleton(old_json)
    new_skeleton = get_json_skeleton(new_json)

    return compare_skeletons(old_skeleton, new_skeleton)