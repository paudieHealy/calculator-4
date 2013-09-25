# Create your views here.

from django.shortcuts import render


# The action for calculator/show_calculator
def show_calculator(request):

    # Retrieves values from calculator
	result = ''
	storedResult = '0'
	storedOp = ''

	#check for existing result, storedVal, storedOp
	if 'result' in request.POST:
		result = request.POST['result']

	if 'storedVal' in request.POST:
		storedResult = request.POST['storedVal']

	if 'storedOp' in request.POST:
		storedOp = request.POST['storedOp']

	#press of number key
	if 'number' in request.POST:

		#concatenate numbers on the press of a number key
		result += request.POST['number']
		
	#press of an operation key	
	elif 'operation' in request.POST:

		#perform operation
		opType = request.POST['operation']

		if opType == '=':
			#equals button shows the result of all ops performed so far
			result = perform_op(int(storedResult), storedOp, int(result))
			storedOp = ''

		else:

			#what if there's already a stored result and stored optype? must store the result
			#for sucessive operations
			if storedOp != '':
				result = perform_op(int(storedResult), storedOp, int(result))

			#stores operation for sucessive ops, stores number entered as well for future ops, clears text
			storedOp = opType
			storedResult = result
			result = ''

	# Makes the data available to the view
	context = {'newResult':result, 'newStoredVal':storedResult, 'newStoredOp':storedOp}


	return render(request, 'calculator/calculator-main.html', context)

#helper function for performing an operation on two integers
def perform_op(num1, op, num2):
			
	if op == '+':
		result = num1 + num2
	if op == '-':
		result = num1 - num2
	if op == '*':
		result = num1 * num2
	if op == '/':
		if num2 == 0:
			result = 0
		else:
			result = num1 / num2

	return result


