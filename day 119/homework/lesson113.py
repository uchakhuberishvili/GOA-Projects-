def justify(text, width):
    words = text.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) > width:
            lines.append(current_line)
            current_line = []
            current_length = 0
        current_line.append(word)
        current_length += len(word)

    if current_line:
        lines.append(current_line)

    justified_text = []
    for i in range(len(lines)):
        line = lines[i]
        if i == len(lines) - 1:
            justified_text.append(' '.join(line))
        else:
            total_spaces = width - sum(len(word) for word in line)
            gaps = len(line) - 1
            if gaps > 0:
                spaces_per_gap = total_spaces // gaps
                extra_spaces = total_spaces % gaps
                line_str = ''
                for j in range(gaps):
                    line_str += line[j] + ' ' * (spaces_per_gap + (1 if j < extra_spaces else 0))
                line_str += line[-1]
                justified_text.append(line_str)
            else:
                justified_text.append(line[0])

    return '\n'.join(justified_text)