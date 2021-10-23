def remove_punctuations(input):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    output = ""
    for char in input:
        if char not in punctuations:
            output = output + char
    print(output)