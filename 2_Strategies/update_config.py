# Update configurations
import json
import sys
import boto3
import sagemaker as sage

sess = sage.Session()

with open('model/algo_config', 'r') as f:
    config = json.load(f)

account=boto3.client('sts').get_caller_identity().get('Account')
user_account=config['user']+'@'+account
config["user_account"] = user_account
config["region"]=sess.boto_session.region_name

algo_name=sys.argv[1]
config["algo_name"] = algo_name
with open("model/algo_name", "w") as text_file:
    text_file.write(algo_name)

try:
    s3 = boto3.client('s3')
    s3.download_file('ee-assets-prod-us-east-1', 'modules/7c974653c2164bcab350d902744088c5/v1/algo_event.config', 'algo_event.config')
    with open('algo_event.config', 'r') as f:
        event_config = json.load(f)
    config['submitUrl']=event_config['submitUrl']
except:
  print("Skipped event config") 
    
with open("model/algo_config", "w") as text_file:
    text_file.write(json.dumps(config))    

print("config=%s" % json.dumps(config))