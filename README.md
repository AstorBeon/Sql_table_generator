# Sql_table_generator
Creates sql command to create table + populate it with data of you own.

#example
generator = Sql_table_generator()
generator.createTable("People",["Name","Surname", "Email"],["varchar(255)","varchar(255)","varchar(255)"])
generator.createInserts(values=[["Mike","Ike","Like"],["Wazowski","Losco","Tump"],["b@a.com","lol@goal","biz@email.gov.com"]],shuffle=True,amount=3)
generator.save(path="")