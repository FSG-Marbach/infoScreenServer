rect = '<rect x="{x}" y="{y}" width="{w}" height="{h}" style="fill:{fill};stroke-width:3;stroke:{stroke}" />'
circle = '<circle cx="{x}" cy="{y}" r="{r}" stroke="{stroke}" stroke-width="4" fill="{fill}" />'
line = '<line x1="{x}" y1="{y}" x2="{w}" y2="{h}" style="stroke:{stroke};stroke-width:2" />'
polyline = '<polyline points="{points}" style="fill:none;stroke:{stroke};stroke-width:3" />'

rgb = 'rgb({r},{g},{b})'

def draw_rect(x,y,w,h,fill,stroke):
    return rect.format(x=x,y=y,w=w,h=h,fill=fill,stroke=stroke)

def draw_circle(x,y,r,fill,stroke):
    return circle.format(x=x,y=y,r=r,fill=fill,stroke=stroke)

def draw_line(x,y,w,h,stroke):
    return line.format(x=x,y=y,w=w,h=h,stroke=stroke)

def draw_polyline(points,stroke):
    return polyline.format(points=points,stroke=stroke)

def create_poly_list(l):
    pos = []
    for i in l:
        pos.append(str(i[0]) + "," + str(i[1]))
    return " ".join(pos)

def load_svg(path):
    s = open(path, "r")
    svg = s.read()
    s.close()
    return svg

def test():
    print(draw_rect(0,0,100,100,"yellow", "green"))
    print(draw_circle(50,50,50,"yellow", "green"))
    print(draw_line(0,0,100, 100,"black"))
    print(draw_line(100,0,0, 100,"black"))
