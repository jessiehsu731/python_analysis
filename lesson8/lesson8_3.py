import pandas as pd

def main():
    """
    主函數，用於讀取、處理和儲存上市公司資料。
    """
    # 讀取 CSV 檔案，檔案名為 '上市公司資料.csv'，並將資料載入到 DataFrame (df) 中。
    df = pd.read_csv('上市公司資料.csv')
    
    # 移除 DataFrame (df) 中包含 NaN (缺失值) 的所有列，並將結果儲存到新的 DataFrame (df1) 中。
    df1 = df.dropna()
    
    # 重新索引 DataFrame (df1) 的欄位，只保留指定的欄位，並將結果儲存到新的 DataFrame (df2) 中。
    # 保留的欄位包括：'公司代號'、'出表日期'、'公司名稱'、'產業別'、'營業收入-當月營收'、'營業收入-上月營收'。
    df2 = df1.reindex(columns = ['公司代號','出表日期','公司名稱','產業別','營業收入-當月營收','營業收入-上月營收'])
    
    # 重新命名 DataFrame (df2) 中的欄位名稱，並將結果儲存到新的 DataFrame (df3) 中。
    # 將 '營業收入-當月營收' 更名為 '當月營收'。
    # 將 '營業收入-上月營收' 更名為 '上月營收'。
    df3 = df2.rename(columns={
        '營業收入-當月營收': '當月營收', 
        '營業收入-上月營收': '上月營收'
        })
    
    # 印出處理後的 DataFrame (df3) 的內容。
    print(df3)

    # 將處理後的 DataFrame (df3) 儲存為 CSV 檔案，檔案名為 '上市公司資料整理.csv'，編碼方式為 'utf-8'。
    df3.to_csv('上市公司資料整理.csv',encoding='utf-8')
    
    # 將處理後的 DataFrame (df3) 儲存為 Excel 檔案，檔案名為 '上市公司資料整理.xlsx'。
    df3.to_excel('上市公司資料整理.xlsx')
    
    # 印出 "存檔完成" 的訊息，表示資料已成功儲存。
    print("存檔完成") 


# 檢查是否直接執行此腳本，如果是，則執行 main() 函數。
if __name__ == '__main__':
    main()
