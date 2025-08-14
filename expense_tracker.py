# Simple expense tracker.

expenses = {}
exp_num = 0
def add_expense(desc, amnt):
    global exp_num
    exp_num += 1
    if not str(amnt).isdigit(): return "Error"
    if len(desc) <= 1: return 'Error'
        
    expenses[f'Expense #{exp_num}'] = [exp_num, desc, amnt]
    return f'Expense added successfully (ID: {exp_num})'

def upd_expense(exp_id, desc, amnt):
    expenses[f'Expense #{exp_id}'] = [exp_id, desc, amnt]
    return f'Expense #{exp_id} updated successfully'

def expense_summ():
    print('# {0}  {1:<5}  {2:>5}'.format('ID', 'Description', 'Amount'))
    for exp, data in expenses.items():
        print('# {0}  {1:<5}  {2:>5}'.format(data[0], data[1], data[2]))
            
def expense_recap():
    exp_sum = 0
    for exp, data in expenses.items():
        try:
            exp_sum += int(data[2])
        except (ValueError, TypeError):
            print('Error. Value not convertible to int')
    print(f'Total expenses ${exp_sum}')
    
def export_expenses():
    with open('expenses.txt', 'w') as f:
        f.write('ID,Description,Amount\n')
        for exp, data in expenses.items():
            f.write('{0},{1},{2}\n'.format(data[0], data[1], data[2]))

while True:
    try:
        print('1. Add expense')
        print('2. Update expense')
        print('3. Delete expense')
        print('4. View all expenses')
        print('5. Summarize expenses')
        print('6. Export expenses')
        print('7. Exit')
        opt = int(input('Enter a number\n'))
        
        if opt == 1:
            info = input('Enter the descriiption of the expense:\n')
            ammnt = int(input('How much did it cost? :\n'))
            add_expense(info, ammnt)
        elif opt == 2:
            if exp_num == 0: 
                print('No expenses to update.')
                continue
            n_exp = int(input(f'Please enter the number of the expense you want to update.\nChoose between expense 1 to {exp_num}'))
            if n_exp > len(expenses):
                print('Number out of range.')
                continue
            else: 
                info = input('Enter the descriiption of the expense:\n')
                ammnt = int(input('How much? :\n'))
                upd_expense(n_exp, info, ammnt)
        elif opt == 3:
            n_exp = int(input(f'Please enter the number of the expense you want to delete.\nChoose between expense 1 to {exp_num}'))
            if n_exp > len(expenses):
                print('Number out of range.')
                continue
            else:
                del expenses[f'Expense #{n_exp}']
                print(f'Expense #{n_exp} deleted successfully.')
        elif opt == 4: # View all expenses
            expense_summ()
        elif opt == 5:
            expense_recap()
        elif opt == 6:
            export_expenses()
        elif opt == 7:
            print('Exiting'); break
        else:
            print('Please enter a valid option.')
    except KeyboardInterrupt:
        print('\nGoodbye!!')
        break
    except TypeError:
        print('Please enter a number.')
    