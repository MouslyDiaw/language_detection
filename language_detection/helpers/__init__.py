""" Init """
import re


# regex for search html tags
RE_HTML_NEWLINE = re.compile(r"((\n|<.*?>)\s*)+")
# regex for url, link
RE_URL_EMAIL = re.compile(
    r"""(?:(\S*@|http|www)\S*
    |\.(?:pdf|png|gif|jpe?g|pptx?|docx?|xlsx?|xlt|xml|pps|html?|csv|te?xt|tif)\b
    )""",
    re.I | re.X,
)
# regex for punctuations
RE_PUNCT = re.compile(r"(?:\W+|_)")