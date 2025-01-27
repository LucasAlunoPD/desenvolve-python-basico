import datetime


now = datetime.datetime.now()


data_formatada = f"{now.day:02d}/{now.month:02d}/{now.year}"
hora_formatada = f"{now.hour:02d}:{now.minute:02d}"


print(f"Data: {data_formatada}")
print(f"Hora: {hora_formatada}")
