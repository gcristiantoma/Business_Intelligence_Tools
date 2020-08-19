import  selenium
from selenium import webdriver
import pandas as pd
from datetime import datetime
import os.path
from os import path
import os
from time import sleep

class sel_class:

    def __init__(self):
        self.driver = webdriver.Chrome(r"C:\Users\tomy\Documents\MEGAsync\Programming\Python\Final Porjects\Python\FTSE MIB (Python+SQL+Analytics)\v1\chromedriver_win32\chromedriver.exe")

        # self.driver = webdriver.Chrome()

        #open the webpage
    def navigate(self):
        myLink="https://mercati.ilsole24ore.com/azioni/borsa-italiana/ftse-mib?refresh_ce"
        self.driver.get(myLink)
        sleep(5)

        # geting headers and create df
    def create_headers(self):

            # taking date and time
        self.now = datetime.now()
        self.tempo = self.now.strftime("%d/%m/%Y %H:%M:%S")

        lista_headers = []
        cols_headers = self.driver.find_elements_by_xpath("//*[@id=\"wrapper\"]/div[1]/element/element/div/div[1]/section[1]/div/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/table/thead/tr/th")

        for x in cols_headers:
            lista_headers.append(x.text)  # append each header to a list of headers

        lista_headers.append("Data")
        self.df = pd.DataFrame(columns=lista_headers)

        return self.df

    # take all rows from the webpage and insert them into the previous df
    def create_rows_df(self):
        str1 = "//*[@id=\"wrapper\"]/div[1]/element/element/div/div[1]/section[1]/div/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/table/tbody/tr["
        str2 = "]/td["
        str3 = "]"
        lista = []
        lista_temp = []
        cols = self.driver.find_elements_by_xpath("//*[@id=\"wrapper\"]/div[1]/element/element/div/div[1]/section[1]/div/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/table/tbody/tr[1]/td")
        rows = self.driver.find_elements_by_xpath("//*[@id=\"wrapper\"]/div[1]/element/element/div/div[1]/section[1]/div/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/table/tbody/tr")
        # Looping trough each cell of the table
        for i in range(1, len(rows) + 1):
            for j in range(1, len(cols) + 1):

                final_path = str1 + str(i) + str2 + str(j) + str3  # construct the path string using i and j
                elem = self.driver.find_element_by_xpath(final_path).text  # take the text from the cell returnd
                lista_temp.append(elem)  # append in the temporary list each cell(elem)

                if j == len(cols):  # when the elements(cells) in the temporary list have the same size as the headers then we are going to write down the row to the df
                    n_rows_df = len(self.df)  # checking the present nr of rows in the df
                    lista_temp.append(self.tempo)  # appending the date and time to our list filled with one row
                    self.df.loc[n_rows_df] = lista_temp  # charging the DataFrame with the row completed
                    # lista.append(lista_temp)
                    lista_temp = []  # reset the temporary list with the previous row
        return self.df

    def save_results(self):
        self.mypath = r"C:\Users\tomy\Documents\MEGAsync\Programming\Python\Final Porjects\Python\FTSE MIB (Python+SQL+Analytics)\v1\indici_sole24.csv"
        if (path.exists(self.mypath)):
            # Save to csv , if the file exists ignore the headers
            self.df.to_csv(self.mypath, mode='a', header=False)
            print("File exists and  Saved")
        else:
            # Save the file including the headers
            self.df.to_csv(self.mypath)
            print("The file has been created and saved")
        self.driver.close()



# s=sel_class()
# s.navigate()
# s.create_headers()
# s.create_rows_df()
# s.save_results()
