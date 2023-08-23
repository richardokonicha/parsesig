import re

def is_valid(text):
    "filter"
    invalid = re.search("(OFFER|DISCOUNT|JOIN|TELEGRAM|DON'T MISS|MT4|24//7|EXPIRES|easyforexpips|FREE COPY)", text)
    value = bool(invalid)
    return not value

def bparse(line):
    parser = re.search("([A-Z]*)\s(BUY|SELL)\s[\(@at\s]*([0-9]*[.,][0-9]*)[\).\s]*", line)
    if parser is not  None:
        p = parser.groups()
        place = p[1]
        place = place.upper()

        if place == "BUY":
            flag = '📈'
        if place == "SELL":
            flag = '📉'
        output = f"""
#{p[0]}
{p[1]}{flag}{p[2]}
"""
        return output
    else:
        return None

def tparser(line):
    parser = re.search("(^[TP:]*)\s[at@\s]*([\d]*[,.][0-9]*)", line)
    if parser is not  None:
        p = parser.groups()
        output = f"""✅TP {p[-1]}"""
        return output
    else:
        return None

def sparser(line):
    parser = re.search("(^[SL:]*)\s[at@\s]*([\d]*[,.][0-9]*)", line)
    if parser is not  None:
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

rawsignal1 = """
EURUSD BUY @ 1.0943 / 1.0949
TP: 1.0963 (scalper) 
TP: 1.0993 (intraday) 
TP: 1.1043 (swing)
SL: 1.0873
▪️Use money management 2-3%
"""

rawsignal2 = """

CHFJPY SELL @ 165.81 / 165.76

TP: 165.61 (scalper) 
TP: 165.31 (intraday) 
TP: 164.81 (swing)
SL: 166.61

▪️Use money management 2-3%
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

# print(pasig(rawsignal2))

# ..................

