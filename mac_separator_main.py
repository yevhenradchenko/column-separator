import pandas as pd


def do():
    df = pd.read_csv('file_name.csv') # Input file with file extension
    column = df['column_name'] # Column title to wotk with
    list = []
    for i in column.values:
        if isinstance(i, str):
            i = i.strip()
            i = i.replace(" ", ",") # Replace spasing with comas
            for j in i.split(','):
                list.append(j.lower()) # Edit all uppercase symbols to lowercase

    with open('output_file_name.txt', 'w') as f_out: # Name and type of file you want to see as output source
        f_out.write(','.join(list))


if __name__ == '__main__':
    do()
