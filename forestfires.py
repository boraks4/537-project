import pandas as pd


def main():
    df = pd.read_csv('forestfires.csv', sep=',')
    print(df['X'])


if __name__ == '__main__':
    main()
