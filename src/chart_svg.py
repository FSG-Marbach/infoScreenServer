import display_svg

class chart:
    def __init__(self, w, h, v, s=1):
        self.val = v
        self.scale = 1
        self.style = s
        self.w = w
        self.h = h

    def set_scale(self, scale):
        self.scale = scale

    def set_value(self, val):
        self.val = val

    def add_value(self, val):
        self.val.append(val)

    def set_style(self, s):
        self.style = s

    def draw(self, color):
        if self.style == 1:
            l = []
            num = 0
            for i in self.val:
                l.append([num, self.h-i])
                num += self.w/len(self.val)
            return display_svg.draw_polyline(display_svg.create_poly_list(l), color)
        elif self.style == 2:
            num = 0
            s = ""
            for i in self.val:
                s += display_svg.draw_line(num,self.h,num, self.h-i,color)
                num += self.w/len(self.val)
            return s
        else:
            return ""
