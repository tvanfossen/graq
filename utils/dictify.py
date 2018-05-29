def dictify(msg):
    temp = {}
    for field in msg._fields:
        temp[field] = getattr(msg, field)
        if field == "metadata" or field == "payload_fields":
            temp[field] = dictify(getattr(msg, field))
        if field == 'gateways':
            x = 0  # save for later if needed

    return temp

# end
