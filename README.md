# NYT Front Page API

This is an application programming interface (API) for the front page of the New York Times.
Data for the API will be scraped starting Sep 1, 2024 and all data for any day after will be retrievable through the API. The next phase of the project will include collecting all data prior to Sep 1, 2024, possibly years of data for each front page of the NYT.

This project was inspired by the importance of spreading reliable and trustworthy information on a global scale, while helping developers retrieve any information they deem useful for any purposes such as research, statistical analysis, etc.

To run the current project:

1. Download the zip file and extract it on your local machine.
2. `cd` into the extracted directory.
3. Run `npm install` in the terminal to install the Node.js dependencies.
4. Create and enter your virtual environment to isolate Pyton dependencies:

macOS/linux:
> `python -m venv venv` and `source venv/bin/activate`(macOS/Linux)
> `source venv/bin/activate`

Windows:
> `python -m venv venv`
> `.\venv\Scripts\activate`

6. Run `pip install -r requirements.txt` in the terminal to install the necessary libraries.
7. Run `npm run dev` or `npm start` to launch the project.
8. Open your web browser and navigate to "localhost:3000".
