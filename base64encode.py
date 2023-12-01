import base64 
  
sample_string = "GeeksForGeeks is the best"
sample_string_bytes = sample_string.encode("ascii") #encoding with the 'ascii' which does this b'the thang you typed'
  
base64_bytes = base64.b64encode(sample_string_bytes) #encoding base64
base64_string = base64_bytes.decode("ascii") #decoding from ascii
  
print(f"Encoded string: {base64_string}") #to print