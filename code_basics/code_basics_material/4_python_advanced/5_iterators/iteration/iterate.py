price_details = []
with open("price_details.txt", 'r') as file:
    for price_detail in file:
        ticket, country, price, date = price_detail.split("|")
        price_details.append({
            'ticket': ticket,
            'country': country,
            'price': price,
            'date': date,
        })
print(price_details[:2])

# how the iteration moves
f = open('price_details.txt', 'r')
print(iter(f))
iteratee = iter(f)

print(next(iteratee))
print(next(iteratee))

# iterator custom class

class channels:
    def __init__(self):
        self.channel = ["BCOS", "NTA", "OSBC"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index +=1
        if self.index < len(self.channel):
            return self.channel[self.index]
        else:
            raise StopIteration

the_channel = channels()

for val in channels():
    print(val)

for _ in range(3):
    print(next(the_channel))
# print(next(the_channel))
# print(next(the_channel))

def remote_control():
    yield "BCOS"
    yield "NTA"
    yield "OSBC"

r_c = remote_control()
print(f"generators: {next(r_c)}")
print(f"generators: {next(r_c)}")
print(f"generators: {next(r_c)}")
# print(next(remote_control()))
# print(next(remote_control()))
# print(type(remote_control()))


def get_company_data():
    record = []
    for i in range(3):
        with open(f"stock_{i + 1}.txt", 'r') as f:
            # print(f) return obj
            content = f.read()
            record.append(content)
    return record

# print(get_company_data())

def get_company_data():
    record = []
    for i in range(3):
        with open(f"stock_{i + 1}.txt", 'r') as f:
            # print(f) return obj
            content = f.read()
            yield content
data = get_company_data()
print(f"yeilding one after the other: {next(data)}")
print(f"yeilding one after the other: {next(data)}")
print(f"yeilding one after the other: {next(data)}")
print(f"yeilding one after the other: {next(data)}")

# for data in get_company_data():
#     print(data)

# fibonaci series
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b, = b, a + b

# fib = fibonacci()
# for _ in range(10):
#     print(next(fib))