from django.shortcuts import render

# Create your views here.

def index(request):
    """
    #1. Varaible
        # Creating a variable in views.py
        # Send to html template and display
    var1 = "Broadway" # Simple variable, file, database, web-form (different sources)

    #2. Packaging
    context = {'key2', var1}

    #3. Sending value to html template
    return render(request, 'app6_1/index.html', context)

    #4. Display value on html template
    # {{ varaible_name }} # {{ key2 }}
    """

    # Tags
    # 1. autoescape
    # Sending value to template
    """
    var1 = "Welcome to mysite." # Direct Assign/Web Form/Url/File/Database Table
    var2 = "<h3>Welcome to mysite</h3>"
    context = {'title':var1, 'text1':var2} # key, value -> Dictionary
    # return render(request, 'app6_1/index.html')
    return render(request, 'app6_1/index.html', context)
    """

    """
    #2. comment
    #3. extends
    #4. block    
    # templates, extends, block    
    context = {'title_text':'About Us', 'body_text':'Filters the contents of the block through one or more filters. Multiple filters can be specified with pipes and filters can have arguments, just as in variable syntax.'}
    return render(request, 'app6_1/about.html', context)
    """

    #5. csrf_token # used in form which post values with post method

    #6. cycle
    context = {'persons':
        [
        {'first_name':'Mohit', 'last_name':'Maharjan', 'email':'mohit@gmail.com'},
        {'first_name': 'Sabin', 'last_name': 'Shrestha', 'email': 'sabin@gmail.com'},
        {'first_name': 'Simran', 'last_name': 'Sharma', 'email': 'simran@gmail.com'}
        ],
    }
    return render(request, 'app6_1/cycle.html', context)
