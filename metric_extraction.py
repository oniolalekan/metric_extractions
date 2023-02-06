from datetime import datetime
import pandas as pd
from pandas import to_datetime


def metrics_extract(data):
    site_id = data['Site ID'].tolist()
    cleaned_site_id = [x for x in site_id if str(x) != 'nan']

    df_page_view = pd.DataFrame()
    df_uniq_visitor = pd.DataFrame()
    df_total_time_spent = pd.DataFrame()
    df_visit = pd.DataFrame()
    df_avg_time_spent = pd.DataFrame()

    try:
        for i in data:
            df_dataset_list = data[i].tolist()
            date_viewed = [to_datetime(w) for w in df_dataset_list if type(w) == datetime]
            day_viewed = [to_datetime(w).day for w in df_dataset_list if type(w) == datetime]
            if "Page Views" in i:
                header_type = "Page Views"
                result = transpose_data(df_dataset_list, day_viewed, date_viewed, cleaned_site_id, header_type)
                old_df_pv = pd.concat([result, df_page_view])
                df_page_view = old_df_pv
            elif "Unique Visitors" in i:
                header_type = "Unique Visitors"
                result = transpose_data(df_dataset_list, day_viewed, date_viewed, cleaned_site_id, header_type)
                old_df_uv = pd.concat([result, df_uniq_visitor])
                df_uniq_visitor = old_df_uv
            elif "Total Time Spent" in i:
                header_type = "Total Time Spent"
                result = transpose_data(df_dataset_list, day_viewed, date_viewed, cleaned_site_id, header_type)
                old_df_ttt = pd.concat([result, df_total_time_spent])
                df_total_time_spent = old_df_ttt
            elif "Visits" in i:
                header_type = "Visits"
                result = transpose_data(df_dataset_list, day_viewed, date_viewed, cleaned_site_id, header_type)
                old_df_vst = pd.concat([result, df_visit])
                df_visit = old_df_vst
            else:
                # transpose the average time spent here
                avg_time_spent = [a for a in df_dataset_list if isinstance(a, (int, float))]
                combined_avg_time_spent = pd.DataFrame(
                    list(zip(day_viewed, date_viewed, cleaned_site_id, avg_time_spent)),
                    columns=['Day of Month', 'Date', 'Site ID',
                             'Average Time Spent on Site'])
                old_df_avts = pd.concat([combined_avg_time_spent, df_avg_time_spent])
                df_avg_time_spent = old_df_avts
    except Exception as e:
        print(f"Unexpected {e=}, {type(e)=}")
        raise

    result_1 = df_page_view.merge(df_uniq_visitor, how='outer')
    result_2 = result_1.merge(df_total_time_spent, how='outer')
    result_3 = result_2.merge(df_visit, how='outer')
    result = result_3.merge(df_avg_time_spent, how='outer')
    result = result.sort_values(by=['Site ID', 'Day of Month'], ascending=True)
    result.to_csv('data.csv', index=False)
    return result.shape


def transpose_data(df_dataset_list, day_viewed, date_viewed, cleaned_site_id, header_type):
    data_per_header = [p for p in df_dataset_list if isinstance(p, int)]
    combined_data = pd.DataFrame(list(zip(day_viewed, date_viewed, cleaned_site_id, data_per_header)),
                                 columns=['Day of Month', 'Date', 'Site ID', header_type])
    return combined_data


if __name__ == '__main__':
    dataset = pd.read_excel('data.xlsx')
    dim_result = metrics_extract(dataset)
    print(dim_result)
