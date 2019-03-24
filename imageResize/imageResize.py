from PIL import Image
from sys import argv

if (len(argv) != 5):
    exit("Usage: python3 imageResize.py newWidth newHeight infile outfile")

w = int(argv[1])
h = int(argv[2])
infile = argv[3]
outfile = argv[4]

inImage = Image.open(infile)
width, height = w, h
outImage = inImage.resize((width, height))
# width, height = inImage.size
# outImage = inImage.resize((width * n, height * n))

outImage.save(outfile)
