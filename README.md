Online Job Application is a tedious and long process. The candidates have to fill up long forms and sometimes even the good candidates do not get filtered out by the resume filtering system of companies. Even a lot of time of the employers is taken by selection of the right candidate through resume. Sometimes, many good candidates don’t make the cut because of some candidates who look better on paper. This project doesn’t aim to entirely replace the current system but to automate it. It aims at improving the current process.

Project Description:

•	A web-app is made using Django.

•	The homepage shows the current openings for the company. Details of the Job Requirements can be seen by clicking on the Job openings.

•	The user needs to first upload his/her resume for the interested job profile. The vital details like Name, Phone, E-mail and the matching skills for the job are extracted from the resume using NLP and shown on the next page.

•	The pdf file is processed using spacy library from which all the text of pdf is first extracted. From the extracted text, important details are found. Name is found using a matching function, phone number and email are extracted by using regular expressions. For extracting skills, a csv file is made as a reference which has a collection of different skills. The text from pdf is compared with the csv and all matching values are then filtered out as skills. Also, the skills of candidates are then compared with the skills required for the job opening and the matching skills are displayed to the employer as well as employee.

•	The candidate is then asked some questions based on the skills required. The questions are pre-decided by the employer.

•	The model answers are also saved in the system.

•	Both the model answers and the candidates’ answers are preprocessed. Stemming is performed first, then the punctuations are removed, then they are normalized and finally vectorized by using TfidfVectorizer(). Then, stopwords from both the answers are removed.

•	These preprocessed answers of the candidate are then compared to the preprocessed model answers and evaluated by using cosine similarity function of nltk library.

•	The average of the cosine similarities of all answers is calculated and saved.

•	Django provides a pre-built admin interface.

•	This interface can be used by the recruiter to:
Post job openings, Look at candidate’s profile(from the data extracted), See the answers by the candidate, See the performance of the candidate.
