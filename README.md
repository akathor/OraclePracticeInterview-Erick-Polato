# Practice Exercise

## How to run it

### Requirements
- Python 3.*

### How to run the code
Just clone the repo in your local machine by running the following command in your terminal:
> git clone https://github.com/akathor/OraclePracticeInterview-Erick-Polato.git

Then access to the new directory and run the main.py file as follows:
> python main.py 


## Exercise:

given
· a list of fruit types, each fruit type with a price in €/Kg
· a list of fruits, each fruit with a weight

### TASK:

package the fruits in boxes of at most 1Kg
and for each package provide

· list of fruits contained
· package weight
· package price calculated as
· the price of the sum of the prices of the fruits, with 2 decimals
· plus a packaging fee per each package (independent of the content)

### notes:
· package the fruits in the same order they come, don't re-arrange them
· don't split the fruits, if the box is not full but the next fruit doesn't fit, the box will be closed with less than 1kg of fruits
· also, if the list of fruits finishes and there is still space in the current box, that last box is considered completed and packaged

### Example 1

fruit types: apple 4 € / Kg
packaging fee: 1€
fruits: apple 250g
response: box 1 - apple - 250g 2.00€

### Example 2

fruit types: apple 1€/Kg , avocado 10€/Kg
packaging fee: 1€
fruits: apple 300g, avocado 300g, apple 300g, apple 300g, avocado 300g
response

· box 1: apple, avocado, apple - 900g - 4,60€
· box 2: apple, avocado - 600g - 4,30€
