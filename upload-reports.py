import requests

headers = {
    'Authorization': f'Token {$DEFECTDOJO_API_KEY}'
}

url = 'https://demo.defectdojo.org/api/v2/import-scan'

data = {
    'active': True,
    'verified': True
    'scan_type': 'Gitleaks Scan',
    'minimum_severity': 'Low'
    'engagement': 19
}

files = {
    'file': open('gitleaks.json', 'rb')
}

response = requests.post(url, headers=headers, data=data, files=files)

if response.status_code == 201:
    print('Scan results imported successfully')
else:
    print('Failed to import scan results: {response.content}')