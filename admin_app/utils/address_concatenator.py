def format_pencil_box_location(location):
    address_parts = [
        location.address1,
        location.address2 if location.address2 else None,
        f"{location.city}, {location.state} {location.zip}"
    ]
    formatted_address = "".join(filter(None, address_parts))

    return formatted_address
