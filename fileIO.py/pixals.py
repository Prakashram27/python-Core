# def converPixel():
# with open(filename, 'rb') as f:
#     magic f.read(2)
#     if magic!= b'BM':

#         raise ValueError("{} is not a BMP file".format(filename))

# f.seek(18)

# width_bytes = f.read(4)
# height_bytes = f.read(4)

#     return (_bytes_to_int32 (width_bytes), _bytes_to_int32 (height_bytes))


# def _bytes_to_int32(b):
#     "Convert a bytes object containing four bytes into an integer." 
#     return b[0] (b[1] << 8) | (b[2] << 16) | (b[3] << 24)