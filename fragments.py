import os 

def read_html_fragments(relativeFilePath, fileName):
    currentWorkingDirectory = os.path.dirname(os.path.realpath(__file__))
    htmlFragmentFilePath = os.path.join(f'{currentWorkingDirectory}{relativeFilePath}', fileName)
    try:
        with open(htmlFragmentFilePath, 'r') as file:
            htmlFragment = file.read()
    except FileNotFoundError:
        print(f"{fileName} file not found in path: {htmlFragmentFilePath}")

    if htmlFragment:
        return htmlFragment
    else:
        return None