# **Rocket Picture Downloader - Phase 2** 

The script follows a simple sequential workflow to process and save data: 

1. **Fetch Launch Data** : Retrieve the upcoming rocket launches from the Launch Library 2 (https://thespacedevs.com/llapi). 

2. **Save Launch Schedule** : Store the retrieved launch information locally. 

3. **Fetch Images** : Read the stored launch data to look up and request rocket pictures from the Internet. 

4. **Save Media** : Download and save the rocket pictures directly into local computer directories. 



```text
   CURRENT PROJECT
         │
         ▼
┌─────────────────┐
│ Launch Library  │
│      API        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Extract launch  │
│      data       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Parse image     │
│      URLs       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Download images │
└─────────────────┘
```

## **Roadmap** 

```text
☑ Phase 1 — Working script
     │
     ├── API request
     ├── JSON parsing
     └── Save images
     │
     ▼
☑ Phase 2 — Improved Python script
     │
     ├── Error handling
     ├── Logging
     ├── Configuration
     ├── Functions/modules
     └── Better filesystem handling
     │
     ▼
☐ Phase 3 — Automated testing
     │
     ├── pytest
     ├── Mock API responses
     ├── Test JSON parsing
     ├── Test failures
     └── Test image saving
     │
     ▼
☐ Phase 4 — Pipeline structure
     │
     ├── Extract
     ├── Transform
     ├── Load
     └── Configuration
     │
     ▼
☐ Phase 5 — Airflow
     │
     ├── DAG
     ├── API extraction task
     ├── image processing task
     ├── logging
     ├── retries
     └── scheduling
     │
     ▼
☐ Phase 6 — DataOps/DevOps
     │
     ├── Docker
     ├── CI tests
     ├── Airflow
     ├── environment variables/secrets
     └── Jenkins/GitHub CI
```