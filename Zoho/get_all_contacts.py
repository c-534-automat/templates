# Get all contacts from zoho to c-534 dump. 
{
    "connector_in":"Zoho, v1.0",
    "parameters_out":{},
    "name":"Zoho_1",
    "parameters_in":{
        "api_url":"https://crm.zoho.com/crm/private/json/",
        "api_method":"Contacts/getMyRecords?scope=crmapi",
        "api_token":"Insert_your_token_here",
        "rest_data":"",
        "http_method":"GET",
        "error_codes":[
            4422,
            4600,
            4834
        ]
    },
    "connector_out":"Dump, v1.0",
    "new_mapper":"out_dict = in_dict"
}
