import json

def format_response(result):
    if isinstance(result, dict) and "error" in result:
        return json.dumps({"status": "error", "message": result["error"]}, ensure_ascii=False)
    return json.dumps({"status": "success", "data": result}, ensure_ascii=False)
