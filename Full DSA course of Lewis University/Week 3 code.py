from stack_list import Stack, Empty
ops = '+-'

def Expression_Input():
    expression = []
    print("Enter the values until you enter operator except - or + ")
    while True:
        value = input("Enter input: ")
        expression.append(str(value))
        Opr = input("Enter Operator: ")  
        if Opr != '+':
            if Opr != '-':
                break 
        expression.append(str(Opr))
    return expression

tokens= Expression_Input()
val_stack = Stack()
op_stack = Stack()

def higher_priority(op1: str, op2: str):
    if op1 in '+-' and op2 in '+-':
        return True
    return False


for token in tokens:
    if token.isalnum():
        val_stack.push(token)
    elif token in ops:
        # compare priorities with top ops
        try:
            top_ops = op_stack.top()
        except Empty:
            #this is first operation seen, push it to ops_stack and continue
            op_stack.push(token)
            continue

        if higher_priority(top_ops, token):
            # need to evalute
            result = eval('{val1} {op} {val2}'.format(val2=val_stack.pop(),
                                                      val1 = val_stack.pop(),
                                                      op = op_stack.pop()))
            val_stack.push(result)

        op_stack.push(token)

while not op_stack.is_empty():
    result = eval('{val1} {op} {val2}'.format(val2=val_stack.pop(),
                                              val1 = val_stack.pop(),
                                              op = op_stack.pop()))
    val_stack.push(result)

print('result = {}'.format(val_stack.pop()))
print('done')