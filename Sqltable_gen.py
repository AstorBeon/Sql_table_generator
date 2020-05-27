import random
import sys


class Sql_table_generator:

    def __init__(self, tablename: str = ""):

        self.tablename = tablename
        self.result = ""

    # Possible tables: Name, Surname, Fullname, Email, Company, City, Region
    # only up to 100 recs :(

    def create_table(self, tablename: str, list_of_colnames: [str], list_of_types: [str]) -> None:

        """
        Function creates sql command to create new table with provided params.
        :param tablename: name of table to be created
        :param list_of_colnames: list of strings, containing names of columns to be created
        :param list_of_types:  list of strings, containing types of columns to be created
        :return:
        """

        self.result = f"CREATE TABLE {tablename}(\n" + "".join([f"{list_of_colnames[i]} {list_of_types[i]},\n" for i in range(len(list_of_colnames))])[:-2] + "\n);\n" if len(list_of_types) == len(list_of_colnames) else sys.exit("Columns and types lists have unequal lengths")


    def create_inserts(self, values: [[]], amount: int = -1, shuffle=False) -> None:
        """
        Function create insert commands.
        :param values: list of lists with string values to be put into
        :param amount: number of inserts to be created
        :param shuffle: controls if data should be shuffled
        :return:
        """
        inserts = ""  # list of lists
        # check if all lists in values has proper length
        length = len(values[0])
        for i in values:
            if len(i) != length:
                raise Exception("All lists")

        # if amount not set, then going for length
        if amount == -1:
            amount = length
        if amount > length:
            raise Exception("Amount is higher than max length of datatable")

        # shuffling
        if shuffle:
            for d in values:
                random.shuffle(d)


        #generating inserts
        for i in range(amount):
            inserts += f"INSERT INTO {self.tablename}, VALUES( "
            for val in values:
                inserts += f"'{val[i]}',"

            # deleting last comma
            inserts = inserts[:-1]
            inserts += " );"

        self.result += inserts

    def save(self, path=""):
        newpath = ""
        if path.endswith(".txt"):
            newpath = path
        else:  # path.endswith("/") or path.endswith("\\"):
            newpath = path + f"SQL_buildup-{self.tablename}.txt"

        with open(newpath, "w") as target:
            target.write(self.result)



generator = Sql_table_generator()
generator.create_table("People",["Name","Surname", "Email"],["varchar(255)","varchar(255)","varchar(255)"])
# generator.create_inserts(values=[["Mike","Ike","Like"],["Wazowski","Losco","Tump"],["b@a.com","lol@goal","biz@email.gov.com"]],shuffle=True,amount=3)
# generator.save(path="")