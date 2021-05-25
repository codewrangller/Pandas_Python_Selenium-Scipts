import pandas as pd
df = pd.read_excel(#'xlsx_file.....')
data = df
data

data.#column_title/header_name

for column_title, df_column_title in df.groupby(#'column_title/header'):
    print(column_title)
    print(df_location)
    loc = r'C:\\Path....'
    writer = pd.ExcelWriter(f'{loc}{column_title}.xlsx', engine ='xlsxwriter')
    df_column_title.to_excel(writer, index = False)
    writer.save()
        






