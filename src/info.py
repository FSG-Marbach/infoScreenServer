html = """<html>
<head>
<title>Schule als Staat Info</title>
<script>
var i=1;
function pageScroll() {
    window.scrollTo(0,i);
    i++;
    var body = document.body,
    html = document.documentElement;
    if(i>document.documentElement.scrollHeight-1) {
        i = 0;
        window.scrollTo(0,0);
    }
    scrolldelay = setTimeout(pageScroll,10);
}
</script>
<style>
#con {
width:99%;
border: 1px solid #ccc;
background-color: #F3F3F3;
color: #000000;
opacity: 0.9;
filter: alpha(opacity=90);
padding-bottom: 25px;
}
#in {
margin-left: auto;
margin-right: auto;
width: 90%;
}
h1, h2, h3 {
margin-left: auto;
margin-right: auto;
width: 80%;
}
</style>
</head>
<body onload="pageScroll()">
{feeds}
</body>
</html>"""

class info:
    def __init__(self):
        self.display = {}

    def add_info(self, title, text):
        self.display[title] = text

    def add_svg(self, title, svg, w, h):
        self.display[title] = "<svg width=\"" + str(w) +"\" height=\"" + str(h) + "\">" + svg + "</svg>"

    def get_html(self):
        string = ""
        for info in self.display.keys():
            string += "<div id=\"con\"><h2>" + info + "</h2>\n<div id=\"in\">" + self.display[info] + "</div></div>\n"
        return html.replace("{feeds}", string)

def test():
    sas_info = info()
    sas_info.add_info("test", "bla")
    sas_info.add_info("test2", "ble")
    sas_info.add_info("test3", "blu")
    sas_info.add_svg("svg1", "Ich bin svg")
    print(sas_info.get_html())
