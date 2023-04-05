# def grayscale(filename,pixal):
    
#     """Created and writes a BMP file
    
#     Arg:
#     file name : the name of the file to be created 

#     Pixals: A rectangular images stored as a sequence.
#     Each row must be a iterable series of integer in the range of 0-255

#     """

#     height = len(pixal)
#     width = len(pixal[0])


#     with open(filename,'wb') as bmp:
#         bmp.write(b'BM')

#         size_bookmark = bmp.tell() # the next four bites hold the file size as 32 bytes
#         print(size_bookmark)

#         bmp.write(b'\x80\x88') # Unused 16-bit integer - should be zero bmp.write(b'\x80\x88') # Unused 16-bit integer - should be zero

#         pixel_offset_bookmark = bmp.tell() # The next four bytes hold the integer offset to the bmp.write(b'\x80\x80\x80\x00') # pixel data. Zero placeholder for now.

#         # Image Header

#         bmp.write(b'\x28\x68\x80\x00') # Image header size in bytes 48 decimal

#         # bmp.write(_int32_to_bytes(width)) # Image width in pixels 
#         # bmp.write(_int32_to_bytes (height)) # Image height in pixels

#         bmp.write(b'\x01\x00')

#         #Number of image planes

#         bmp.write(b'\x08\x88') #Bits per pixel 8 for grayscale
#         bmp.write(b'\x80\x80\x80\x80') # No compression 
#         bmp.write(b'\x80\x80\x80\x88') # Zero for uncompressed images
#         bmp.write(b'\x80\x80\x80\x00') 
#         bmp.write(b'\x80\x80\x80\x88') # Unused pixels per meter

#         # Unused pixels per meter

#         bmp.write(b'xe8\x80\x80\x88') # Use whole color table 
#         bmp.write(b'\x80\x80\x80\x08') # All colors are important


#         # Color palette a linear grayscale

#         for c in range(256):
#             #bmp.write(bytes((c, c, c, e))) # Blue, Green, Red, Zero

#         # Pixel data

#         # pixel_data_bookmark = bmp.tell()

#         # row_data = bytes(row)

#         # for row in reversed (pixels): # BMP files are bottom to top 
#         #     padding= b'x80' ((4- (len(row) %4)) %4) # Pad row to multiple of four bytes
#         # bmp.write(row_data)

#         # bmp.write(padding)

#         # End of  file

#         # eof_bookmark = bmp.tell()

#         # Fill in file size placeholder

#         # bmp.seek(size_bookmark) 
#         # bmp.write(int32_to_bytes (eof_bookmark))

#         # Fill in pixel offset placeholder

#         # bmp.seek(pixel_offset_bookmark) 
#         # bmp.write(_int32_to_bytes (pixel_data_bookmark))


