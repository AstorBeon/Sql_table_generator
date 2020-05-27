# Sql_table_generator
Creates sql command to create table + populate it with data of you own. 
Handy to create with own data or mock data (provided in repo)

#example


generator = Sql_table_generator()
generator.create_table("People",["Name","Surname", "Email"],["varchar(255)","varchar(255)","varchar(255)"])
generator.create_inserts(values=[["Mike","Ike","Like"],["Wazowski","Losco","Tump"],["b@a.com","lol@goal","biz@email.gov.com"]],shuffle=True,amount=3)
generator.save(path="")
