# Update configurations
import json
import sys
import boto3

with open('model/algo_config', 'r') as f:
    config = json.load(f)

account=boto3.client('sts').get_caller_identity().get('Account')
user_account=config['user']+'@'+account
config["user_account"] = user_account

algo_name=sys.argv[1]
config["algo_name"] = algo_name
with open("model/algo_name", "w") as text_file:
    text_file.write(algo_name)

with open("model/algo_config", "w") as text_file:
    text_file.write(json.dumps(config))    

print("config=%s" % json.dumps(config))