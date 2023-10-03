from django.shortcuts import render
from django.http import JsonResponse

from django.conf import settings
# import openai
import google.generativeai as palm
import google.api_core.exceptions as exceptions

# open_api_key ='<Enter your api key here>'
# openai.api_key = open_api_key

# API_KEY = '<Enter your api key here>'
API_KEY=settings.BARD_API_KEY
palm.configure(api_key=API_KEY)

# def ask_openai(message):
#     reponse = openai.Completion.create(
#         model = "text-davinci-003",
#         prompt = message,
#         max_tokens = 50,
#         n=3,
#         stop=None,
#         temperature=0.7,
#     )

#     # print(response)
#     answer = reponse.choice[0].text.strip()
#     return answer

try:
    def ask_bardai(message):
        model_list = [_ for _ in palm.list_models()]
        for model in model_list:
            print(model.name)

        # Example 1. Text Generation
        model_id = 'models/text-bison-001'
        # prompt = '''
        # what is compiler design
        # '''
        completion = palm.generate_text(
            model = model_id,
            prompt=message,
            temperature=0.99, #the randomness of the output
            #The maximum length of the response
            max_output_tokens=800,
            candidate_count=8,
        )
        # print(completion)
        # completion.result
        
        outputs = [output['output'] for output in completion.candidates]
        for output in outputs:
            # print(output)
            # print('-'*50)
            return output
            # return '-'*50



    # Create your views here.
    def chatbot(request):
        if request.method == 'POST':
            message = request.POST.get('message')
            response = ask_bardai(message)
            return JsonResponse({'message': message, 'response': response})

        return render(request, 'chatbot.html')
        
except Exception as e:
    print("Sorry for the inconvenience, we couldn't find your result")
    