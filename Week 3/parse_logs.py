import json

with open("/home/cowrie/cowrie/var/log/cowrie/cowrie.json") as reader:
	login_success = 0
	command_input = 0
	login_failed = 0
	session_connect = 0
	for line in reader:
		entry = json.loads(line)

		if entry.get("eventid") == "cowrie.login.success":
			print("=== LOGIN SUCCESS ===")
			print("Time:",entry.get("timestamp"))
			print("IP:",entry.get("scr_ip"))
			print("Username:",entry.get("username"))
			print("Password:",entry.get("password"))
			print("-" * 40)
			login_success+=1
		elif entry.get("eventid")=="cowrie.command.input":
			print("=== COMMAND EXECUTED ===")
			print("Time:", entry.get("timestamp"))
			print("IP:",entry.get("src_ip"))
			print("command:", entry.get("input"))
			print("-" * 40)
			command_input+=1
		elif entry.get("eventid") == "cowrie.login.failed":
			print("=== LOGIN FAILED ===")
			print("Time:", entry.get("timestamp"))
			print("IP:", entry.get("src_ip"))
			print("Username:", entry.get("username"))
			print("Password:", entry.get("password"))
			print("-" * 40)
			login_failed+=1
		elif entry.get("eventid") == "cowrie.session.connect":
			print("=== NEW CONNECTION ===")
			print("Time:", entry.get("timestamp"))
			print("IP:", entry.get("src_ip"))
			print("-" * 40)
			session_connect+=1
	print("========== SUMMARY ==========")
	print("Total Connections:", session_connect)
	print("Total Failed Logins:", login_failed)
	print("Total Successful:", login_success)
	print("Total Commands:", command_input)
