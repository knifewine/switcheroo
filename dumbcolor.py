# dumb imperitive terminal colorizer that is probably broken in many ways. enjoy!

COLORS = {'black': 30, 'red': 31, 'green': 32, 'yellow': 33, 'blue': 34, 'purple': 35, 'cyan': 36, 'white': 37}
RESET = '\033[0m'


def colorize(text, color_declaration='blue bold'):
    try:
        declarations = color_declaration.split('|')

        codes = ''

        for dec in declarations:
            words = dec.split(' ')
            color_name = words.pop(0)
            basecode = COLORS[color_name]

            regcolor, bold, underline = '0;', '', ''

            if 'background' in words:
                regcolor = ''
                basecode = basecode + 10

            if 'bold' in words:
                bold = '1;'

            if 'underline' in words:
                underline = '4;'

            codes += '\033[{regcolor}{bold}{underline}{basecode}m'.format(
                regcolor=regcolor, bold=bold, underline=underline, basecode=basecode
            )

        return '{codes}{text}\033[0m'.format(codes=codes, text=text)
    except:
        print "couldn't format text, something went wrong"
        return text
