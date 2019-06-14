# Uses Python3

'''Problem: Check brackets in the code
Problem Introduction
In this problem you will implement a feature for a text editor to find errors in the usage of brackets in the
code.
Problem Description
Task. Your friend is making a text editor for programmers. He is currently working on a feature that will
find errors in the usage of different types of brackets. Code can contain any brackets from the set
[]{}(), where the opening brackets are [,{, and ( and the closing brackets corresponding to them
are ],}, and ).
For convenience, the text editor should not only inform the user that there is an error in the usage
of brackets, but also point to the exact place in the code with the problematic bracket. First priority
is to find the first unmatched closing bracket which either doesn’t have an opening bracket before it,
like ] in ](), or closes the wrong opening bracket, like } in ()[}. If there are no such mistakes, then
it should find the first unmatched opening bracket without the corresponding closing bracket after it,
like ( in {}([]. If there are no mistakes, text editor should inform the user that the usage of brackets
is correct.
Apart from the brackets, code can contain big and small latin letters, digits and punctuation marks.
More formally, all brackets in the code should be divided into pairs of matching brackets, such that in
each pair the opening bracket goes before the closing bracket, and for any two pairs of brackets either
one of them is nested inside another one as in (foo[bar]) or they are separate as in f(a,b)-g[c].
The bracket [ corresponds to the bracket ], { corresponds to }, and ( corresponds to ).
Input Format. Input contains one string 𝑆 which consists of big and small latin letters, digits, punctuation
marks and brackets from the set []{}().
Constraints. The length of 𝑆 is at least 1 and at most 105.
Output Format. If the code in 𝑆 uses brackets correctly, output “Success" (without the quotes). Otherwise,
output the 1-based index of the first unmatched closing bracket, and if there are no unmatched closing
brackets, output the 1-based index of the first unmatched opening bracket.'''

def check_brackets(s):
    bracket_stack = []
    index_stack = []
    open_brackets = ['(','[','{']
    close_brackets = [')',']','}']
    ret = 0
    for i,c in enumerate(s):
        if c in open_brackets:
            bracket_stack.append(c)
            index_stack.append(i)
        elif c in close_brackets:
            if len(bracket_stack) == 0:
                ret = i + 1
                #print("Unmatched closing bracket")
                break
            op = bracket_stack.pop()
            index_stack.pop()
            # match
            if open_brackets.index(op) != close_brackets.index(c):
                #print("Unmatched closing bracket")
                ret = i + 1
                break  
    if ret == 0 and len(bracket_stack) != 0:
        #print("Unbatched opening bracket")
        while(len(index_stack) > 1):
            index_stack.pop()
        ret = index_stack.pop() + 1
    return ret

def main():
    s = input()
    i = check_brackets(s)
    if i == 0:
        print('Success')
    else:
        print(i)

if __name__ == '__main__':
    main()
