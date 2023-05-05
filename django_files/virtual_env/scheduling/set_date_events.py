
# # Dates
# import datetime
# gold_dates = ['02-01','02-02']
# brown_dates = ['01-02','01-03','01-06','01-07','01-08','01-11','01-12','01-16','01-17','01-20','01-21','01-22','01-25','01-26','01-30','01-31',]
# colored_dates = []

# twentyThree = {
#     '2023': {
#         'Gold' : {
#             '01': ['01','04','05','09','10','13','14','15','18','19','23','24','27','28','29']
#         },
#         'Brown' : {
#             '01' : []
#         }
#     }
# }


# # for year in twentyThree.keys():
# #     for team in twentyThree[year].keys():
# #         for month in twentyThree[year][team]:
# #             print(twentyThree[year][team][month])

# #Append Dates to colored_dates array
# def append_events(dates, color):
#     for date in dates:
#         colored_dates.append(
#             {
#                 'start': ('2023-' + date),
#                 'display' : 'background',
#                 'color' : color
#             }
#         )
# append_events(gold_dates,'yellow')
# append_events(brown_dates, '#8b4513')


# # Define the weekly pattern for the gold and brown teams
# weekly_pattern = [
#     ['gold', 'gold', 'brown', 'brown', 'gold', 'gold', 'gold'],
#     ['brown', 'brown', 'gold', 'gold', 'brown', 'brown', 'brown']
# ]

# # Create empty arrays for the gold and brown teams
# gold_team = []
# brown_team = []

# # Set the start date to a Monday
# start_date = datetime.date(2023, 1, 2)


# def schedule_pattern(s_date):
#     num_days = 14  # generate dates for 14 days
#     # Loop through the number of days
#     for i in range(num_days):
#         # Determine the current week and the current day within that week
#         current_week = i // 7
#         current_day = i % 7

#         # Determine which team is assigned for the current day
#         if weekly_pattern[current_week][current_day] == 'gold':
#             current_team = gold_team
#         else:
#             current_team = brown_team

#         # Add the current date to the current team's array
#         current_team.append(s_date.strftime('%Y-%m-%d'))

#         # Add the current date to the current team's array
#         current_team.append(s_date.strftime('%Y-%m-%d'))

#         # Add the current date to the current team's array
#         current_team.append(s_date.strftime('%Y-%m-%d'))

#         # Add the current date to the current team's array
#         current_team.append(s_date.strftime('%Y-%m-%d'))

#         # Increment the date by one day
#         s_date += datetime.timedelta(days=1)
#     for i in range(num_days):
#         # Determine the current week and the current day within that week
#         current_week = i // 7
#         current_day = i % 7

#         # Determine which team is assigned for the current day
#         if weekly_pattern[current_week][current_day] == 'gold':
#             current_team = gold_team
#         else:
#             current_team = brown_team

#         # Add the current date to the current team's array
#         current_team.append(s_date.strftime('%Y-%m-%d'))

#         # Add the current date to the current team's array
#         current_team.append(s_date.strftime('%Y-%m-%d'))

#         # Add the current date to the current team's array
#         current_team.append(s_date.strftime('%Y-%m-%d'))

#         # Add the current date to the current team's array
#         current_team.append(s_date.strftime('%Y-%m-%d'))

#         # Increment the date by one day
#         s_date += datetime.timedelta(days=1)
#     return s_date


# # Print the final arrays
# start_date = schedule_pattern(start_date)
# start_date = schedule_pattern(start_date)
# start_date = schedule_pattern(start_date)
# start_date = schedule_pattern(start_date)
# start_date = schedule_pattern(start_date)
# print("Gold Team Dates: ", gold_team)
# print("Brown Team Dates: ", brown_team)
# print(start_date)
