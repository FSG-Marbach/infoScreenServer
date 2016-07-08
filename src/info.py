html = """
<html>
        <head>
        <title>Schule als Staat Info</title>
        <script>
        var i=-130;
        function pageScroll() {
            window.scrollTo(0,Math.max(i, 0));
            i++;
            var body = document.body,
            html = document.documentElement;
            var h = Math.max(window.innerHeight,document.body.offsetHeight,document.documentElement.clientHeight);
            if(i+window.innerHeight-130>h) {
                i = 0;
                window.scrollTo(0,0);
                location.reload(); 
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
            margin-bottom: 25px;
            box-shadow: 4px 4px 5px grey; 
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
            body {
                background-color: #F4F4F4;
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

    def add_svg(self, title, svg, w, h, t=""):
        self.display[title] = "<svg width=\"" + str(w) +"\" height=\"" + str(h) + "\">" + svg + "</svg><br><br>" + t

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
