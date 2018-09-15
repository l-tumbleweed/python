product_list = [
    ('Iphone', 6000),
    ('bicycle', 2300),
    ('mac', 1200),
    ('coffee', 35),
    ('book', 100),
]

shopping_list = []

salary = input("input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index, item in enumerate(product_list):
            print(index, item)
        user_choice = input("请选择商品编号：")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] < salary:
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("added %s into shopping cart,your current balance is %s" % (p_item, salary))
                else:
                    print("你的余额只剩[%s]拉" % salary)
            else:
                print("product code [%s] i not exist" % user_choice)
        elif user_choice == 'q':
            print("-----------shopping list-------------")
            for i in shopping_list:
                print(i)
            print("your current balance:", salary)
            exit()
        else:
            print("invalid option")



