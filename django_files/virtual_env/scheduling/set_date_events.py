
# Dates
gold_dates = ['02-01','02-02']
brown_dates = ['01-02','01-03','01-06','01-07','01-08','01-11','01-12','01-16','01-17','01-20','01-21','01-22','01-25','01-26','01-30','01-31',]
colored_dates = []

twentyThree = {
    '2023': {
        'Gold' : {
            '01': ['01','04','05','09','10','13','14','15','18','19','23','24','27','28','29']
        },
        'Brown' : {
            '01' : []
        }
    }
}


# for year in twentyThree.keys():
#     for team in twentyThree[year].keys():
#         for month in twentyThree[year][team]:
#             print(twentyThree[year][team][month])

#Append Dates to colored_dates array
def append_events(dates, color):
    for date in dates:
        colored_dates.append(
            {
                'start': ('2023-' + date),
                'display' : 'background',
                'color' : color
            }
        )
append_events(gold_dates,'yellow')
append_events(brown_dates, '#8b4513')
