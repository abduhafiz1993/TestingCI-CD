#!/bin/bash

python3 -c "from tests import primetest; test_prime(1, False)"
python3 -c "from tests import primetest; test_prime(2, False)"
python3 -c "from tests import primetest; test_prime(8, False)"
python3 -c "from tests import primetest; test_prime(11, True)"
python3 -c "from tests import primetest; test_prime(25, False)"
python3 -c "from tests import primetest; test_prime(28, False)"