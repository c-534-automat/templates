# Create new pipedrive person for zoho contact.
{
    "connector_in":"Zoho, v1.0",
    "parameters_out":{
        "api_url":"https://api.pipedrive.com/v1",
        "api_method":"/persons",
        "api_token":"Insert_your_pipedrive_token_here",
        "rest_data":{},
        "http_method":"POST",
        "error_codes":[
            501,
            401
        ]
    },
    "name":"P_zoho_2",
    "parameters_in":{
        "api_url":"https://crm.zoho.com/crm/private/json/",
        "api_method":"Contacts/getRecordById?scope=crmapi&id=insert_your_id_contact_here",
        "api_token":"Insert_your_zoho_token_here",
        "rest_data":"",
        "http_method":"GET",
        "error_codes":[
            4422,
            4600,
            4834
        ]
    },
    "connector_out":"Pipedrive, v1.0",
    "new_mapper":"
    in_data = in_dict.get('response').get('result').get('Contacts').get('row').get('FL')
    out_dict = {}
      def set_out_dict():
          first_name = ''
          last_name = ''
          phones = []
          emails = []
          for elem in in_data:
              key = elem.get('val')
              val = elem.get('content')
              if key == 'First Name':
                  first_name = val
              elif key == 'Last Name':
                  last_name = val
              elif key == 'Phone':
                  phones.append(val)
              elif key == 'Mobile':
                  phones.append(val)
              elif key == 'Home Phone':
                  phones.append(val)
              elif key == 'Asst Phone':
                  phones.append(val)
              elif key == 'Other Phone':
                  phones.append(val)
              elif key == 'Email':
                  emails.append(val)
              elif key == 'Secondary Email':
                  emails.append(val)
          name = ' '.join([first_name, last_name])
          out_dict['name'] = name
          out_dict['phones'] = phones
          out_dict['email'] = emails"
      set_out_dict()
}
