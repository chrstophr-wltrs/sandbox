from stack import Stack

def eval_postfix(expr):
    """
    1. Initialize a stack
    2. if next input is a number:
            Read the next input and push it onto the stack   
       else:         
            Read the next character, which is an operator symbol         
            Use top and pop to get the two numbers off the top of the stack         
            Combine these two numbers with the operation         
            Push the result onto the stack
    3. goto #2 while there is more of the expression to read
    4. there should be one element on the stack, which is the result 
        Return this
    """

def in2post(expr):
    """
    1. initialize stack to hold operation symbols and parenthesis
    2.  if the next input is a left parenthesis:
            Read the left parenthesis and push it onto the stack   
        else if the next input is a number or operand:
            Read the operand (or number) and write it to the output   
        else if the next input is an operator:
            while (stack is not empty AND               
                stack's top is not left parenthesis AND               
                stack's top is an operation with equal or higher precedence than the next input symbol):            
                    Print the stack's top
                    Pop the stack's top
                    Push the next operation symbol onto the stack
        else:
            Read and discard the next input symbol (should be a right parenthesis)
            Print the top operation and pop it
            while stack's top is not a left parenthesis:
                Print next symbol on stack and pop stack
            Pop and discard the last left parenthesis
    3. Goto #2 while there is more of the expression to read
    4. Print and pop any remaining operations on the stack
        There should be no remaining left parentheses
    """

def main():
    """"
    1.open file data.txt
    2.read an infix expression from the file
    3.display the infix expression
    4.call function in2post(expr) which you write 
        in2post() takes an infix expression as an input and returns an equivalent postfix expression as a string
        If the expression is not valid, raise a SyntaxError
        If the parameter expr is not a string, raise a ValueError
    5.display the postfix expression
    6.call function eval_postfix(expr) which you write 
        eval_postfix() takes a postfix string as input and returns a number
        If the expression is not valid, raise a SyntaxError 
    7.display the result of eval_postfix()
    """
    pass

def scratch():
    some_list = [1, 2, 3, 4]
    print(some_list[:-1])

if __name__ == "__main__":
    scratch()