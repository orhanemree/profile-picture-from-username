from PIL import Image, ImageDraw
from io import BytesIO

# randomize list of valid characters
chars = list("lcj5m9p27wnx6v0a_sr34f*oy8.ebdzgq1tihu-k")


def remap(x, in_min, in_max, out_min, out_max):
    new_x = (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    return new_x


def make_profile(username:str, canvas_size:int, pixel_size:int):

    if len(username) < 3:
        raise Exception("Username must be at least 3 characters.")
    else:
        r = round(remap(chars.index(username[0].lower()) ** 2, 0, len(chars) ** 2, 1, 255))
        g = round(remap(chars.index(username[1].lower()) ** 2, 0, len(chars) ** 2, 1, 255))
        b = round(remap(chars.index(username[2].lower()) ** 2, 0, len(chars) ** 2, 1, 255))

        # for better contrast
        lightness = round(((0.212 * r + 0.701 * g + 0.087 * b) / 255) * 100)
        canvas_color = "#ccc" if lightness < 50 else "#222"
        fill_color = (r, g, b)

        image = Image.new("RGB", (canvas_size, canvas_size), canvas_color)
        draw = ImageDraw.Draw(image)

        for i in username:

            i = i.lower()

            if username.count(i) % 2 != 0:

                x0 = round(remap(chars.index(i), 0, len(chars), 1, canvas_size / pixel_size - 2)) * pixel_size
                y0 = round(remap(chars[::-1].index(i), 0, len(chars), 1, canvas_size / pixel_size - 2)) * pixel_size
                x1 = x0 + pixel_size
                y1 = y0 + pixel_size

                draw.rectangle([x0, y0, x1, y1], fill=fill_color)

                # symmetry
                x0 = canvas_size - pixel_size - x0
                x1 = x0 + pixel_size

                draw.rectangle([x0, y0, x1, y1], fill=fill_color)

        buffered = BytesIO()
        image.save(buffered, format="PNG")
        buffered.seek(0)

        return buffered
