def exists_key(request_json, list_keys):

    keys_not_found_in_request = []

    for data in list_keys:
        if data in request_json:
            continue
        
        else:
            keys_not_found_in_request.append(data)

    if len(keys_not_found_in_request) == 0:    
        return request_json
    
    return {"error": f"Está faltando o item {keys_not_found_in_request}"}
