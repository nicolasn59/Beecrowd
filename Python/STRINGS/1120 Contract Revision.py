# SUBPROGRAM
def fixContract(wrongDigit, contractValue):
    contractFilter = []
    for value in contractValue:
        if value != wrongDigit:
            contractFilter.append(value)
    if contractFilter == []:
        contractFilter.append('0')

    for i in range(len(contractFilter)):
        if len(contractFilter) > 1 and contractFilter[0] == '0':
            contractFilter.pop(0)

    filteredContract = ''.join(contractFilter)
    contractFilter.clear()

    return filteredContract


# MAIN
faultyDigit, negotiatedNumber = map(str, input().split())
while faultyDigit != '0' or negotiatedNumber != '0':
    fixedContract = fixContract(faultyDigit, negotiatedNumber)
    print(fixedContract)
    faultyDigit, negotiatedNumber = map(str, input().split())