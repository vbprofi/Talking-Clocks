Dim speaks, speech 

Set speech = CreateObject("sapi.spvoice") 
set speech.Voice = speech.GetVoices.Item(0) 'sprache ändern
speech.Rate = 6
speech.Volume = 100

'aktuelle Uhrzeit
speaks = "Es ist " & hour(time) & " Uhr und " & minute(time) & " minuten"
speech.Speak speaks

'aktuelles Datum
speaks = "Heute ist " & WeekdayName(Weekday(date())) & " der " & day(date()) & ". " & MonthName(month(date()), False) & " " & year(date())
speech.Speak speaks