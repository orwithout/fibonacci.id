import json

def hello_world(verify_token=False, user_id="", full_path="", sub_path="", temp_file_path="", fn="", accept="", content_type="", args_in_url="", token_in_url="", args_in_header="", token_in_header="", headers="", body=""):
    data = {
        "user_id": str(user_id),
        "full_path": str(full_path),
        "sub_path": str(sub_path),
        "temp_file_path": str(temp_file_path),
        "fn": str(fn),
        "accept": str(accept),
        "content_type": str(content_type),
        "args_in_url": str(args_in_url),
        "token_in_url": str(token_in_url),
        "args_in_header": str(args_in_header),
        "token_in_header": str(token_in_header),
        "headers": str(headers),
        "body": str(body),
        "message": "hello world"
    }
    return data
