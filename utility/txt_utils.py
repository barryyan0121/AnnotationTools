def txt_to_text(file_path):
    result = []
    with open(file_path, errors='ignore') as fp:
        lines = fp.readlines()
        for txt in lines:
            result.append(txt)
    return result
