import requests

# Read txt url from file
file = open('url.txt', 'r')
# Read line to list
lines = file.readlines()

for idx, value in enumerate(lines) :

    line = value.rstrip()
    print('Line ' + str(idx) + ' : ' + line)

    # Remove any leading and trailing whitespaces include
    url = line.strip()

    # Get response from url
    response = requests.get(url)

    # Check url status and content type
    if response.status_code == 200 and response.headers['Content-Type'] == 'image/jpeg':
        # Get file name from url
        first = url.rfind("/")
        last = url.rfind(".")
        fileName = url[first+1:last]
        # Create jpg file
        file = open('img/' + fileName + '.jpg', 'wb')
        # Write content
        file.write(response.content)
        # Close file
        file.close()
        msg = '\t Download .jpg succesfuly.'
    else :
        msg = '\t Content-Type:' + response.headers['Content-Type']

    print(msg)
