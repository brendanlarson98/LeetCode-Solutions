# https://leetcode.com/problems/generate-parentheses/

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

def valid(pars):
    balance = 0
    for i in pars:
        if i == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    if balance == 0:
        return True

def generate_parentheses(n):
    parentheses = []
    totals = []
    def generate(parentheses):
        if len(parentheses) == 2*n:
            if valid(parentheses):
                totals.append(''.join(parentheses))
        else:
            
            parentheses.append('(')
            generate(parentheses)
            parentheses.pop()
            parentheses.append(')')
            generate(parentheses)
            parentheses.pop()
    generate(parentheses)

    print(totals)

generate_parentheses(1)
