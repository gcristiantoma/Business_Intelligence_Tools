##### This Module adds all the data from the csv file to the sql
import sqlalchemy
from os import system
from selenium_class import *
def ExpandRowsColumns():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

engine = sqlalchemy.create_engine('mysql+pymysql://root:abc123@localhost:3306/ftse_mib')

# dfSQL = pd.read_sql_table('prices_and_others_vars',engine)

#excluding the first columbn which is not usefull and reseting the index
def Prepare_Df_BeforeSqlInsertion(df):
    # df = pd.read_csv(r"C:\Users\tomy\Documents\MEGAsync\Python\Selenium\indici_sole24.csv")

    df=df.iloc[:,:]
    df.reset_index(drop=True)

    #dropping duplicates
    df=df.drop_duplicates()

    # In order to be able to insert the date into sql the datetime has to be YEAR-Month-Day:
    df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y %H:%M:%S", dayfirst=True)
    # this functions is to be used in the apply method to filter the % out


    def filterPercentageSymbol():
        def ok_row(row):
            return row[:-1]
        df["Var %"] = df["Var %"].apply(lambda x: ok_row(x))
    filterPercentageSymbol()
    return df

# inserting the data into sql
def transfer_df_SQL(df):
    Prepare_Df_BeforeSqlInsertion(df)
    df.to_sql(
        name='prices_and_others_vars',  # database table name
        con=engine,
        if_exists='append',
        index=False )
    print("transfered to SQL 100%")


# Execute Function in this part:
s=sel_class()
s.navigate()
s.create_headers()
df_=s.create_rows_df()
df=Prepare_Df_BeforeSqlInsertion(df_)
s.save_results()

ExpandRowsColumns()
# print(df)

transfer_df_SQL(df)
# raise SystemExit
system('taskkill /fi "WindowTitle eq C:\Program Files\Python38\python.exe"')
system('taskkill /fi "WindowTitle eq taskeng.exe"')





