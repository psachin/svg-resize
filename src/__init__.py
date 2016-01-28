import argparse
from .svg_resize import process_stream


def main():
    parser = argparse.ArgumentParser(description='Resize SVG and add a frame for printing.')
    parser.add_argument('input', help='source svg file ("-" for stdin, which is default)', nargs='?', default='-')
    parser.add_argument('output', help='destination svg file ("-" for stdout, skip for the same as source)', nargs='?')
    parser.add_argument('-x', '--width', help='target width (including margins, default units are mm)')
    parser.add_argument('-y', '--height', help='target height (including margins, default units as mm)') # choose smaller of two
    parser.add_argument('-l', '--longest', help='target longest side')
    parser.add_argument('-s', '--shortest', help='target shortest side')
    parser.add_argument('-m', '--margin', help='margin (default units are mm)', default='0')
    parser.add_argument('-f', '--frame', action='store_true', help='add white frame around the picture')
    options = parser.parse_args()
    process_stream(vars(options))
