# WordCounter
Website Word Counter API

## Process on counting words
- Get all the text of the whole body page with BS4
- Split the text with 'space'
- loop the resulting list 
    - check if it is equal the given word


## Endpooint
### https://webwordcounter.herokuapp.com/wordcount
```python

input_json = {
"word": "Word",
"url": "sample_url"
}

output_json = {
    "count": 2,
    "status": "ok"
}
```

### Use Cases
#### Use Case 1
```python
input_json = {
"word": "Phones",
"url": "https://webscraper.io/test-sites/e-commerce/allinone/phones"
}

output_json = {
    "count": 2,
    "status": "ok"
}
```

#### Use Case 2
```python
input_json = {
"word": "Phones",
"url": "sample_url"
}

output_json = {
    "msg": "could not parse the page",
    "status": "fail"
}
```