from datetime import datetime as dt


def make_log(activity: str):
    timestamp = dt.now().strftime('%m/%d/%Y, %H:%M:%S')
    record = f'{timestamp} - {activity}'
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{record}\n')
