Demonstrate usage of module name.  
Run 
```
python test_main.py
```
Output is
```
Called from module.py
Called from test_main.py
```
Or run
```
python example_module.py
```
output is
```
Called from module.py
```
Code defined in 
```
if __name__ == "__main__":
```
is executed when python executes file test_main.py but NOT when it is imported.  
Code in example_module.py is executed when module IS imported and invoked directly.
