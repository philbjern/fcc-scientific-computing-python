OUTPUT_SPACES = 1
DESC_MAX_LEN = 23
AMOUNT_MAX_LEN = 7

class Category:
    def __init__(self, category='other'):
        self.ledger = []
        self.category = category

    def __str__(self):
        width = DESC_MAX_LEN + AMOUNT_MAX_LEN
        stars_amount = (width - len(self.category)) // 2
        
        category_str = ''
        category_str += '*' * stars_amount
        category_str += str(self.category) 
        category_str += '*' * stars_amount
        
        while len(category_str) < width:
            category_str += '*'
        category_str += '\n'

        for item in self.ledger:
            category_str += f'{item["description"][:DESC_MAX_LEN]:{DESC_MAX_LEN}}' + \
                    f'{self.format_amount(item["amount"])[:AMOUNT_MAX_LEN]:>{AMOUNT_MAX_LEN}}\n'

        category_str += f'Total: {self.format_amount(self.get_balance())}'

        return category_str

    def get_name(self):
        return str(self.category)

    def format_amount(self, amount):
        return str("{:.2f}".format(amount))

    def deposit(self, amount, description=''):
        if amount:
            self.ledger.append({'amount': amount, 
            'description': description})
        else:
            print('No deposit amount')

    def withdraw(self, amount, description=''):
        if not self.check_funds(float(amount)):
            return False
        self.ledger.append({'amount': -float(amount), 
        'description': description})
        return True

    def get_balance(self):
        return sum(map(lambda x: float(x['amount']), self.ledger))

    def transfer(self, amount, dest_category):
        if not amount:
            print('No amount to transfer')
            return False
        elif self.get_balance() < amount:
            print('Not enought funds for transfer')
            return False

        transfer_description = f'Transfer to {dest_category.get_name()}'
        if self.withdraw(amount, f'Transfer to {dest_category.get_name()}'):
            dest_category.deposit(amount, f'Transfer from {self.get_name()}')
            return True

    def check_funds(self, amount):
        return float(amount) <= sum(map(lambda x: float(x['amount']), self.ledger))

    def total_spent(self):
        return self.format_amount(sum(map(lambda x: x['amount'] if x['amount'] < 0 else 0, self.ledger)))

CHART_OFFSET = 1
CATEGORY_START_INDEX = 5

def create_spend_chart(categories):
    cat_amount = len(categories)
    line_width = (cat_amount * 3) + 1

    chart_str_lines = ['Percentage spent by category\n']
    for i in range(10, -1, -1):
        chart_str_lines.append(f'{str(i * 10):>3}|{" " * line_width}\n')
    
    chart_str_lines.append(' ' * 4 + '-' * line_width + '\n')

    total_spent = 0
    cat_spent = []
    for cat in categories:
        total_spent += -float(cat.total_spent()) if cat.total_spent() != 0 else 0
        cat_spent.append(-float(cat.total_spent()) if cat.total_spent() != 0 else 0)

    cat_index = CATEGORY_START_INDEX

    for cat in cat_spent:
        percent = (cat / total_spent) * 100

        for i in range(int(percent / 10)):
            line_index = 10 - i
            chart_str_lines[line_index] = chart_str_lines[line_index][:cat_index] + 'o' + \
            chart_str_lines[line_index][cat_index + 1:]
        cat_index += 3
            
    # fill zero line
    cat_index = CATEGORY_START_INDEX
    for i in range(len(categories)):
        chart_str_lines[11] = chart_str_lines[11][:cat_index] + 'o' + \
            chart_str_lines[11][cat_index + 1:]
        cat_index += 3

    # add category description
    max_category_name = max(map(lambda x: len(x.get_name()), categories))
    for i in range(max_category_name):
        chart_str_lines.append(' ' * 4 + ' ' * line_width + ('\n' if i < max_category_name - 1 else ''))

    cat_index = CATEGORY_START_INDEX
    start_legend_line = 13

    for cat in categories:
        cat_name_idx = 0
        for line_idx in range(start_legend_line, start_legend_line + max_category_name):
            chart_str_lines[line_idx] = chart_str_lines[line_idx][:cat_index] + \
            cat.get_name()[cat_name_idx] + \
            chart_str_lines[line_idx][cat_index + 1:]

            if cat_name_idx < len(cat.get_name()) - 1:
                cat_name_idx += 1
            else:
                break
        cat_index += 3
        cat_name_idx = 0

    return ''.join(chart_str_lines)


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(10.15, 'groceries')
food.withdraw(10.15, 'groceries')
food.withdraw(10.15, 'groceries')
food.withdraw(10.15, 'groceries')
food.withdraw(10.15, 'groceries')
food.withdraw(10.15, 'groceries')
food.withdraw(10.15, 'groceries')
food.withdraw(10.15, 'groceries')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(20.15, 'groceries')
entertainment = Category('Entertainment')
entertainment.deposit(1000, 'deposit')
entertainment.withdraw(200, 'concert')
print(food)

print(create_spend_chart([food, clothing, entertainment]))
