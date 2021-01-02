
def fcn(text:str, words:list):
    # dic = {}
    # text = text.lower().split()
    # print(text)
    # for i in words:
    #     dic[i] = text.count(i)
    # return dic

    answer ={}
    for i in words: answer[i] = text.lower().split().count(i)
    return answer

if __name__ == "__main__":
    print('Example: ')
    print(fcn(''' I was verry WAS happy i mum''',['i','was','mum','alio']))