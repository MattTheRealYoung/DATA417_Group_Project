# Natural Language Processing Explaination

This code takes in a pdf resume and a job description text file and finds the cosine similarity between the unique words in the job description and resume.

### Preprocessing
First the files are pre processed to remove puncuation, isolate words, and remove common words (and duplicate words). These words are put into a list

### Difference of words
The words that are only in the resume are seperated from the resume words and stored as "excess words" these can then be used by the manager to refine future job descriptions (possibly)

The words that are only in the job description are seperated out for the manager to look at and provide feedback to the applicant. This is where we add a transparency element to the program

### Similarity

Now that there is a list of words in job description and words from the job description in the resume, the similarity between these lists is found using cosine similarity. This gives a "matching score".
The missing words can be looked at to see if the differences are important or more menial.
