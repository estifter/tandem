import console

def test_format_text():
    assert console.format_text('red', 'red') == '\033[91m' + 'red' + '\033[0m' # color code + text + end code
    assert console.format_text(5) == '5'

