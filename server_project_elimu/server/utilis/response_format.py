from flask import jsonify

def success_response(status,message,data,status_code):
    return jsonify({
        "status":status,
        "message":message,
        "data":data if data is not None else {},
    }),status_code

def error_response(status,message,status_code,errors=None):
    response= jsonify(
        {
            "status":status,
            "message":message,  
        }
        )
    if errors:
        response["errors"]=errors
    return response,status_code
