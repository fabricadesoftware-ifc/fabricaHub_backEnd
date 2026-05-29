from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if response is not None:
        custom_data = {
            'erro': True,
            'status_code': response.status_code,
            'mensagem': response.data.get('detail', 'Ocorreu um erro na requisição.'),
        }
        
        if response.status_code == 400:
            custom_data['campos'] = response.data
            
        response.data = custom_data
        
        
    return response
