# Internal imports
from models.transaction import Transaction

class Initialize():
    
    def show_menu(self):
        print(50 * '-')
        print('Welcome to financial control!')
        print(50 * '-')

        print('1 - Add transaction')
        print('2 - View transactions')
        print('3 - Get out')
    
    def chose_options(self):
        option = input('\nChoose one of the options: ')

        if option not in ['1', '2', '3']:
            print('Invalid option!')
        
        return option
    
    def to_add(self):
        operation = input('Enter the type of operation: ')
        value = input('Enter the value of the operation: ')
        description = input('Enter the description: ')

        transacion = Transaction(operation, value, description)
        transacion.save()
        del transacion
    
    def to_view(self):
        for transaction in Transaction().view():
            print(transaction)
    
    def to_go_out(self):
        print('\nThank you, come back often!')



if __name__ == '__main__':
    init = Initialize()
    option = ''

    while option != '3':
        init.show_menu()

        option = init.chose_options()

        if option == '1':
            init.to_add()
        elif option == '2':
            init.to_view()
        elif option == '3':
            init.to_go_out()


'''
- Resgatar uma transação
- Excluir transação
- Editar transação
- Fazer o CRUD
'''