import re
import sys

VOID_TAGS = {"area","base","br","col","embed","hr","img","input","link","meta","param","source","track","wbr"}

def validate(path, debug=False):
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()

    # remove comments
    s = re.sub(r'<!--.*?-->', '', s, flags=re.S)

    tag_re = re.compile(r'<(/?)([a-zA-Z0-9:-]+)([^>]*)>', re.S)
    pos = 0
    stack = []
    errors = []

    while True:
        m = tag_re.search(s, pos)
        if not m:
            break
        full = m.group(0)
        closing = bool(m.group(1))
        name = m.group(2).lower()
        rest = m.group(3) or ''
        start = m.start()
        end = m.end()

        # skip DOCTYPE and xml declarations
        if name.startswith('!') or name.startswith('?'):
            pos = end
            continue

        # handle script/style: skip until their closing tag
        if not closing and name in ('script','style'):
            close_re = re.compile(r'</%s>' % name, re.I)
            close_m = close_re.search(s, end)
            if close_m:
                pos = close_m.end()
                continue
            else:
                errors.append(f"Unclosed <{name}> starting at {start}")
                pos = end
                continue

        # self-closing if ends with '/>'
        self_closing = rest.strip().endswith('/')

        if name in VOID_TAGS or self_closing:
            if debug:
                print(f"SKIP (void/self): <{name}> at {start}")
            pos = end
            continue

        if closing:
            if debug:
                print(f"CLOSE </{name}> at {start}, stack top: {stack[-1] if stack else None}")
            if not stack:
                errors.append(f"Extra closing </{name}> at {start}")
            else:
                top = stack.pop()
                if top != name:
                    errors.append(f"Mismatched closing </{name}> at {start}, expected </{top}>")
        else:
            stack.append(name)
            if debug:
                print(f"OPEN  <{name}> at {start}, stack now: {stack}")

        pos = end

    for t in reversed(stack):
        errors.append(f"Unclosed <{t}> tag")

    if errors:
        print('Validation issues found:')
        for e in errors:
            print(' -', e)
        return 1
    else:
        print('No tag-matching issues found.')
        return 0

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python html_tag_validator.py path/to/file.html [--debug]')
        sys.exit(2)
    debug = False
    if len(sys.argv) > 2 and sys.argv[2] == '--debug':
        debug = True
    sys.exit(validate(sys.argv[1], debug=debug))
