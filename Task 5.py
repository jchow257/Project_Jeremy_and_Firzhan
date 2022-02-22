import requests
url = 'https://unsplash.com/'
x = requests.get(url)
print(x.text)
print("Status code:")
print("\t*", x.status_code)

h = requests.head(url)
print("Header: ")
print("Top of the header")
for y in h.headers:
    print("\t", y, ":", h.headers[y])
print("Bottom of the header")
