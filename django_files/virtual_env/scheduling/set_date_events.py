
# Dates
gold_dates = ['01-01','01-04','01-05','01-09','01-10','01-13','01-14','01-15','01-18','01-19','01-23','01-24','01-27','01-28','01-29','02-01','02-02']
brown_dates = ['01-02','01-03','01-06','01-07','01-08','01-11','01-12','01-16','01-17','01-20','01-21','01-22','01-25','01-26','01-30','01-31',]
colored_dates = []

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
