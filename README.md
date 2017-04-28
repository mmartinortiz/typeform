# typeform
A python wrapper for the typeform API

# Installation
Clone the original repo </br>
```bash
git clone https://github.com/WarmongeR1/typeformPython.git
```

or this fork
```bash
git clone https://github.com/mmartinortiz/typeform
```

In the base directory run:
```bash
python setup.py install
```

# Usage
**Instantiating a form object**
```python
from typeform import TypeFormAPI
api = TypeFormAPI(API_KEY)
exampleForm = api.get_form(formKey)
```

**Retrieving questions from a form object**
```python
questionDict = exampleFrom.get_questions()
```
Returns a dictionary of the form `{questionToken: Question Text}`

**Retrieving responses from a form object**
```python
responseDict = exampleForm.get_all_completed_responses()
```

Returns all responses in form: `{responseToken: {questionToken: answerString....}}`

**Get average rating of a rating or opinion question**
```python
rating = exampleForm.get_average_rating(questionToken)
```

# Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
