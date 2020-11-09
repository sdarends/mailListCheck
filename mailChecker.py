import pandas as pd


def load_excel(filename):
    mail_list = open(filename, "r")
    return mail_list


def convert_to_pandas(excel_file):
    df = pd.read_excel(excel_file)
    return df


def main():
    file = load_excel("train_list.xlsx")
    table = convert_to_pandas(file)
    print(table)


if __name__ == '__main__':
    main()

