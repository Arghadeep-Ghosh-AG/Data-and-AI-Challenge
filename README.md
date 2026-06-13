# Data-and-AI-Challenge

# AI-Powered Candidate Ranking System

## Overview

Recruiters often rely on keyword matching systems that fail to identify strong candidates whose profiles may not contain exact keyword matches. This project introduces an AI-powered candidate ranking system that understands job requirements semantically and ranks candidates based on overall suitability rather than simple keyword overlap.

The system leverages modern Natural Language Processing (NLP) techniques, sentence embeddings, and hybrid scoring mechanisms to recommend the most relevant candidates for a given job description.

---

## Problem Statement

Traditional Applicant Tracking Systems (ATS) primarily use keyword-based filtering, which often leads to:

* Missing qualified candidates
* Poor relevance ranking
* Over-reliance on exact keyword matches
* Limited understanding of candidate experience

The objective of this project is to build an intelligent ranking system that:

* Understands the job description
* Understands candidate profiles
* Computes semantic similarity
* Incorporates behavioral signals
* Produces a recruiter-ready ranked shortlist

---

## Dataset

The project uses:

### Candidate Profiles

Contains information such as:

* Professional headline
* Summary/About section
* Skills
* Work experience
* Education
* Career history

### Behavioral Signals

Contains recruiter and platform interaction signals such as:

* Profile activity
* Recruiter engagement
* Response rate
* Assessment performance

### Job Description

A target job description against which candidates are evaluated.

---

## Approach

### Step 1: Candidate Profile Processing

Each candidate profile is transformed into a unified text representation containing:

* Headline
* Summary
* Skills
* Experience
* Current role

Example:

Headline: AI Engineer

Skills: Python, Machine Learning, NLP

Experience: Built recommendation systems using deep learning and transformers.

---

### Step 2: Job Description Understanding

The target job description is processed and converted into a dense vector representation using transformer-based embeddings.

---

### Step 3: Semantic Matching

The project uses:

BAAI/bge-small-en-v1.5

to generate embeddings for:

* Job Description
* Candidate Profiles

Cosine similarity is then used to measure relevance between the job description and candidate profiles.

---

### Step 4: Rule-Based Feature Engineering

Additional boosts are provided for candidates possessing highly relevant skills such as:

* Machine Learning
* Deep Learning
* NLP
* Retrieval Systems
* Ranking Systems
* LLM Applications
* Embeddings
* Vector Databases
* RAG Pipelines

---

### Step 5: Behavioral Scoring

Behavioral signals are normalized and combined into a single score.

Examples:

* Recruiter saves
* Profile views
* Response rate
* Assessment performance

---

### Step 6: Hybrid Ranking

Final score is calculated using:

Final Score =
0.70 × Semantic Score +
0.20 × Behavioral Score +
0.10 × Rule-Based Score

Candidates are ranked according to this score.

---

## Project Architecture

Job Description
↓
Embedding Model
↓
JD Embedding

Candidate Profiles
↓
Embedding Model
↓
Candidate Embeddings

↓

Cosine Similarity

↓

Behavioral Features

↓

Hybrid Scoring

↓

Candidate Ranking

↓

Top Recommended Candidates

---

## Technology Stack

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* Sentence Transformers
* PyTorch
* TQDM

### Embedding Model

* BAAI/bge-small-en-v1.5

---

## Project Structure

AI-Recruitment-Ranker/

├── data/

│ ├── candidates.jsonl

│ ├── job_description.txt

│ └── signals.csv

│

├── notebooks/

│ └── EDA.ipynb

│

├── src/

│ ├── preprocess.py

│ ├── embeddings.py

│ ├── scoring.py

│ ├── ranking.py

│ └── main.py

│

├── output/

│ └── submission.csv

│

├── models/

│ └── candidate_embeddings.npy

│

├── requirements.txt

│

└── README.md

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AI-Recruitment-Ranker.git

cd AI-Recruitment-Ranker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Execute:

```bash
python src/main.py
```

The ranked candidate list will be generated inside:

```text
output/submission.csv
```

---

## Output Format

| candidate_id | rank |
| ------------ | ---- |
| 1001         | 1    |
| 1045         | 2    |
| 1208         | 3    |

---

## Future Improvements

* Cross-Encoder Re-ranking
* LLM-Based Candidate Reasoning
* Skill Gap Analysis
* Explainable Recommendations
* Learning-to-Rank Models (XGBoost Ranker, LambdaMART)
* Recruiter Feedback Loop
* Real-Time Candidate Search

---

## Results

The system successfully ranks candidates using semantic understanding and behavioral insights, providing recruiter-ready recommendations that go beyond traditional keyword matching approaches.

---

## Author

Arghadeep Ghosh
Suman Mondal
Dhrubati Sur
Srijita Dan
