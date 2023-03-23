string = 'to accept something even though it was not exactly what you wanted.'

encodedString = string.encode('utf8')
print(encodedString) # b'to accept something even though it was not exactly what you wanted.'

retrnString = encodedString.decode()

print(retrnString) #string wil be normal 


