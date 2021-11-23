import query
from function import execute_query
from function import execute_and_print_query
if __name__ == "__main__":
    execute_query(query.create_table_query)
    execute_query(query.insert_data_query)
    execute_query(query.show_table_employee_payroll)