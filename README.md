# **Rocket Picture Downloader** 

# **User Story** 

**As a** space enthusiast, 

**I want to** automatically fetch upcoming rocket launch  schedules and download their corresponding images, 

**So that** I can keep a curated collection of rocket  pictures on my local computer. 

# **Workflow** 

The application follows a simple sequential workflow to process and save the data: 

1. **Fetch Launch Data** : Retrieve the upcoming rocket launches  from the Launch Library. 

2. **Save Launch Schedule** : Store the retrieved launch information  locally on John's computer. 

3. **Fetch Images** : Read the stored launch data to look  up and request rocket pictures from the Internet. 

4. **Save Media** : Download and save the rocket pictures  directly into John's computer directories. 

# **Acceptance Criteria** 

- The system must successfully connect to the Launch Library API to pull the next scheduled launches. 

- The application must store the retrieved launch metadata locally in a structured folder format. 

- The system must parse the saved metadata to extract image URLs and fetch media files via an internet connection. 

- Downloaded images must be written properly to the local file system without corruption. 

