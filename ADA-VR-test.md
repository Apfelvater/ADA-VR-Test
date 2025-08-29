# This is the assignment for Adaptive Authentication in Virtual Reality (ADA-VR)
---

Please fill in this assignment and submit it to register for this project group. For more information about the PG, check our website: https://en.cs.uni-paderborn.de/its/teaching/student-projects/projects/ada-vr-adaptive-authentication-in-virtual-reality

If you have questions, feel free to contact Emiram: ekablo@mail.uni-paderborn.de

**Remember to SUBMIT this assignment! Otherwise, it will be ignored!**

# 1. Motivation (10 points)

## 1.1 Why would you like to be part of this project group? What are your expectations?


YOUR ANSWER HERE

## 1.2 What makes you a suitable candidate for this PG?


YOUR ANSWER HERE

# 2 Academic Background (20 points)

## 2.1 Courses from our group

Please tell us if you have attended one of our courses or seminars in the last semesters like "Usable Security and Privacy", "Privacy and Technology" or TUSA/TUSP/CIA/HIPS Seminar. If you worked on a project or paper during the courses, write briefly about your research.

Specify if you have only attended or completed the course/seminar.

YOUR ANSWER HERE

## 2.2 Other Courses

Tell us if you have taken any other course in the field of security (e.g., Web Security) or if you have other knowledge/skills relevant for the project (e.g., Machine Learning, Signal Processing, VR, etc.).

YOUR ANSWER HERE

## 2.3 Programming Experience

Do you have any programming experience? If yes, with which languages? Specifically, do you have experience in VR development (Unity, C#)? For each language please specify your level of competence.

<i>Optional: If you like, you can share your personal programming projects with us by providing a link to the sources (Gitlab/Github/Drive etc.).</i>

YOUR ANSWER HERE

## 2.4 Human Computer Interaction, UX Design


Do you have knowledge in human-centered design, UX implementation, or experience with designing and conducting user studies? (Briefly explain)

YOUR ANSWER HERE

## 2.5 Role Preference 

What would be your preference if we would divide the group into two separate roles: Developer and UX/HCI researcher.
    
- Developers: you have a solid programming background and experience with back-end or front-end development
- UX/HCI Researchers: you have knowledge in human-centered design or experience designing /conducting user studies 

YOUR ANSWER HERE

# 3 Programming Task (30 points)

## Task: Behavioral Authentication via Keystroke Dynamics (Python) 

One way to improve security is to analyze how a password is typed, not just what is typed. This is called keystroke dynamics and is a form of behavioral biometrics.

### Task Description:
Write a Python program that: 

1. Asks the user to enter a password five times in a row.
2. For each attempt, records the time between each keypress.
3. Calculates the average inter-key timing pattern per user.
4. Simulates a login attempt and checks if the timing pattern is similar to the user’s “enrollment” attempts (for simplicity, use Euclidean distance between the new timing vector and the average vector—accept login if the distance is sufficiently small).

### Sample Input/Output:

```plaintext
Enter your password for enrollment (5 attempts):
Attempt 1: pa55word
Attempt 2: pa55word
...
(login phase)
Enter your password: pa55word
Access granted! (or Access denied!)
```

#### Hints: 
You may use any library that could fit the assignment. If you want to use a library that is not installed on this Jupyter Python Kernel (you will notice when it doesn't compile), please provide a link to a Git repository or Drive where we can download your project. The link should also include screenshots of your solution. 


```python

```
