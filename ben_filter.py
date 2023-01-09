
# filter for bentheman

import re


text = """
{coin}
{direction}
כניסה בין {entry}
מטרות:
{target_list}
סטופ: {stop_loss}
"""


def parse_message(input_message: str) -> str:
    # Extract the relevant information from the input message
    # signal_id = re.search(r'#(\d+)\s*', input_message,
    #                       re.IGNORECASE).group(1) or 'None'
    coin = re.search(r'COIN:\s*\$(\w+)/', input_message,
                     re.IGNORECASE).group(1) or 'None'
    direction = re.search(r'Direction:\s*(\w+)',
                          input_message, re.IGNORECASE).group(1) or 'None'
    entry = re.search(r'ENTRY:\s*([\d.]+\s*-\s*[\d.]+)',
                      input_message, re.IGNORECASE).group(1) or 'None'
    ote = re.search(r'OTE:\s*([\d.]+)', input_message,
                    re.IGNORECASE).group(1) or None
    short_term_targets = re.search(
        r'Short\s*Term:\s*([\d.\s*-]+)', input_message, re.IGNORECASE).group(1) or 'None'
    mid_term_targets = re.search(
        r'Mid\s*Term:\s*([\d.\s*-]+)', input_message, re.IGNORECASE).group(1) or 'None'
    stop_loss = re.search(
        r'STOP\s*LOSS:\s*([\d.]+)', input_message, re.IGNORECASE).group(1) or 'None'

    # Convert direction to Hebrew
    if direction.lower() == 'long':
        direction = 'לונג'
    else:
        direction = 'שורד'

    # Convert targets to list of targets
    short_term_targets = short_term_targets.split(' - ')
    mid_term_targets = mid_term_targets.split(' - ')
    mid_term_targets[-1] = mid_term_targets[-1].replace('\n', ' ')
    targets = short_term_targets + mid_term_targets

    # Create the template message
    # template_message = f'SIGNAL ID: #{signal_id}\nCOIN: {coin}\nכיוון: {direction}\nכניסה: {entry}\nמטרות:\n'
    target_list = ""
    for i, target in enumerate(targets, start=1):
        target_list += f'{i} - {target}\n'
    # template_message += f'סטופ: {stop_loss}'

    template_message = text.format(coin=coin, direction=direction,
                                   entry=entry, stop_loss=stop_loss, target_list=target_list)

    return template_message
