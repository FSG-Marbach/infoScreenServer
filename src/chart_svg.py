import display_svg

class chart:
    def __init__(self, w, h, v):
        self.val = v
        self.scale = 1
        self.style = 0
        self.w = w
        self.h = h

    def set_scale(self, scale):
        self.scale = scale

    def set_value(self, val):
        self.append(val)

    def set_style(self, s):
        self.style = s

    def draw(self, color):
        l = []
        num = 0
        for i in self.val:
            l.append([num, self.h-i])
            num += w/len(self.val)
        return display_svg.draw_polyline(display_svg.create_poly_list(l), color)
        
