import csv
import pandas as pd 

df  = pd.read_csv('sales_data.csv', encoding = "UTF-8")


category_imu = df[df['category'] ==  'IMU' ]
# print(category_imu)
# print(category_imu.shape[0])


# ful_sales_number = df.shape[0]

total_rows = df.shape[0]
total_sum = df['price'].sum()
summ_kategory = (df.groupby('category')['price'].sum()/total_sum)*100
category_frame = pd.DataFrame({


    'Сумма $': df.groupby('category')['price'].sum(),
    'Процент %': (df.groupby('category')['price'].sum()/total_sum)*100

})
result_sort = category_frame.sort_values('Процент %', ascending=False)
print(result_sort)