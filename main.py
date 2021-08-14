from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def pictocharpic(pic, chars="今晚打老虎"):
    '''
    @params pic: PIL Image object
    @params chars: chars to show as pixels
    '''
    size = 512
    fontsize = 10

    width, height = pic.size
    print(width, height)
    if max(width, height) > size:
        scale = max(width, height) / size
        pic = pic.resize((int(width / scale), int(height / scale)))
        width, height = pic.size

    w, h = width * fontsize, height * fontsize
    img = Image.new("RGB", (w, h), (255, 255, 255))

    font = ImageFont.truetype("Dengb.ttf", fontsize)

    draw = ImageDraw.Draw(img)

    len_chars = len(chars)
    count_chars = 0
    for row in range(height):
        for col in range(width):
            pixel = pic.getpixel((col, row))
            pixel = [round(min(255, pix * 1.5)) for pix in pixel]
            pixel = tuple(pixel)
            # print(pixel)
            pos = ( (col - 1) * fontsize , (row - 1) * fontsize )
            draw.text(pos, chars[count_chars % len_chars], pixel, font=font)
            count_chars += 1

    img.save('pil_red1.png')


def main():
    # pic = input("input name of the picture")
    pic = "./xx1.jpg"
    img = Image.open(pic)
    pictocharpic(img)

if __name__ == "__main__":
    main()
