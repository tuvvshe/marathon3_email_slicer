email = input("ENTER YOU EMAIL: ").strip()
username = email[email.index("@")+1:]
domain_name = email[email.index("@")+1]
format_ = (f"YOUR USER NAME IS '{username}' AND YOUR DOMAIN NAME IS '{domain_name}'")
print(format_)