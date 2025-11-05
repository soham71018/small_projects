from PIL import Image
import os

inpath = input("Drag and drop your image here and Press Enter :").strip()
if inpath.startswith("'") or inpath.startswith('"'):
    input_path = inpath[1:-1] 

if not os.path.exists(inpath)   :
    print ("File not found .")
    exit()

base , ext = os.path.exists(inpath)
outpath= f"{base} compressed{ext}"

with Image.open(inpath) as img:
    originalsize=os.path.getsize(inpath)
    img.save(outpath,optimize=True,quality=60)
    compressedsize=os.path.getsize(outpath)

print(f"✅ Compression Done!\nOriginal: {originalsize/1024:.2f} KB\nCompressed: {compressedsize/1024:.2f} KB\nSaved as: {outpath}")
