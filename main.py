import sys
from PIL import Image

from trace import trace_image


def main():
    img = Image.open('test.png')
    print(trace_image(img))
    return 0


if __name__ == '__main__':
    sys.exit(main())
