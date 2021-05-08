import re


def regular_expression(text):
    cleaned_data = re.findall("([\w\s])", text)
    cleaned_data = ''.join(cleaned_data)
    cleaned_data =  re.sub("_","", cleaned_data)
    cleaned_data = re.sub("([\n])", "", cleaned_data)
    cleaned_data = re.sub('http | https\S+', "", cleaned_data)
    cleaned_data = re.sub("([\s]{2,})", " ", cleaned_data)

    return cleaned_data
