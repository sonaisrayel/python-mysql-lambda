from  main import lambda_handler

event = [
	{
		"ID": 11,
		"name": "Lily",
		"city": "Yerevan"
	},
	{
		"ID": 12,
		"name": "Bob",
		"city": "Gyumri"
	},
	{
		"ID": 13,
		"name": "Bruce",
		"city": "Brazil"
	}
]

lambda_handler(event)