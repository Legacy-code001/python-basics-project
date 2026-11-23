def bool_of(value):
    
    falely_value  = (None, False, 0, 0.0, "", [], (), {}, set())
    if value in falely_value:
        return False
    else: 
        return True


def safe_measure(raw):
   clean = str(raw).strip()
   if clean.count('.') > 1:
    return "invalid"
   if clean.replace(".", "", 1).isdigit():
    return float(clean)
   return "invalid"

def censor(message, word):
    mess_arr = message.split(" ")
    for i in range(len(mess_arr)):
        if mess_arr[i] == word:
            mess_arr[i] = "[REDACTED]"
        # This condition checks if the 'word' is a substring of the message part
        elif word in mess_arr[i]:
            mess_arr[i] = mess_arr[i].replace(word, "[REDACTED]")
    res = ' '.join(mess_arr)
    return res

def is_valid_transmission(message):
    # 1. String method for the start: .startswith()
    # 2. String method for the end: .endswith()
    # 3. 'in' operator for the separator: "//" in message
    # 4. Joined together using the 'and' operator
    return message.startswith("BEGIN") and message.endswith("END") and "//" in message

