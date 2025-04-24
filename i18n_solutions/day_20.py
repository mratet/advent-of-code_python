import base64


def decode_utf8_extended(byte_stream):
    i = 0
    result = []
    while i < len(byte_stream):
        byte = byte_stream[i]
        masks = [
            (0x7F, 0x7F),
            (0xDF, 0x1F),
            (0xEF, 0x0F),
            (0xF7, 0x07),
            (0xFB, 0x03),
            (0xFD, 0x01),
        ]
        for codepoint_length, (len_mask, first_mask) in enumerate(masks, start=1):
            if byte <= len_mask:
                codepoint = byte & first_mask
                for next_byte in byte_stream[i + 1 : i + codepoint_length]:
                    codepoint = (codepoint << 6) | (next_byte & 0x3F)
                result.append(codepoint)
                i += codepoint_length
                break
    return result


def codepoint_to_bytes(input_codepoints, bits_per_codepoint):
    bin_stream = "".join(
        [bin(codepoint)[2:].zfill(bits_per_codepoint) for codepoint in input_codepoints]
    )
    return bytes([int(bin_stream[i : i + 8], 2) for i in range(0, len(bin_stream), 8)])


data = base64.b64decode(open("input.txt").read())
data = map(ord, data.decode("utf-16"))
data = codepoint_to_bytes(data, 20)
data = decode_utf8_extended(data)
data = codepoint_to_bytes(data, 28)
print(data.decode("utf-8"))
