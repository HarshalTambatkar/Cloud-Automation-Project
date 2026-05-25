# Cloud Automation Scripting using Python and AWS

## Project Overview
This project automates cloud resource provisioning and monitoring using Python and AWS services. The project uses AWS CLI, Boto3 SDK, logging, scheduling, and Git version control to automate cloud operations.

---

## Aim
To automate AWS cloud resource provisioning and monitoring tasks using Python and AWS SDK.

---

## Objectives

- Automate cloud resource provisioning
- Use Python with AWS SDK (Boto3)
- Implement error handling and logging
- Schedule automated monitoring tasks
- Use Git for version control
- Generate logs and sample outputs

---

## Technologies Used

- Python 3
- AWS CLI
- AWS S3
- Boto3
- PowerShell
- Git
- Windows Task Scheduler
- VS Code

---

## Project Structure

```text
Cloud-Automation-Project
│
├── scripts
│   ├── create_s3.py
│   └── monitor_resources.py
│
├── logs
│   └── automation.log
│
├── outputs
│   └── sample_output.txt
│
├── docs
│
├── README.md
├── requirements.txt
├── .gitignore
├── .git
└── venv
```

---

## Features

### 1. Automated Resource Provisioning

The create_s3.py script automatically creates an AWS S3 bucket.

Functionality:

- Connects to AWS using Boto3
- Creates S3 bucket
- Handles bucket existence errors
- Stores logs automatically

---

### 2. Resource Monitoring

The monitor_resources.py script monitors AWS resources.

Functionality:

- Connects to AWS S3
- Fetches available bucket information
- Displays bucket list
- Logs monitoring activity

---

### 3. Logging and Error Handling

The project implements:

- Python logging module
- Error handling using try-except blocks
- Automatic log generation

Log file:

```text
logs/automation.log
```

---

### 4. Task Scheduling

Windows Task Scheduler is used to automate monitoring execution.

Scheduled Task Name:

```text
Cloud Resource Monitor
```

Purpose:

- Automatically runs monitoring script
- Eliminates manual execution

---

### 5. Version Control

Git is used for:

- Tracking project changes
- Maintaining version history
- Managing project updates

Commands used:

```bash
git init
git add .
git commit -m "Initial cloud automation project"
```

---

## Installation Steps

### Clone/Open Project

```bash
cd C:\projects\Cloud-Automation-Project
```

### Activate Virtual Environment

```powershell
.\venv\Scripts\Activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Verify AWS Connection

```bash
aws sts get-caller-identity
```

### Run Bucket Creation Script

```bash
python scripts/create_s3.py
```

Expected Output:

```text
Bucket created successfully
```

or

```text
Bucket already exists
```

---

### Run Monitoring Script

```bash
python scripts/monitor_resources.py
```

Expected Output:

```text
Available Buckets:

config-bucket-xxxx
harshal-cloud-automation-bucket
```

---

### View Logs

```powershell
Get-Content .\logs\automation.log
```

---

### View Git History

```bash
git log --oneline
```

---

## Sample Output

```text
Bucket already exists

Available Buckets:

config-bucket-359289023183
harshal-cloud-automation-bucket

INFO - Bucket list fetched successfully
```

---

## Outcome

Successfully automated AWS cloud resource provisioning and monitoring using Python and Boto3 with logging, scheduling, and Git integration.

---

## Conclusion

This project reduces manual cloud management effort by automating AWS operations and demonstrates practical implementation of cloud automation, monitoring, scheduling, and version control techniques.
