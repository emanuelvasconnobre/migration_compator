from config.load_config import load_config
from utils.make_request import make_request
from modules.body import compare_body_structure

def main():
    config = load_config()

    old_response = make_request(config['target'])
    new_response = make_request(config['compare'])

    json_differences = compare_body_structure(old_response['json'], new_response['json'])
    headers_differences = compare_body_structure(old_response['headers'], new_response['headers'])

    if json_differences:
        print("JSON structure differences found:")
        for diff in json_differences:
            print(diff)
    else:
        print("The JSON response skeletons are identical!")

    if headers_differences:
        print("Headers structure differences found:")
        for diff in headers_differences:
            print(diff)
    else:
        print("The headers skeletons are identical!")

if __name__=="__main__":
    main()