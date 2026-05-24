# Cloud Automation Project

## Aim
To automate cloud resource provisioning and monitoring using Python and AWS SDK.

## Technologies Used
- Python
- AWS CLI
- Boto3
- Git
- PowerShell

## Features
- Automatic S3 bucket creation
- Resource monitoring
- Logging and error handling
- Scheduled task execution
- Version control with Git

## Project Structure

Cloud-Automation-Project
│
├── scripts
│ ├── create_s3.py
│ └── monitor_resources.py
│
├── logs
│ └── automation.log
│
├── docs
├── outputs
├── README.md
└── requirements.txt

## How to Run

Activate environment:

```powershell
.\venv\Scripts\Activate
```

Create bucket:

```powershell
python scripts/create_s3.py
```

Monitor resources:

```powershell
python scripts/monitor_resources.py
```