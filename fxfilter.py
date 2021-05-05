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
        ["BTCUSD", "BTCUSD"],
        ["UK100", "FTSE100"],
        ["💥", "🎯"],
        ["🔊", "📈"],
        ["VIP", "FX LEADER ITALIA INDICI"],

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


def process_signals(line):
    parser = re.search("([A-Z0-9]+)([\s+-]+)(?=BUY|SELL)(BUY|SELL)\s+([0-9.]+)", line)
    tpraw = re.search("(TP)([:\s]+)([0-9.]+)", line)
    slraw = re.search("(SL)([:\s]+)([0-9.]+)", line)

    if parser != None:
      p = parser.groups()
      pair, action, price = p[0], p[2], p[3]
      pair = replace_pairs(pair)

      if tpraw != None:
        t = tpraw.groups()
        tp = t[2]
      else:
        tp = None

      if slraw != None:
        s = slraw.groups()
        sl = s[2]
      else:
        sl = None

    
      output = f"""
{pair} {action} @ {price}

TP: {tp or 'aperto'}
SL: {sl or 'aperto'}

Usa la size adeguata al tuo capitale se apri questo trade e rispetta il money management 📈

      """
      return output



def process_report(line):
    parser = re.search("(CHANNEL\s+REPORT)", line)
    if parser != None:
      line = replace_pairs(line)
      return line



def process_general(line):
    parser = re.search("CLOSE|PIPS|RUNNING|HALF|SET|SL|at|HIT|pips|Close|half|Move|entry|to|TP", line)
    if parser != None:
      line = replace_pairs(line)
      return line



string1 = """
GER30 RUNNING +630 PIPS :boom:
"""