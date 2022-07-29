def exists_key(request_json, list_keys):

    keys_not_found_in_request = []

    for key in list_keys:
        if key in request_json:
            continue
        
        else:
            keys_not_found_in_request.append(key)

    if len(keys_not_found_in_request) == 0:    
        return request_json
    
    return {"error": f"Está faltando o item {keys_not_found_in_request}"}

def exists_value(request_json, data_already_in_db):

    for json in data_already_in_db:
        if json['id'] == request_json['id'] or json['tech'] == request_json['tech']:
            return json
    
    return False
