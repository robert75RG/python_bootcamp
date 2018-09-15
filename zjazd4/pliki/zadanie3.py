import sys

try:
    input_file = sys.argv[1]
    output_file = sys.argv[2]

except:
    input_file ='pliki_wejsciowe/emails.txt'
    output_file = 'emaile_corrected.txt'

def collect_emails(input_file):
    emeils = set()
    with open(input_file) as f:
        for line in f:
            if line.count("@") == 1:
                line = line.strip().lower()
                emeils.add(line)
    return emeils

def save_emails(emails, output_file):
    with open(output_file, 'w') as f:
        for email in sorted(emails):
            f.write(email + '\n')


save_emails(collect_emails(input_file), output_file)