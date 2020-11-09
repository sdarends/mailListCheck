import pandas as pd


def load_excel(filename):
    mail_list = open(filename, "r", encoding="UTF8")
    return mail_list


def convert_to_pandas(csv_file):
    df = pd.read_csv(csv_file, sep=';', header=0)
    return df


def main():
    file = load_excel("Data/train_list.csv")
    table = convert_to_pandas(file)
    print(table.shape)
    print(table)


if __name__ == '__main__':
    main()
