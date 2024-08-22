def get_json_skeleton(data, skeleton=None):
    if skeleton is None:
        skeleton = {}
    
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                skeleton[key] = get_json_skeleton(value, {})
            elif isinstance(value, list) and len(value) > 0:
                skeleton[key] = [get_json_skeleton(value[0], {})]
            else:
                skeleton[key] = type(value).__name__
    return skeleton