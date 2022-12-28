# well-balanced brackets

def areBracketsBalanced(expr):

    stack = []
    for char in expr:

        if char in ["(", "{", "["]:
            stack.append(char)

        else:
            
            if not stack:
                return False

            current_char = stack.pop()

            if current_char == '(':
                if char != ")":
                    return False

            elif current_char == '{':
                if char != "}":
                    return False

            elif current_char == '[':
                if char != "]":
                    return False
 
    if stack:
        return False

    return True

def isBalanced(str):

    if areBracketsBalanced(str):
        print("Balanced.")

    else:
        print("Not balanced.")

if __name__ == "__main__":

    expr = "{()}[]"
    isBalanced(expr)

    expr = "{](]"
    isBalanced(expr)