from datetime import datetime, timedelta


def main():
    y, d, h, m = [int(x) for x in input().split()]
    current_date = datetime.now()
    output_date = current_date.replace(year=current_date.year + y) \
        + timedelta(days=d, hours=h, minutes=m)
    print("{:%Y-%m-%d %H:%M}".format(output_date))


if __name__ == '__main__':
    main()
