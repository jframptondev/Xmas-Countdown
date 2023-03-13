from datetime import date
the_most_wonderful_time = date.today()
christmas_start = date(the_most_wonderful_time.year, 12, 1)
christmas_end = date(the_most_wonderful_time.year+1, 1, 1)
delta = christmas_start - the_most_wonderful_time
if the_most_wonderful_time >= christmas_start < christmas_end:
    print("Have a Merry Christmas!")
else:
    print("only ",delta.days," day's left until xmas!")