MINUTES_IN_DAY = 24 * 60

DAYS_OF_WEEK = ['monday', 'tuesday', 'wednesday',
    'thursday', 'friday', 'saturday', 'sunday']

def add_time(start, duration, day_of_week=''):
    print(f'\n{start}')
    start_time = start.split(' ')[0]
    am_pm = start.split(' ')[1]
    hours = int(start_time.split(':')[0])
    if am_pm == 'PM':
        hours += 12
    minutes = int(start_time.split(':')[1])
    minutes += hours * 60
    
    duration_hours = int(duration.split(':')[0])
    duration_minutes = int(duration.split(':')[1])
    duration_minutes += duration_hours * 60
    print('Duration minutes: ',duration_minutes)
    
    days_offset = (minutes + duration_minutes) // MINUTES_IN_DAY

    new_hours = (minutes + duration_minutes) // 60 - (24 * days_offset)
    print('New hours 1: ', new_hours)
    if new_hours >= 12:
        if new_hours > 12:
            new_hours -= 12
        am_pm = 'PM'
    else:
        if new_hours == 0:
            new_hours = 12
        am_pm = 'AM'
    print('New hours:', new_hours, am_pm)

    new_minutes = (minutes + duration_minutes) % 60
    if new_minutes < 10:
        new_minutes = '0' + str(new_minutes)
    print('New minutes: ', new_minutes)
    new_time = f'{new_hours}:{new_minutes} {am_pm}'

    print('Days offset: ', days_offset)
    if day_of_week != '':
        day_index = DAYS_OF_WEEK.index(day_of_week.lower())
        new_day_name = DAYS_OF_WEEK[(day_index + days_offset) % len(DAYS_OF_WEEK)]
        new_time += f', {new_day_name[0].upper() + new_day_name[1:]}'

    if days_offset == 1:
        new_time += ' (next day)'
    elif days_offset > 1:
        new_time += f' ({days_offset} days later)'

    return new_time


if __name__ == '__main__':
    print(add_time('3:30 PM', '2:12'))
    print(add_time('11:55 AM', '3:12'))
    print(add_time('11:59 PM', '24:05'))
    print(add_time('3:30 PM', '2:12', 'Monday'))
    print(add_time('11:59 PM', '24:05', 'Wednesday'))
