<h2>Instruction: </h2>
<br>
1. Use this command in console to install all dependencies:

```
pip freeze > requirements.txt  
pip install -r requirements.txt
```
<br>
2. Also use this to start project:

```
python startapp.py
```
<br>
3. To add data: write lines in in url http://127.0.0.1:8080/add_data (post). I used Postman<br>
Example:

```
{
    "strings_list": ["one", "two", "three", "four", "five", "six", "seven", "eleven", "nine", "ten"]
}
```
* Tips:
  * Add only massive, otherwise you will take mistake
  * Don't add empty massive, otherwise you will take mistake
<br>
4. After you get and add some data - you can receive file with result in this path:

```
-- media 
------ txt 
--------- result.txt ✅
```
<br>
5. Also you can receive data in  url http://127.0.0.1:8080/get_data

