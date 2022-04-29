## Helping TOM

### Installation

``pip install -r requirements.txt``

### Run

``python Analysis.py``

### Run with args

You can pass duration (in seconds) for consuming the websocket.
Default is 1 minute.

For example if you pass 
``python Analysis.py -d 5`` 
the socket will consume data for 5 seconds and will print the summary of the block after that 
it will restart the same process again.

### Sample Output:

```json
{
    "max_number": 4294859789,
    "min_number": 310951,
    "first_number": 4071864609,
    "last_number": 1938045417,
    "number_of_prime_numbers": 240,
    "number_of_even_numbers": 2483,
    "number_of_odd_numbers": 2472
}

```