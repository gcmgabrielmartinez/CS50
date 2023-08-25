file = input("File name: ").strip().lower()

extensions = {
    "gif": "image/gif",
    "jpeg":"image/jpeg",
    "jpg":"image/jpeg",
    "png":"image/png",
    "pdf":"application/pdf",
    "txt": "text/plain",
    "zip":"application/zip"
}

if "." not in file:
    print("application/octet-stream")
else:
    extension = file.rsplit(".")[-1]
    if extension not in extensions:
        print("application/octet-stream")
    else:
        print(extensions[extension])
