
#TODO
{
    "name":"client_process",
    "parameters_in":{
        "error_codes":[
            501,
            401
        ],
        "api_token":"Insert_your_api_token_here",
        "http_method":"GET",
        "api_method":"/deals/1",
        "rest_data":{},
        "url":"https://api.pipedrive.com/v1"
    },
    "new_mapper":"in_data = in_dict.get('data')\r\nout_dict = {\r\n    'Title': in_data.get('title'),\r\n    'TypeId': 256045332,\r\n    'Size': in_data.get('value')\r\n}",
    "connector_out":"Leankit Kanban, v1.0",
    "parameters_out":{
        "optional":{
            "position":"1",
            "board_id":"256063992",
            "lane_id":"256129213"
        },
        "command":"AddCard",
        "url":"Insert_your_account_name_here",
        "user":{
            "password":"Insert_your_account_email_address_here",
            "login":"Insert_your_account_password_here"
        }
    },
    "connector_in":"Pipedrive, v1.0"
}
