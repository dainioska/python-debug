
def fcn(text: str, begin: str, end: str):
    # start = text.find(begin)
    # finish = text.find(end)
    # print(start, ':', finish)

    # if start != -1 and finish != -1:
    #     start += len(begin)
    #     return (text[start:finish])
    # elif start == -1 and finish == -1:
    #     return text
    # elif start != -1 and finish == -1:
    #     start += len(begin)
    #     return text[start:]
    # elif start == -1 and finish != -1:
    #     start = 0
    #     return (text[start:finish])

    begin_idx = text.index(begin) + len(begin) if begin in text else 0
    end_idx = text.index(end) if end in text else len(text)
    return text[begin_idx: end_idx]


if __name__ == "__main__":
    print('Example:')
    print(fcn('N0 *>right<*', '*>', '<*'))
    print(fcn('N1 <*wrong*>', '*>', '<*'))
    print(fcn('N2 >hii', '>', '<'))
    print(fcn('N3 <hii', '>', '<'))
    print(fcn('N4 hii<', '>', '<'))
    print(fcn('ok', '>start<', '<stop>'))