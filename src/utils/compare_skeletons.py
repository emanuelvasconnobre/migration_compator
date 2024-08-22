def compare_skeletons(old_skeleton, new_skeleton, path=""):
    differences = []

    old_keys = set(old_skeleton.keys())
    new_keys = set(new_skeleton.keys())

    for key in old_keys - new_keys:
        differences.append(
            f"Key '{path + key}' present in the old JSON but missing in the new one."
        )

    for key in new_keys - old_keys:
        differences.append(
            f"Key '{path + key}' present in the new JSON but missing in the old one."
        )

    for key in old_keys & new_keys:
        old_value = old_skeleton[key]
        new_value = new_skeleton[key]
        new_path = f"{path}{key}."

        if isinstance(old_value, dict):
            differences += compare_skeletons(old_value, new_value, new_path)
        elif (
            isinstance(old_value, list)
            and len(old_value) > 0
            and isinstance(old_value[0], dict)
        ):
            differences += compare_skeletons(old_value[0], new_value[0], new_path)
        elif old_value != new_value:
            differences.append(
                f"Different types for key '{path + key}': {old_value} in the old vs {new_value} in the new."
            )

    return differences
