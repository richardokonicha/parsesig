
# filter for bentheman

import re


def parse_message(input_message: str) -> str:
    # Extract the relevant information from the input message
    signal_id = re.search(r'#(\d+)\s*', input_message,
                          re.IGNORECASE).group(1) or 'None'
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
    targets = short_term_targets + mid_term_targets

    # Create the template message
    template_message = f'SIGNAL ID: #{signal_id}\nCOIN: {coin}\nכיוון: {direction}\nכניסה: {entry}\nמטרות:\n'
    for i, target in enumerate(targets, start=1):
        template_message += f'{i} - {target}\n'
    template_message += f'סטופ: {stop_loss}'

    return template_message
