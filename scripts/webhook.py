import requests
import datetime

file_path = "last_pr_time_file.txt"

jenkins_params = {
    'token': 'aurora-labs-project',
}


gitlab_headers = {
    'PRIVATE-TOKEN': 'glpat--6XzBM7Gi-L9qFq8RyWR',
}

gitlab_params = {
    'state': 'opened',
}

response = requests.get('https://gitlab.com/api/v4/projects/44551806/merge_requests', params=gitlab_params, headers=gitlab_headers)
data = response.json()

current_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')

try:
    with open(file_path, 'r') as file:
        last_pr = file.read()
except:
    last_pr = current_time


while True:
    response = requests.get('https://gitlab.com/api/v4/projects/44551806/merge_requests', params=gitlab_params, headers=gitlab_headers)
    data = response.json()
    if len(data) == 0:
        pass
    else:
        for pr in data:
            pr_time = pr['created_at']
            if pr_time > last_pr:
                last_pr = pr_time
                with open(file_path, 'w') as file:
                    file.write(last_pr)
                requests.head('http://10.5.0.5:8080/job/debops-is-great/build', params=jenkins_params, auth=('admin', 'admin'))
