import re


def replace_pairs(string):
  regex = [
        ["open", "aperto"],
        ["XAUUSD", "GOLD"],
        ["US100", "US_TECH100"],
        ["US50", "US_500"],
        ["US30", "US_30"],
        ["GER30", "DAX30"],
        ["DE30", "DAX30"],
        ["USOIL", "CrudeOIL"],
        ["BTCUSD", "BTCUSD"]
        ]
  for i in regex:
    match = re.search(i[0], string)
    if match:
      string = string.replace(i[0], i[1])
  return string


def is_whitelisted(text):
    whitelist = re.search("(USD|EUR|NZD|CAD|JPY|AUD|TP+|SL+|Close+|CLOSE|XAUUSD|US|BTC|GER|DE|OIL|DAX|GOLD)", text)
    blacklist = re.search("(EXPIRES|UPGRADE|YZE|TradingBOT|OFFER|DISCOUNT|JOIN|TELEGRAM|DON'T MISS|MT4|24//7|.com|EXPIRES|@+)", text)
    value = bool(whitelist)
    if blacklist:
        value = False
        print('message filtered out, Cheers')
    return value


def add_to_text(text):
    parser = re.search("(CLOSE|PIP|SL|Move|TAKE|PROFIT|Set|SET|entry|RUNNING)", text)
    is_warning = bool(re.search("Usa la size adeguata al tuo capitale se", text))
    if parser:
      return text
    if not is_warning:
      text = f"""
{text}

Usa la size adeguata al tuo capitale se apri questo trade e rispetta il money management 📈
        """
    return text
    

def forex_leader(string):
  is_whitelist = is_whitelisted(string)
  if not is_whitelist:
    return False
  string = replace_pairs(string)
  text = add_to_text(string)
  return text



string = """
GER30 CLOSE +870 PIPS :boom::boom::boom:

"""
print(forex_leader(string))