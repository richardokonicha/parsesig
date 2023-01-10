

finale = """
{coin}
{direction}
כניסה בין {entry}
מטרות:
{target_list}
סטופ: {stop_loss}
"""

import re

def getTargetList(text):
  targets = []
  target_list = ''
  try:
    target_re = re.search(r'(?<=Target[s\s][\d\n])([\d.\n]+)', text, re.IGNORECASE).group(1) or 'None'
    targets = target_re.split("\n")
    targets = [x for x in targets if x]
    if not targets: raise Exception('Error')
  except Exception as e:
    targets = re.findall(r'(?<=Target[s\s][\d])[\D]+([\d.]+)', text, re.IGNORECASE)
    if not targets:
      short_term_targets = re.search(
          r'Short\s*Term:\s*([\d.\s*-]+)', text, re.IGNORECASE).group(1) or 'None'
      mid_term_targets = re.search(
          r'Mid\s*Term:\s*([\d.\s*-]+)', text, re.IGNORECASE).group(1) or 'None'
      short_term_targets = short_term_targets.split(' - ')
      mid_term_targets = mid_term_targets.split(' - ')
      mid_term_targets[-1] = mid_term_targets[-1].replace('\n', ' ')
      targets = short_term_targets + mid_term_targets
  except Exception as e:
    print("Signal unrecognised", e, text)

  for i, target in enumerate(targets, start=1):
    target_list += f'{i} - {target}\n'

  return target_list

def benfilter(text):

  try:
    coin = re.search(r'(?<=\$|#)([A-Z]+)', text,
                      re.IGNORECASE).group(1) or 'None'
    direction = re.search(r'(long|short)',
                            text, re.IGNORECASE).group(1) or 'None'
    # Convert direction to Hebrew
    if direction.lower() == 'long':
        direction = 'לונג'
    else:
        direction = 'שורד'
    
    entry = re.search(r'(?<=ENTRY\b)[\s\n:a-z]+([\d.]+\b([\sto]+|[\s-]+)[\d.]+\b)', text, re.IGNORECASE).group(1) or 'None'
    stop_loss = re.search(r'(stop[\s-]loss|sl)[:\s]+([\d.]+)', text, re.IGNORECASE).group(2) or 'None'
    target_list = getTargetList(text)

    template_message = finale.format(
      coin=coin,
      direction=direction,
      entry=entry,
      stop_loss=stop_loss,
      target_list=target_list
      )
    return template_message
    
  except Exception as e:
    print("Signal unrecognised", e, text)
  
