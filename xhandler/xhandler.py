# coding=utf-8

import pandas as pd

def run():
    indexes = [1, 3, 6, 8, 9, 10, 11, 12, 14, 16, 17, 18, 19, 22, 23, 25, 26, 27, 28, 29, 30, 32, 
    36, 37, 39, 41, 42, 43, 44, 48, 49, 53, 54, 60, 61, 62, 64, 66, 67, 69, 71, 73, 76, 77, 78, 80, 81, 
    82, 83, 86, 87, 89, 90, 92, 95, 98, 100, 105, 106, 107, 108, 110, 111, 114, 117, 118, 121, 124, 126, 
    127, 128, 129, 130, 131, 134, 138, 140, 141, 143, 147, 149, 151, 153, 155, 156, 157, 159, 161, 163]

    catalog = pd.read_excel('./xlsxes/产品目录2(87 of 163).xlsx', usecols=[1], skiprows=[0, 1]).values
    products = []
    for index in indexes:
        products.append(catalog[index - 1][0])

    df = pd.read_excel('./xlsxes/2019药品数据.xlsx', skiprows=[1, 2, 3, 4, 5, 6])
    datas = df.values
    names = df.iloc[:, 3].values
    indexes = []
    for index in range(len(names)):
        for product in products:
            if product.strip() in names[index].strip():
                indexes.append(index)
    else:
        for index in indexes:
            print(datas[index])
    
if __name__ == '__main__':
	run()
