
#a simple reusable text formatting class

class TextFormatting:
    def __init__(self, format, string):
        self.textString = string
        self.formats =  {
            'BLUE': '\033[94m',
            'CYAN': '\033[96m',
            'GREEN': '\033[92m',
            'YELLOW': '\033[93m',
            'BOLD': '\033[1m',
            'UNDERLINE': '\033[4m',
            'END': '\033[0m'
        }
        self.formattedTextString = self.formatText(string, format)

    def formatText(self, string, format):
        return self.formats[format]  +  string +  self.formats['END']
         

