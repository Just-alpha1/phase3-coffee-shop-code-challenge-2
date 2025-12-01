COFFEE SHOP DOMAIN PROJECT

A Python object-oriented programming project implementing a Customer–Coffee–Order domain model.
This project demonstrates classes, instances, object relationships, encapsulation, validation, and aggregate methods following object-oriented programming principles.

Features
Define Customer, Coffee, and Order classes
Many-to-many relationship between Customers and Coffees through Orders
Strict validation for attributes
Association and aggregate methods
Tracks all Order instances and relationships
Supports customer order creation and most aficionado calculation
Fully testable with pytest
Includes debug.py interactive console for manual testing

Setup Instructions
1. Clone the Repository
`bash
git clone git@github.com:Just-alpha1/phase3-coffee-shop-code-challenge-2.git
cd coffee-shop-domain-oop

2. Set Up Virtual Environment
`bash
pipenv install
pipenv shell

3. Install Dependencies
`bash
pipenv install pytest

4. Run Tests
`bash
pytest

5. Interactive Debugging
Run debug.py for manual testing:
`bash
python debug.py

Copyright (c) 2025 Collins Thuo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.