import os
import requests

api_key = os.environ.get('DEFECTDOJO_API_KEY')

if not api_key:
    raise ValueError("La variable DEFECTDOJO_API_KEY no está definida en la pipeline.")

headers = {
    'Authorization': f'Token {api_key}'
}

url = 'https://demo.defectdojo.org/api/v2/import-scan/'

data = {
    'active': True,
    'verified': True,
    'scan_type': 'Gitleaks Scan',
    'minimum_severity': 'Low',
    'engagement': '27',
    
}

with open('gitleaks.json', 'rb') as f:
    files = {
        'file': f
    }

    response = requests.post(url, headers=headers, data=data, files=files)

if response.status_code == 201:
    print('Scan results imported successfully')
else:
    print(f'Failed to import scan results: {response.content}')