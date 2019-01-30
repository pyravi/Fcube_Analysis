# Python 3.7.0, Pandas 0.23.4

from io import StringIO
import pandas as pd
import csv

# strings in first 3 columns are of arbitrary length
x = '''ABCD,EFGH,IJKL,34.23;562.45;213.5432
MNOP,QRST,UVWX,56.23;63.45;625.234
'''*10**6

def csv_reader_1(x):
    df = pd.read_csv(x, usecols=[3], header=None, delimiter=',',
                     converters={3: lambda x: x.split(';')})
    return df.join(pd.DataFrame(df.pop(3).values.tolist(), dtype=float))

def csv_reader_2(x):
    df = pd.read_csv(x, header=None, delimiter=';',
                     converters={0: lambda x: x.rsplit(',')[-1]}, dtype=float)
    return df.astype(float)

def csv_reader_3(x):
    return pd.read_csv(x, usecols=[3, 4, 5], header=None, sep=',|;', engine='python')

def csv_reader_4(x):
    with x as fin:
        reader = csv.reader(fin, delimiter=',')
        L = [i[-1].split(';') for i in reader]
        return pd.DataFrame(L, dtype=float)

def csv_reader_5(x):
    with x as fin:
        return pd.read_csv(StringIO(fin.getvalue().replace(';',',')),
                           sep=',', header=None, usecols=[3, 4, 5])
