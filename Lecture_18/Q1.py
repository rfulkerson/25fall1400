# def print_price(item, cost):
#     print(f'{item} cost ${cost:.2f}')

def print_price(item, cost):
    print(f'{item:<15s}${cost:<10.2f}')

if __name__ == '__main__':
    print_price("Beans", 1.23)
    print_price("Corn", 0.59)
    print_price("Detergent", 8.92)
    print_price("baby spinach", 1.29)

# print()
# print("Beans priced at $1.23")
# print("Corn priced at $0.59")
# print("Detergent priced at $8.92")
# print("baby spinach priced at $1.29")

