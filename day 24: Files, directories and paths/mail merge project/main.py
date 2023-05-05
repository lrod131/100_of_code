PLACEHOLDER = "[name]"
INVITATION_NAMES = 'day 24: Files, directories and paths/mail merge project/Input/Names/invited_names.txt'
LETTER_TEMPLATE = 'day 24: Files, directories and paths/mail merge project/Input/Letters/starting_letter.txt'


with open(INVITATION_NAMES) as template:
    names = template.readlines()

with open(LETTER_TEMPLATE) as template:
    letter = template.read()
    for each_name in names:
        strip_name = each_name.strip()
        new_letter = letter.replace(PLACEHOLDER, strip_name)
        with open(f'day 24: Files, directories and paths/mail merge project/Output/ReadyToSend/letter_to_{strip_name}.txt', mode='w') as invitation:
            invitation.write(new_letter)
