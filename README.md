# typeform
A python wrapper for the typeform API

#Installation
Clone the repo </br>
<pre><code>git clone https://github.com/WarmongeR1/typeformPython.git </pre></code>
In the base directory run:
<pre><code>python setup.py install
</pre></code>


#Usage
<b>Instantiating a form object</b>
<pre><code>from typeform import TypeFormAPI
api = TypeFormAPI(API_KEY)
exampleForm = api.get_form(formKey)
</pre></code>

<b>Retrieving questions from a form object</b>
<pre><code>questionDict = exampleFrom.get_questions()
</pre></code>
Returns a dictionary of the form {questionToken: Question Text}

<b>Retrieving responses from a form object</b>
<pre><code>responseDict = exampleForm.get_all_completed_responses()
</pre></code>

Returns all responses in form: {responseToken: {questionToken: answerString....}}

<b> Get average rating of a rating or opinion question</b>
<pre><code>rating = exampleForm.get_average_rating(questionToken)
</pre></code>


## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
