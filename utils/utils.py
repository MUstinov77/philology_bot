def unpack_sequence(
    sequence,
    attr_name: str
):
    for row in sequence:
        for item in row:
            yield getattr(item, attr_name)