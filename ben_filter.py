import re
finale = """
{coin}
{direction}
כניסה בין {entry}
מטרות:
{target_list}
סטופ: {stop_loss}
"""


def get_common_value(text):
    coin = re.search(r'(?<=\$)([A-Z]+)', text,
                     re.IGNORECASE).group(1) or 'None'
    direction = re.search(r'(long|short)',
                          text, re.IGNORECASE).group(1) or 'None'
    # Convert direction to Hebrew
    if direction.lower() == 'long':
        direction = 'לונג'
    else:
        direction = 'שורד'

    entry = re.search(
        r'(?<=ENTRY\b)[\s\n:a-z*]+([\d.]+\b([\sto]+|[\s-]+)[\d.]+\b)', text, re.IGNORECASE).group(1) or 'None'
    stop_loss = re.search(
        r'(stop[\s-]loss|sl)[\\n:\s*]+([\d.]+)', text, re.IGNORECASE).group(2) or 'None'

    value = {
        coin: coin,
        direction: direction,
        stop_loss: stop_loss,
        entry: entry
    }
    return value


def parse_message(text):
    target_list = ''
    targets = []
    TARGETS_LIMIT = 8

    if re.search(r'Bitcoin Bullets', text, re.IGNORECASE):
        coin, direction, stop_loss, entry = get_common_value(text)
        entry = entry.replace("to", "-")
        target_re = re.search(
            r'(Target[s\s*\\n]+)([\d.\n]+)', text, re.IGNORECASE).group(2) or 'None'
        targets = target_re.split("\n")
        targets = [x for x in targets if x]
        print("Bitcoin Bullets")

    elif re.search(r'Russian Insiders',  text, re.IGNORECASE):
        coin, direction, stop_loss, entry = get_common_value(text)
        targets = re.findall(
            r'(?<=Target[s\s][\d])[\D]+([\d.]+)', text, re.IGNORECASE)
        print("Russian Insider")

    elif re.search(r'Long Entry Zone', text, re.IGNORECASE):
        coin, direction, stop_loss, entry = get_common_value(text)
        coin = re.search(r'(?<=\$|#)([A-Z]+)', text,
                     re.IGNORECASE).group(1) or 'None'
        targets = re.findall(
            r'(?<=Target[s\s][\d])[\D]+([\d.]+)', text, re.IGNORECASE)
        print("Long Entry Zone")

    elif re.search(r'SIGNAL ID', text, re.IGNORECASE):
        coin, direction, stop_loss, entry = get_common_value(text)
        short_term_targets = re.search(
            r'Short\s*Term:\s*([\d.\s*-]+)', text, re.IGNORECASE).group(1) or 'None'
        mid_term_targets = re.search(
            r'Mid\s*Term:\s*([\d.\s*-]+)', text, re.IGNORECASE).group(1) or 'None'
        short_term_targets = short_term_targets.split(' - ')
        mid_term_targets = mid_term_targets.split(' - ')
        mid_term_targets[-1] = mid_term_targets[-1].replace('\n', ' ')
        targets = short_term_targets + mid_term_targets
        print('SIGNAL ID Binance killers')
    else:
        print('Unrecognized signal', text)
        return False

    if len(targets) > TARGETS_LIMIT:
        targets = targets[1:min(len(targets), TARGETS_LIMIT + 1)]

    for i, target in enumerate(targets, start=1):
        target_list += f'{i} - {target}\n'

    try:
        template_message = finale.format(
            coin=coin,
            direction=direction,
            entry=entry,
            stop_loss=stop_loss,
            target_list=target_list
        )
        return template_message
    except Exception as e:
        return False
