import os
import requests
import sys

file_name = sys.argv[1]
scan_type = ''

match file_name:
    case "gitleaks.json":
        scan_type = "Gitleaks Scan"
    case "njsscan.sarif":
        scan_type = "SARIF"
    case "semgrep.json":
        scan_type = "Semgrep JSON Report"
    case _:
        print("Comando no reconocido")

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
    'scan_type': scan_type,
    'minimum_severity': 'Low',
    'engagement': '27'
}

with open(file_name, 'rb') as f:
    files = {
        'file': f
    }

    response = requests.post(url, headers=headers, data=data, files=files)

if response.status_code == 201:
    print('Scan results imported successfully')
else:
    print(f'Failed to import scan results: {response.content}')