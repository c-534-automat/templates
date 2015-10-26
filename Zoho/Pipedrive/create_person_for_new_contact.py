# Create new pipedrive person for zoho contact.
{
    "new_mapper":"
        input_mapper_data = in_dict.get(
        'response').get('result').get('Contacts').get('row').get('FL')
    
        def set_mapper_data(input_mapper_data):
            contact_names = {}
            phones = []
            emails = []
            for elem in input_mapper_data:
                key, value = get_item_list(elem)
                set_phones(key, value, phones)
                set_emails(key, value, emails)
                set_first_last_names(key, value, contact_names)
            contact_name = ' '.join([contact_names.get('first_name'), 
                contact_names.get('last_name')])
            mapper_data = {
                'name': contact_name,
                'email': emails,
                'phone': phones
            }
            return mapper_data
        
        def set_emails(key, val, emails):
            if key == 'Email':
                emails.append(val)
            elif key == 'Secondary Email':
                emails.append(val)
                
        def set_first_last_names(key, val, contact_names):
            if key == 'First Name':
                contact_names['first_name'] = val
            elif key == 'Last Name':
                contact_names['last_name'] = val
            
        def set_phones(key, val, phones):
            if key == 'Phone':
                phones.append(val)
            elif key == 'Mobile':
                phones.append(val)
            elif key == 'Home Phone':
                phones.append(val)
            elif key == 'Asst Phone':
                phones.append(val)
            elif key == 'Other Phone':
                phones.append(val)
                
        def get_item_list(elem):
            return elem.get('val'), elem.get('content')
    
    out_dict = set_mapper_data(input_mapper_data)"
    
    "parameters_in":{
        "api_url":"https://crm.zoho.com/crm/private/json/",
        "api_method":"Contacts/getRecordById?scope=crmapi&id=Insert_your_contact_id_here",
        "api_token":"Insert_your_zoho_token_here",
        "http_method":"GET",
        "error_codes":[
            4422,
            4600,
            4834,
            500
        ],
    },
    "name":"P_zoho_2",
    "connector_in":"Zoho, v1.0",
    "connector_out":"Pipedrive, v1.0",
    "parameters_out":{
        "api_url":"https://api.pipedrive.com/v1",
        "api_method":"/persons",
        "error_codes":[
            501,
            401
        ],
        "api_token":"Insert_your_pipedrive_token_here",
        "http_method":"POST",
        "rest_data":{}
    }
}
