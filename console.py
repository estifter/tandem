import os

def clear_console():
    """Clear the console. Check platform first to work with posix and windows."""

    os_type = os.name

    if os_type == 'nt':
        os.system('cls')
    elif os_type == 'posix':
        os.system('clear')
    else:
        raise SystemExit


def format_text(text, color='', bold=False, underline=False):
    """Format text for output to console. Options for color, bold, and underline.\n
       Color options: magenta, blue, cyan, green, orange, red.
    """

    if color == 'magenta':
        color_code = '\033[95m' # magenta
    elif color == 'blue':
        color_code = '\033[94m' # blue
    elif color == 'cyan':
        color_code = '\033[96m' # cyan
    elif color == 'green':
        color_code = '\033[92m' # green
    elif color == 'orange':
        color_code = '\033[93m' # orange
    elif color == 'red':
        color_code = '\033[91m' # red
    else:
        color_code = ''

    if bold:
        bold_code = '\033[1m' # bold_code
    else:
        bold_code = ''

    if underline:
        underline_code = '\033[1m' # underline_code
    else:
        underline_code = ''

    leading_code = color_code + bold_code + underline_code
    ending_code = '\033[0m' # endline
    if leading_code == '':
        ending_code = ''

    return leading_code + str(text) + ending_code

def print_heading(score):
    print(format_text(f'Welcome to the trivia game for tandem! | Score: {score}\n', bold=True, underline=True))