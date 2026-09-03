from pyscript import document

def compute(event):
    num1 = float(document.querySelector("#input1").value)
    num2 = float(document.querySelector("#input2").value)
    operation = document.querySelector("#operations").value

## the if statements for choosing operations and caluclations
    if operation == "add":
        ## adds num1 and num2
        result = num1 + num2

    elif operation == "subtract":
        ## subtracts num1 and num2
        result = num1 - num2

    elif operation == "multiply":
        ## multiplies num1 and num2
        result = num1 * num2

    elif operation == "divide":
        ## divides num1 and num2
        if num2 != 0: ## this detects if the user is dividng by zero by != 0
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operation"

    document.querySelector("#output").innerText = f"Result: {result}" ##outputs the result to the output div