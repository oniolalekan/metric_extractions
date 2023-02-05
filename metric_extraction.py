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
                page_view = [p for p in df_dataset_list if type(p) == int]
                combined_page_view = pd.DataFrame(list(zip(day_viewed, date_viewed, cleaned_site_id, page_view)),
                                                  columns=['Day of Month', 'Date', 'Site ID', 'Page Views'])
                old_df_pv = pd.concat([combined_page_view, df_page_view])
                df_page_view = old_df_pv
            elif "Unique Visitors" in i:
                uniq_visitors = [u for u in df_dataset_list if type(u) == int]
                combined_unique_visitors = pd.DataFrame(list(zip(day_viewed, date_viewed, cleaned_site_id, uniq_visitors)),
                                                        columns=['Day of Month', 'Date', 'Site ID', 'Unique Visitors'])
                old_df_uv = pd.concat([combined_unique_visitors, df_uniq_visitor])
                df_uniq_visitor = old_df_uv
            elif "Total Time Spent" in i:
                tt_spent = [t for t in df_dataset_list if type(t) == int]
                combined_time_spent = pd.DataFrame(list(zip(day_viewed, date_viewed, cleaned_site_id, tt_spent)),
                                                   columns=['Day of Month', 'Date', 'Site ID', 'Total Time Spent'])
                old_df_ttt = pd.concat([combined_time_spent, df_total_time_spent])
                df_total_time_spent = old_df_ttt
            elif "Visits" in i:
                visits = [v for v in df_dataset_list if type(v) == int]
                combined_visit = pd.DataFrame(list(zip(day_viewed, date_viewed, cleaned_site_id, visits)),
                                              columns=['Day of Month', 'Date', 'Site ID', 'Visits'])
                old_df_vst = pd.concat([combined_visit, df_visit])
                df_visit = old_df_vst
            else:
                avg_time_spent = [a for a in df_dataset_list if type(a) == float]
                combined_avg_time_spent = pd.DataFrame(list(zip(day_viewed, date_viewed, cleaned_site_id, avg_time_spent)),
                                                       columns=['Day of Month', 'Date', 'Site ID',
                                                                'Average Time Spent on Site'])
                old_df_avts = pd.concat([combined_avg_time_spent, df_avg_time_spent])
                df_avg_time_spent = old_df_avts
    except Exception as e:
        print(f"Unexpected {e=}, {type(e)=}")
        raise

    result_page_view = df_page_view.sort_values(['Site ID', 'Day of Month'])
    result_uniq_visitors = df_uniq_visitor.sort_values(['Site ID', 'Day of Month'])
    result_total_time_spent = df_total_time_spent.sort_values(['Site ID', 'Day of Month'])
    result_visits = df_visit.sort_values(['Site ID', 'Day of Month'])
    result_average_time_spent = df_avg_time_spent.sort_values(['Site ID', 'Day of Month'])

    result_1 = result_page_view.merge(result_uniq_visitors, how='outer')
    result_2 = result_1.merge(result_total_time_spent, how='outer')
    result_3 = result_2.merge(result_visits, how='outer')
    result = result_3.merge(result_average_time_spent, how='outer')
    result.to_csv('df_to_csv4.csv', index=False)
    return result.shape


if __name__ == '__main__':
    dataset = pd.read_excel('test_data.xlsx')
    print(dataset.shape)
    dim_result = metrics_extract(dataset)
    print(dim_result)
