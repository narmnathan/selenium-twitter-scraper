# for collecting links to aggregate information in the nitter scraper

nanterre = []
nahel = []
franceriots = []
francehasfallen = []
franceonfire = []
franceburning = []

def add(list):
    while True:
        prompt = input("Enter link to tweet, or 'exit' to exit: ")
        if prompt == 'exit':
            break
        else:
            list.append(prompt)
def view(list):
    print(*list, sep="\n")

add(nanterre)
print(nanterre)