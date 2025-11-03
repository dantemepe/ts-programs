import turtle
import math
import os
import sys
import subprocess

turtle.bgcolor("black")
turtle.color("gray")
turtle.shapesize(0.01)
turtle.setup(1000, 850)
turtle.speed(0)
size = input("How many circles do you want to be in the image? (1k+ reccomended)(can lag a lot if the amount inputted is higher than 10k)  > ")
x = 0
z = 0
dp=0
while True:
    turtle.circle(x)
    turtle.left(math.pi)
    x += 1
    z += 1
    dp+=1
    print(dp," circles drawn")
    if z >= int(size):
        break

# Ensure canvas updated
canvas = turtle.getcanvas()
try:
    canvas.update()
except Exception:
    pass

# paths
script_dir = os.path.dirname(os.path.abspath(__file__))
eps_path = os.path.join(script_dir, "shii.eps")
svg_path = os.path.join(script_dir, "shii.svg")
png_path = os.path.join(script_dir, "shii.png")

# write EPS (tkinter postscript)
try:
    canvas.postscript(file=eps_path)
    print("Wrote EPS:", eps_path)
except Exception as e:
    print("Failed to write EPS:", e)

def safe_itemcget(c, item, option):
    try:
        return c.itemcget(item, option)
    except Exception:
        # some canvas item types don't support all options (raises TclError)
        return ""

# helper: extract stroke/fill/width from canvas item
def item_stroke_fill(c, item):
    # use safe_itemcget so unknown option errors are swallowed
    stroke = safe_itemcget(c, item, "outline") or safe_itemcget(c, item, "fill") or safe_itemcget(c, item, "foreground") or "gray"
    fill = safe_itemcget(c, item, "fill")
    width_raw = safe_itemcget(c, item, "width") or safe_itemcget(c, item, "linewidth") or "1"
    try:
        width = float(width_raw)
    except Exception:
        width = 1.0
    return stroke, fill, width

def coords_to_points(coords):
    pts = []
    for i in range(0, len(coords), 2):
        pts.append(f"{coords[i]:.2f},{coords[i+1]:.2f}")
    return " ".join(pts)

# export approximate SVG from Tk canvas (keeps background rect)
def canvas_to_svg(c, svg_path):
    bbox = c.bbox("all")
    if bbox:
        x0, y0, x1, y1 = bbox
        width = int(x1 - x0)
        height = int(y1 - y0)
        viewbox = f"{x0} {y0} {width} {height}"
        vb_x, vb_y = x0, y0
    else:
        width = c.winfo_width() or 1000
        height = c.winfo_height() or 850
        viewbox = f"0 0 {width} {height}"
        vb_x, vb_y = 0, 0

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="utf-8"?>\n')
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{width}" height="{height}" viewBox="{viewbox}" style="background:black">\n')
        f.write(f'  <rect x="{vb_x}" y="{vb_y}" width="{width}" height="{height}" fill="black" />\n')

        for item in c.find_all():
            itype = c.type(item)
            coords = c.coords(item)
            stroke, fill, sw = item_stroke_fill(c, item)

            if not coords:
                continue

            if itype in ("line", "polyline"):
                points = coords_to_points(coords)
                f.write(f'  <polyline points="{points}" stroke="{stroke}" stroke-width="{sw}" fill="none" stroke-linecap="round" stroke-linejoin="round" />\n')
            elif itype == "oval":
                if len(coords) >= 4:
                    x0c, y0c, x1c, y1c = coords[:4]
                    cx = (x0c + x1c) / 2.0
                    cy = (y0c + y1c) / 2.0
                    rx = abs(x1c - x0c) / 2.0
                    ry = abs(y1c - y0c) / 2.0
                    fill_attr = fill if fill else "none"
                    f.write(f'  <ellipse cx="{cx:.2f}" cy="{cy:.2f}" rx="{rx:.2f}" ry="{ry:.2f}" stroke="{stroke}" stroke-width="{sw}" fill="{fill_attr}" />\n')
            elif itype == "polygon":
                points = coords_to_points(coords)
                fill_attr = fill if fill else "none"
                f.write(f'  <polygon points="{points}" stroke="{stroke}" stroke-width="{sw}" fill="{fill_attr}" />\n')
            elif itype == "rectangle":
                if len(coords) >= 4:
                    x0c, y0c, x1c, y1c = coords[:4]
                    x_rect = min(x0c, x1c)
                    y_rect = min(y0c, y1c)
                    w_rect = abs(x1c - x0c)
                    h_rect = abs(y1c - y0c)
                    fill_attr = fill if fill else "none"
                    f.write(f'  <rect x="{x_rect:.2f}" y="{y_rect:.2f}" width="{w_rect:.2f}" height="{h_rect:.2f}" stroke="{stroke}" stroke-width="{sw}" fill="{fill_attr}" />\n')
            elif itype == "text":
                tx = coords[0]
                ty = coords[1] if len(coords) > 1 else 0
                text_val = c.itemcget(item, "text") or ""
                f.write(f'  <text x="{tx:.2f}" y="{ty:.2f}" fill="{stroke}">{text_val}</text>\n')
            else:
                points = coords_to_points(coords)
                f.write(f'  <polyline points="{points}" stroke="{stroke}" stroke-width="{sw}" fill="none" />\n')

        f.write('</svg>\n')
print("")
# write SVG
try:
    canvas_to_svg(canvas, svg_path)
    print("Wrote SVG:", svg_path)
except Exception as e:
    print("SVG export failed:", e)

# Convert SVG -> PNG: try cairosvg first (recommended), then fallback to opening EPS with Pillow (requires Ghostscript)
converted = False
try:
    import cairosvg
    try:
        cairosvg.svg2png(url=svg_path, write_to=png_path)
        print("Saved PNG via cairosvg:", png_path)
        converted = True
    except Exception as e:
        print("cairosvg conversion failed:", e)
except Exception:
    pass

if not converted:
    try:
        from PIL import Image
        try:
            img = Image.open(eps_path)
            img.load()
            img.save(png_path, "PNG")
            print("Saved PNG via Pillow from EPS:", png_path)
            converted = True
        except Exception as e:
            print("Pillow failed to rasterize EPS (needs Ghostscript):", e)
    except Exception:
        print("Pillow not available in this interpreter. Install with:")
        print(f'    "{sys.executable}" -m pip install --user pillow')
        print("Or install cairosvg for direct SVG->PNG conversion:")
        print(f'    "{sys.executable}" -m pip install --user cairosvg')

if not converted:
    print("PNG not created. Install cairosvg or Pillow+Ghostscript, then re-run.")
import time
turtle.done()  # Ends the graphics loop
time.sleep(10)  # Keep window open for a moment before exit
sys.exit(0)