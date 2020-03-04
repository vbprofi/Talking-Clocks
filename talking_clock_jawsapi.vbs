Option Explicit
Dim bFlush, oJaws
Dim speaks

' JawsAPI
Set oJaws = CreateObject("FreedomSci.JawsApi")

'aktuelle Uhrzeit
speaks = "Es ist " & hour(time) & " Uhr und " & minute(time) & " minuten"
bFlush = False
oJaws.SayString speaks, bFlush

'aktuelles Datum
speaks = "Heute ist " & WeekdayName(Weekday(date())) & " der " & day(date()) & ". " & MonthName(month(date()), False) & " " & year(date())
bFlush = False
oJaws.SayString speaks, bFlush