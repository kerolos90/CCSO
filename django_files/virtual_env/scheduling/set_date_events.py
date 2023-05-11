import datetime, json

weekly_pattern = [
    ['gold', 'gold', '#400f0f', '#400f0f', 'gold', 'gold', 'gold'],
    ['#400f0f', '#400f0f', 'gold', 'gold', '#400f0f', '#400f0f', '#400f0f']
]

# Create empty arrays for the gold and brown teams
gold_team = []
brown_team = []
colored_dates = []
# Set the start date to a Monday
start_date = datetime.date(2023, 1, 9)

def schedule_pattern(s_date):
    while(s_date <= datetime.date(2024, 5, 30)):
        num_days = 14  # generate dates for 14 days
        # Loop through the number of days
        for i in range(num_days):
            # Determine the current week and the current day within that week
            current_week = i // 7
            current_day = i % 7

            # if weekly_pattern[current_week][current_day] == 'gold':
            #     gold_team.append(s_date.strftime('%Y-%m-%d'))
            # else:
            #     brown_team.append(s_date.strftime('%Y-%m-%d'))

            colored_dates.append(
                    {
                        'start': s_date.strftime('%Y-%m-%d'),
                        'display': 'background',
                        'color': weekly_pattern[current_week][current_day]
                    }
                )
            s_date += datetime.timedelta(days=1)
    return s_date

schedule_pattern(start_date)

# with open("gold_dates.json", "w") as outfile:
#     # Write the Python array to the JSON file
#     json.dump(gold_team, outfile)