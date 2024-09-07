# NYT Front Page API

![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

## Overview

This is an application programming interface (API) for the front page of the New York Times.
Data for the API will be scraped starting Sep 1, 2024 and all data for any day after will be retrievable through the API. The next phase of the project will include collecting all data prior to Sep 1, 2024, possibly years of data for each front page of the NYT.

## Purpopse

This project was inspired by the importance of spreading reliable and trustworthy information on a global scale, while helping developers retrieve any information they deem useful for any purposes such as research, statistical analysis, etc.

## Backend

(Under Dev) Database Schema:
https://drawsql.app/teams/cornell-university/diagrams/nyt-api-database-schema
<img width="1368" alt="Screenshot 2024-09-06 at 5 29 32 PM" src="https://github.com/user-attachments/assets/3298d5b9-1bb1-48ab-883d-23cbcde35f10">


## Getting Started

1. Download the zip file and extract it on your local machine.
2. `cd` into the extracted directory.
3. Run `npm install` in the terminal to install the Node.js dependencies.
4. Create and enter your virtual environment to isolate Pyton dependencies:

macOS/linux:
> `python -m venv venv`

> `source venv/bin/activate`

Windows:
> `python -m venv venv`

> `.\venv\Scripts\activate`

6. Run `pip install -r backend/requirements.txt` in the terminal to install the necessary libraries.
7. Run `npm run dev` or `npm start` to launch the project.
8. Open your web browser and navigate to "localhost:3000".
