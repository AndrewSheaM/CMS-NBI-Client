# IMPORT STATEMENT
from CMSNBIClient import CMS_NBI_Client
from CMSNBIClient import Create_E7_Data
# IMPORT STATEMENT

# Create the CMS_NBI_Client() instance
client = CMS_NBI_Client()

# Next step is to submit a login request to the CMS server, I will be using an example node
client.login_netconf(message_id='1',
                     cms_user_nm=client.cms_nbi_config['cms_nodes']['example_node']['cms_creds']['user_nm'],
                     cms_user_pass=client.cms_nbi_config['cms_nodes']['example_node']['cms_creds']['pass_wd'],
                     cms_node_ip=client.cms_nbi_config['cms_nodes']['example_node']['connection']['cms_node_ip'],
                     uri=client.cms_nbi_config['cms_netconf_uri']['e7'])
# if the login_netconf() function is successful a tuple with (True, '') is returned  else a response.Models.Response object is returned
# you can use the response library to debug the response.models.response object

# Next we create a Create_E7_Data instance and pass the CMS_NBI_Client instance to it
create_e7_data = Create_E7_Data(client)
# Once the Create_E7_Data object is created we can then call the ont() function and create a new ont record

# When creating an ONT we have a plethora of variables and combination to leverage. I will provide examples for some ONT configurations that I personally use day to day.
# THE DEFAULT CMS SERVER CONTAINS A GROUP OF DEFAULT ONT-PROFILES THAT CAN BE USED TO FILL THE ontprof_id variable.
# These profiles can be found on pg.136 of Calix Management System (CMS) R15.x Northbound Interface API Guide
# these profiles are the default and new custom profiles can be created to meet network design requirements.

# CREATE A DEFAULT 812G ONT, USING THE FIRST ONT_ID available on NTWK-Example_Name.
# Coupled with ont_sn='0', this call will tell the cms server to create a new ont record with no SN allowing us to fill it in later.
create_e7_data.ont( message_id='1',
                    cms_user_nm=client.cms_nbi_config['cms_nodes']['example_node']['cms_creds']['user_nm'],
                    network_nm='NTWK-Example_Name',
                    http_timeout=1,
                    ont_id='0',
                    admin_state='enabled',
                    ont_sn='0',
                    reg_id='',
                    sub_id='999999',
                    ont_desc='Example_Description',
                    ontpwe3prof_id='1',
                    ontprof_id='162')

# CREATE A DEFAULT 812G ONT, USING THE FIRST ONT_ID AVAILABLE ONT NTWK-Example_Name
# With this call we provided the ONT_SN, this will create a record tying the ONT_SN to the ONT provisioning, once the ont is discovered by the E7 the config is pushed.
create_e7_data.ont( message_id='1',
                    cms_user_nm=client.cms_nbi_config['cms_nodes']['example_node']['cms_creds']['user_nm'],
                    network_nm='NTWK-Example_Name',
                    http_timeout=1,
                    ont_id='0',
                    admin_state='enabled',
                    ont_sn='0',
                    reg_id='',
                    sub_id='999999',
                    ont_desc='Example_Description',
                    ontpwe3prof_id='1',
                    ontprof_id='162')
