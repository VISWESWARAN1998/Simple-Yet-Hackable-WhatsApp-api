from whatsapp import WhatsApp
wapp = WhatsApp(100)
temp = """
Hi ! *$NAME* , you haved scored *$marks* in Exam

Your Detailed Report :
	_RANK_ : *$rank*
	_PERCENTILE_ : *$perc*
	_GRADE_ : *$grade*

:-) Keep Studying (y)
"""  # prefix the variables with a dollar sign
wapp.send_messages_in_batch('students.csv', temp)
