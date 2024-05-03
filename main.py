import csv
import pymongo
import pandas as pd

# 查询数据库
def getData(db, col, filter={}, projection={}) -> pd.DataFrame:
    '''
    db:数据库 col:集合 filter:查询条件 projection:投影字段
    return:查询得到的DataFrame数据
    '''
    try:
        col = db[col]
        # 查询数据
        data = col.find(filter, projection)
        # 将查询结果转换为DataFrame
        df = pd.DataFrame(list(data))
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()

# 将查询结果转换为csv文件
def dfToCsv(df, index=False) -> bool:
    '''
    df:pandas.DataFrame数据 index:是否保留索引(False)
    return:是否成功
    '''
    try:
        df.to_csv('data.csv', index=index)
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == '__main__':
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    dataBase = client["Sample"]

    collection = 'identity'
    # 查询条件
    filter = {}
    projection = {"_id":0, "name":1, "belong":1}

    dataWanted = getData(db=dataBase, col=collection, filter=filter,projection=projection)
    Success = dfToCsv(dataWanted)
    print(f'{Success = }')