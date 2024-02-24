import psycopg2


db_data={
    'dbname':'Najottalim',
    'user':'postgres',
    'host':'localhost',
    'port':5432,
    'password':'ikrom0315'

    }


conn=psycopg2.connect(**db_data)
curr=conn.cursor()

#uyga vazifa

# def create_table(table_name): # table yaratish
#     try:
#         curr.execute(f"""
#         create table {table_name}(id int primary key, name varchar(20), age int);
#         """)
#         print("Table yaratildi")
#     except Exception as e:
#         print(f"Xato kiritildi", e)
#
# create_table('users_')


# def create_column(table_name, column_name, column_type): # Column qo'shish
#     try:
#         curr.execute(f"""
#         ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type};
#         """)
#         print("Yangi qator kiritildi!")
#
#     except Exception as e:
#         print(f"Xato kiritildi",{e})
# create_column(table_name='users_', column_name='city', column_type='varchar(20)')

# def drop_column(table_name, column_name): #Qatorni o'chirish
#     try:
#         curr.execute(f"""
#         alter table {table_name} drop column {column_name};
#         """)
#         print("Qator o'chirildi")
#     except Exception as e:
#         print(f"Bu column mavjud emas", e)
# drop_column(table_name='users_', column_name='city')
#


# def insert_table(table_name): #malumot qo'shish
#     try:
#         curr.execute(f"""
#         insert into {table_name} values
#         (1,'Ikrom', 19),
#         (2,'Alisher', 19),
#         (3,'Ahror', 23),
#         (4,'Bobur', 18);
#bookauthor
#         """)
#         print("Malumot kiritildi!")
#     except Exception as e:
#         print(f"Xato malumot kiritldi", e)
#
# insert_table('users_')

# def del_table(table_name, name_raw):
#     try:
#         curr.execute(f"""
#         delete from {table_name}  where name={name_raw};
#
#
#         """)
#         print("Malumot o'chirildi")
#     except Exception as e:
#         print(f"Bu malumot yo'q", e)
# del_table('users_', name_raw="'Ikrom'")


# def select_table(table_name):
#     try:
#         curr.execute(f"""
#         Select * from {table_name};
#
#         """)
#         data=curr.fetchall()
#         print(data)
#     except Exception as e:
#         print("Bu malumot yo'q")
#
# select_table('users_')

# def rename_table(old_table, new_table):
#     try:
#         curr.execute(f"""
#         alter table {old_table} rename to {new_table};
#
#         """)
#         print("Table nomi o'zgardi!")
#     except Exception as e:
#         print("Xato malumot", e)
#
# rename_table('users_', 'customer')


# def rename_column(table_name, old_column, new_column):
#     try:
#         curr.execute(f"""
#         alter table {table_name} rename column {old_column} to {new_column};
#
#         """)
#         print("column nomi o'zgardi!")
#     except Exception as e:
#         print("Xato malumot", e)
#
# rename_column('customer', 'name', 'fullname')

# def update_table(table_name, column, id, new_data ):
#     try:
#         curr.execute(f"""
#         update {table_name} set {column}='{new_data}'
#         where id ={id}
#         """)
#         print("O'zgartirildi")
#     except Exception as e:
#         print("Xato mamlumot kiritildi}",e)
#
#
# update_table('customer', 'fullname', 2,'Ikrom')

#
# def update_colum_type(table_name, column_name, type_):
#     try:
#         curr.execute(f"""
#         alter table {table_name}
#         alter column {column_name}
#         type {type_}
#
#         """)
#         print("O'zgartirildi!")
#
#     except Exception as e:
#         print("Xato malumot", e)
#
# update_colum_type('customer', 'fullname', 'varchar(40)')
#
#
#
#









# conn.commit()
# conn.close()




