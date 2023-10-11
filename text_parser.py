import re


def bparse(line):
    parser = re.search(
        "^(BUY|SELL)\s([A-Z]*)\s[\(@at\s]*([0-9]*[.,][0-9]*)[\).]", line)
    if parser != None:
        p = parser.groups()
        place = p[0]
        place = place.upper()

        if place == "BUY":
            flag = '📈'
        if place == "SELL":
            flag = '📉'
        output = f"""
#{p[1]}
{p[0]}{flag}{p[2]}
"""
        return output
    else:
        return None


def tparser(line):
    parser = re.search(
        "(^[takeTAKE]*\s[profitPROFIT]*)\s\d\s[at@\s]*([\d]*[,.][0-9]*)", line)
    if parser != None:
        p = parser.groups()
        output = f"""✅TP {p[-1]}"""
        return output
    else:
        return None


def sparser(line):
    parser = re.search(
        "(^[stopSTOP]*\s[lossLOSS]*)\s[at@\s]*([\d]*[.,][\d]*)", line)
    if parser != None:
        p = parser.groups()
        output = f"""🛑SL {p[-1]}"""
        return output
    else:
        return None


def pasig(rawsignal):
    """entry function to parse forex signals"""
    signal = """"""
    rsignal = rawsignal.split("\n")
    for line in rsignal:
        bp = bparse(line)
        tp = tparser(line)
        sp = sparser(line)
        for i in [bp, tp, sp]:
            if i != None:
                signal = signal + """
"""+i
    return signal


rawsignal = """
BUY EURUSD (@ 1.0877) 
Take profit 1 at 1.0897
Take profit 2 at 1.0927
Take profit 3 at 1.0977
Stop loss at 1.0795
"""

outputsignal = """
#EURUSD 
BUY:chart_with_upwards_trend:1.0877
:white_check_mark:TP 1.0897
:white_check_mark:TP 1.0927
:white_check_mark:TP 1.0977
✅
🛑SL 1.0795
"""

# print(pasig(rawsignal))


# EB10 filters
def emanuelefilter(text):

    parser = re.search(
        "(GBP|USD|EUR|NZD|CAD|JPY|AUD|TP+|SL+|Close+|pips|tp|sl|UK+|US+|SELL+|BUY+)", text)
    invalid = re.search(
        "(OFFER|DISCOUNT|JOIN|TELEGRAM|DON'T MISS|MT4|.com|https:|24//7|EXPIRES|@+)", text)

        

    value = bool(parser)
    if invalid:
        value = False
        print('message filtered out, Cheers')
    return value


def transform_text(text):
    parser = re.search("(USD|EUR|NZD|CAD|JPY|AUD|CHF|GBP)", text)

    is_warning = bool(re.search("INVEST WITH CONSCIENCE", text))
    # https://www.tradingview.com/x/cehtMm4G/
    has_link = bool(re.search("(.com|www.tradingview.com|https)", text))

    if parser:
        if not is_warning:
            text = f"""
{text}
..................................
⚫ INVEST WITH CONSCIENCE 
⚫ Don't invest more than you can afford
⚫ This signal does not constitute an investment advice, 
we are not responsible for money loss
        """
        if has_link:
            link = re.search("(https[://w.\w]+)", text).group()
            text = text.replace(link, " ")

    return text
