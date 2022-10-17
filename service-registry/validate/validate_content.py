
def validate_content(rc):
    if rc["service_name"]:
        if rc["service_ip"]:
            if rc["service_port"]:
                if rc["service_endPoint_Post"] or rc["service_endPoint_Get"] or rc["service_endPoint_Put"] or rc["service_endPoint_Delete"]:
                    return "Validate Complete",True
                else:
                    return "Missing Service EndPoint (min. 1)"
            else:
                return "Missing Service Port", False
        else:
            return "Missing Service IP", False
    else:
        return "Missing Service Name", False
            