hours_slept = float(input("How many hours did you sleep today? "))

if hours_slept > 8:
    print('Drink melatonin at 12 am today. Avoid naps during the day.')
elif hours_slept == 8:
    print('Drink melatonin at 11 pm today.')
elif 7 <= hours_slept < 8:
    print('Drink melatonin at 10 pm today.')
else:
    print('Hard days happen. I believe in you.')
